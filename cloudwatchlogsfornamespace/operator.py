import kopf
import boto3
import logging
from kubernetes import client, config
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the Kubernetes client
config.load_incluster_config()
v1 = client.CoreV1Api()

# Initialize CloudWatch Logs client
cloudwatch_logs = boto3.client('logs')

# Create a logger
logger = logging.getLogger('k8s_operator')

# Define a Function to send logs to cloudwatch
def send_logs_to_cloudwatch(log_group_name, log_stream_name, log_data):
    try:
        # Create log group if not exists
        response = cloudwatch_logs.create_log_group(logGroupName=log_group_name)
    except cloudwatch_logs.exceptions.ResourceAlreadyExistsException:
        pass

    # Create log stream if not exists
    try:
        cloudwatch_logs.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
    except cloudwatch_logs.exceptions.ResourceAlreadyExistsException:
        pass

    # Send logs
    response = cloudwatch_logs.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=[{'timestamp': int(log_data['timestamp'] * 1000), 'message': log_data['message']}]
    )
    return response

#Watch Pod Events

@kopf.on.event('pods', namespace="default")  # change "default" to the desired namespace
def log_pod_event(event, **kwargs):
    pod_name = event['object']['metadata']['name']
    log_group_name = "k8s-logs"
    log_stream_name = pod_name

    if event['type'] in ['ADDED', 'MODIFIED']:
        try:
            pod_log = v1.read_namespaced_pod_log(name=pod_name, namespace="default")
            log_data = {'timestamp': event['object']['metadata']['creationTimestamp'], 'message': pod_log}
            send_logs_to_cloudwatch(log_group_name, log_stream_name, log_data)
            logger.info(f"Logs from {pod_name} sent to CloudWatch.")
        except Exception as e:
            logger.error(f"Failed to send logs for pod {pod_name}: {str(e)}")


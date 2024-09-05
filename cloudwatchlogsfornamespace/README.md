# Cloudwatch Logging
Creating a Kubernetes operator in Python that sends logs from the current namespace to CloudWatch involves several steps. The operator will watch for log events in the namespace and forward them to CloudWatch. Here’s a basic outline of how you can achieve this:

1. **Set Up Your Environment**
Ensure you have Python 3.6+ installed.
Install the required libraries:
```bash
pip install kubernetes boto3 kopf
```

2. **Python Code to send logs to namespace**

This is in operator.py

3. **Build and Push**
```bash
docker build -t your-operator-image .
docker push your-operator-image
```

4. **Deploy the operator**

```bash 
kubectl apply -f deployment.yaml

```

5. **Ensure IAM Permissions**
Ensure your Kubernetes service account (used by the operator) has IAM permissions to create log groups, log streams, and put log events in CloudWatch.

6. **Test and Monitor**
Monitor the operator’s logs to ensure it’s capturing pod logs and sending them to CloudWatch.
Check CloudWatch to verify logs are arriving as expected.
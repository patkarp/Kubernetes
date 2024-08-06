# Overview
What is Cross Plane ? 
Crossplane is an open-source Kubernetes add-on helpful in defining and managing cloud resources using Kubernetes-style APIs. Meanwhile, Terraform is a widely adopted infrastructure provisioning tool used to define and manage infrastructure as code across multiple cloud providers

### Step 1:  Lets Install Crossplane

Let's use helm to install crossplane:

```bash
helm repo add \
crossplane-stable https://charts.crossplane.io/stable && helm repo update

helm install crossplane \
crossplane-stable/crossplane \
--namespace crossplane-system \
--create-namespace
```

Check Pod Status

```bash
kubectl get pods -n crossplane-system
```
Check API Resources

```bash
kubectl api-resources  | grep crossplane
```

### Step 2: Create a Kubernetes secret for AWS or maybe Service Account Role, depending on security policy


Now create the secret below

```bash
kubectl create secret \
generic aws-secret \
-n crossplane-system \
--from-file=creds=./aws-credentials.txt
```

Check that the secret was created:
```bash
kubectl describe secret aws-secret -n crossplane-system
```

### Step 3: Get the AWS provider and provider config ready, or Any other Cloud Pro

Now let's configure the AWS provider and use the credentials we created. This provider.yaml will create a S3 Provider, or S3 CRD (Custom Resource defination)

```bash
kubectl apply -f provider.yaml -n crossplane-system
```

You now have your Kubernetes cluster ready with crossplane installed to work with s3

### Step 4: Create the S3 Bucket


Apply the configuration:

```bash
kubectl apply -f s3bucket.yaml
```

### Step 5: Verify Resource Status
Check the status of the resource claim to ensure the S3 bucket has been successfully provisioned:

```bash
kubectl get bucket
```

Upon successful provisioning, you should see the following output:

```
NAME                  READY   SYNCED   EXTERNAL-NAME         AGE
Patsbucket  True    True     Patsbucket   5m
```

### Step 6: Verify Drift Correction

Lets delete the bucket from the AWS console and wait for bucket to reappear. ETCD is responsible for restoring it to previous state


```bash
kubectl describe bucket
```

### Step 7: Cleanup and Delete

Delete the bucket run the command below:

```bash
kubectl delete -f s3bucket.yaml
```

# KubeMQ:
A message broker and message queue ideal for developers. Provides all messaging patterns, scalable, highly available, and secure. Connect microservices instantly using a rich set of connectors without writing any code. Easy-to-use SDKs and elimination of predefined topics, channels, brokers, and routes.

This project demonstrates how to deploy a simple Node.js application using KubeMQ on a Kubernetes cluster with Minikube.

## Prerequisites

- Docker
- Minikube
- kubectl

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/kubemq-sample-app.git
cd kubemq-sample-app

cd sample-app
docker build -t your-dockerhub-username/sample-app:latest .
```

2. **Build the Image**
```bash
cd sample-app
docker build -t your-dockerhub-username/sample-app:latest .

```

3. **Start Minikube**
```bash 
minikube start

```

4. **Apply Kubernetes Manifests**

```bash 
kubectl apply -f kubernetes/

```
5. **Access Application**
```bash 
minikube service sample-app --url

```

6. **Cleanup**
```bash 
kubectl delete -f kubernetes/

```

Project Structure
```go
kubemq-sample-app/
├── kubernetes/
│   ├── deployment.yaml
│   ├── kubemq.yaml
│   └── service.yaml
├── sample-app/
│   ├── Dockerfile
│   ├── index.js
│   └── package.json
└── README.md
```
This project demonstrates a simple setup of deploying a Node.js application with KubeMQ on Kubernetes using Minikube. The README.md file provides detailed instructions to get started and run the project.


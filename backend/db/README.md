# DB Container setup

Setting up the kubernetes resources for the DB. The files create a persistent volume of 5Gi, expose the service through NodePort 5432:30001, and use a postgres alpine image from dockerhub.

## Installation

Initiate with the following commands:

```bash
microk8s.kubectl apply -f backend/db/postgres-config.yaml
microk8s.kubectl apply -f backend/db/postgres-secret.yaml
microk8s.kubectl apply -f backend/db/postgres-storage.yaml
microk8s.kubectl apply -f backend/db/postgres-deployment.yaml
microk8s.kubectl apply -f backend/db/postgres-service.yaml
```


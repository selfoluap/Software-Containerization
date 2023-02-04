# Software-Containerization
App for WS2022 Course Software Containerization at VU

## Contents:
- /backend - Flask implementation for the back end of application
- /frontend - React implementation for the front end of application
- /helm-charts - Helm files to deploy application on cluster
- /kubernetes - Services, deployments, secrets, ingress etc.

## Deployment:


# Commands:

Containerize frontend:
```
sudo docker build -t frontend:v3 .
sudo docker images frontend (check image)
sudo docker run -p 8091:80 frontend:v3 (run test - localhost:8091)
sudo docker ps (if there is something, remove it by its ID with sudo docker rm *id*)
sudo docker tag frontend:v3 localhost:32000/frontend:v3 (tag the image)
sudo docker push localhost:32000/frontend:v3 (push it)
```

Kubernetes deployment for frontend:
```
microk8s kubectl apply -f frontend-deployment.yaml (create deployment)
microk8s kubectl get pods -l app=frontend (check pods)
microk8s kubectl apply -f frontend-service.yaml (create service)
```

Docker image for Flask API app:
```
sudo docker build . (build image)
sudo docker images (check image)
sudo docker tag *id of image* api:v3
sudo docker run -p 5000:5000 api:v3 (try - localhost:5000/server/get_task (depends on route))
```

Push image to Microk8s registry:
```
sudo docker tag api:v3 localhost:32000/api:v3
microk8s start
microk8s enable registry
sudo docker push localhost:32000/api:v3 (push image to the registry)
```

Kubernetes deployment for Flask API:
```
microk8s kubectl apply -f backend-deployment.yaml (create deployment)
microk8s kubectl apply -f backend-service.yaml (create service of type ClusterIP for the Flask api)
microk8s kubectl get svc (get cluter ips and ports)
```

Building database:
```
sudo microk8s apply -f postgres-config.yaml
sudo microk8s apply -f postgres-secret.yaml
sudo mkdir -p /opt/postgre/data
sudo microk8s kubectl apply -f postgres-storage.yaml 
sudo microk8s kubectl apply -f postgres-deployment.yaml
sudo microk8s kubectl apply -f postgres-service.yaml
psql -h localhost -U postgresadmin --password -p 30001 postgresdb
```

Kubernetes deployment for Ingress:
```
sudo microk8s kubectl apply -f ingress.yaml
```

Update kubernetes deployment after changing application:
```
sudo docker build . -t frontend:versionNumber
sudo docker tag frontend:versionNumber localhost:32000/frontend:versionNumber
sudo docker push localhost:32000/frontend:versionNumber
a. sudo microk8s kubectl set image deployments/frontend-deployment frontend-container=localhost:32000/frontend:versionNumber
b. sudo microk8s kubectl set image deployments/backend-deployment backend-container=backend:versionNumber
```


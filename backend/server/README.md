# Server setup

The server is containerized in its own pod and consists of a Flask API commiting changes to the postgres-service.

## Local development

For local development it is possible to use the .env file to store secrets and access them with python-dotenv.

## Setting up on kubernetes

The secrets that allow the access to the DB are stored within the deployment. The Deployment uses the image localhost:32000/tasksapp. To setup the image run:

```bash
sudo docker build backend/server/.
sudo docker tag <pod-name> localhost:32000/tasksapp:<version-number>
sudo docker push localhost:32000/tasksapp:<version-number>
```

To setup on kubernetes, run:

```bash
microk8s.kubectl apply -f backend/server/backend-deployment.yaml
microk8s.kubectl apply -f backend/server/service-deployment.yaml
```
# Software-Containerization
P3 Project Master Computer Science (VU / UVA)

## Project structure:
* `/backend` - Flask implementation for the back end of application
    * `server/`
        * `.env` - for local dev
        * `requirements.txt`
        * `server.py` - main api and db connection
        * `.dockerignore` - exclude .env
        * `Dockerfile`
* `/frontend` - React implementation for the front end of application
    * `public/`
    * `src/`
    * `frontend-nginx-custon.conf`
    * `Dockerfile`
* `/helm-charts` - Helm files to deploy application on cluster
    * `templates/`
        * `*.yaml` - chart k8s components
    * `Chart.yaml` - the chart
    * `values.yaml` - chart's values
* `presentation/` - presentation contents

* `/kubernetes` - Services, deployments, secrets, ingress etc.



## Setup:
On GCP we use a Standard Mode Regional Cluster. Create a cluster on GCP and connect the shell to it

Install the nginx ingress controller on GCP

Execute the following commands to install the nginx ingress controller
```
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm install nginx-ingress ingress-nginx/ingress-nginx
```

Wait a few moments while the load balancer gets deployed and then retrieve the EXTERNAL-IP associated with the nginx-ingress service
```
kubectl get service nginx-ingress-ingress-nginx-controller -ojson | jq -r '.status.loadBalancer.ingress[].ip'
```
The output should look like this 35.239.106.62. This IP address will later be used to set the correct hostname in the values.yaml of the helm chart. 

Build and push docker images to Container Registry
```
docker build . -t $YOUR_REGION_NAME/$YOUR_PROJECT_NAME/backend:v1
docker push $YOUR_REGION_NAME/$YOUR_PROJECT_NAME/backend:v1

docker build . -t $YOUR_REGION_NAME/$YOUR_PROJECT_NAME/frontend:v1
docker push $YOUR_REGION_NAME/$YOUR_PROJECT_NAME/frontend:v1
```
Create TLS Certificate
We already created the secrets, but with the following command new keys can be created.
```
openssl req -x509 -sha256 -nodes -newkey rsa:4090 -keyout key.pem -out cert.pem
```

Set up Artifact Registry on GCP


Package the helm chart and push it to Artifact Registry
```
helm package helm
helm push software-containerization-0.1.0.tgz oci://$YOUR_REGION_NAME-docker.pkg.dev/$YOUR_PROJECT_NAME/$YOUR_ARTIFACT_REPO_NAME
```

Install helm chart on GKE

```
helm install oci://YOUR_REGION_NAME-docker.pkg.dev/$YOUR_PROJECT_NAME/$YOUR_ARTIFACT_REPO_NAME/software-containerization-0.1.0
```


## Overview and Comands

![Kubernetes Architecture](presentation_/architecture.svg)

![Docker](presentation_/docker_architecture.png)

Check permissions for roles created by RBAC

```
kubectl auth can-i get configmaps --as <gcloud-user-email>
```
The cluster setup provides 3 RBAC roles: admin, developer, and devops-engineer.

Changing values in the Chart example: change the replicaCount to 5 in values.yaml and version to 0.1.1 in charts.yaml
```
helm upgrade --install software-containerization -f software-containerization-values.yaml software-containerization-0.1.1.tgz --set software-containerization.backend-deployment.replicaCount=5
```

After a source code change, the application can be rebuilt with the following:

```
docker build . -t  $YOUR_REGION_NAME/$YOUR_PROJECT_NAME/backend:v2
docker push  $YOUR_REGION_NAME/$YOUR_PROJECT_NAME/backend:v2
kubectl set image deployment/software-containerization-frontend-deployment software-containerization-frontend-container=gcr.io/$YOUR_PROJECT_NAME/backend:v2
```

To uninstall the application use:

```
helm uninstall software-containerization
```

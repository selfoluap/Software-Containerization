# Software-Containerization
App for WS2022 Course Software Containerization at VU

## Contents:
- /backend - Flask implementation for the back end of application
- /frontend - React implementation for the front end of application
- /helm-charts - Helm files to deploy application on cluster
- /kubernetes - Services, deployments, secrets, ingress etc.

## Requirements:

This repo assumes that you have microk8s installed with helm3 enabled and gcloud just be configured for your project.

For information on how to set up glcloud, please refer to https://cloud.google.com/sdk/docs/install

## Setup:
1. Create a cluster on GCP and connect to it
```
gcloud container clusters get-credentials $CLUSTER_NAME --zone $YOUR_ZONE --project $YOUR_PROJECT_NAME
```

2. Install the nginx ingress controller on GCP

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
The output should look like this:
    35.239.106.62

This IP address will later be used to set the correct hostname in the values.yaml of the helm chart. 

3. Build and push docker images to Container Registry
```
docker build . -t gcr.io/$YOUR_PROJECT_NAME/backend:v1
docker push gcr.io/$YOUR_PROJECT_NAME/backend:v1

docker build . -t gcr.io/$YOUR_PROJECT_NAME/frontend:v1
docker push gcr.io/$YOUR_PROJECT_NAME/frontend:v1
```
4. Create TLS Certificate
We already created the secrets, but with the following command new keys can be created.
```
openssl req -x509 -sha256 -nodes -newkey rsa:4090 -keyout key.pem -out cert.pem
```
You just need to make sure to replace the values in the tls-secret.yaml accordingly with the new values.


4. Set up Artifact Registry on GCP

4.1 Create a docker repository

4.2 Authenticate with an access token
```
gcloud auth print-access-token | sudo microk8s helm3 registry login -u oauth2accesstoken     --password-stdin https://us-central1-docker.pkg.dev
```
You should see a message "Login succeeded"


5. Package the helm chart and push it to Artifact Registry
```
sudo microk8s helm3 package helm
sudo microk8s helm3 push software-containerization-0.1.0.tgz oci://us-central1-docker.pkg.dev/$YOUR_PROJECT_NAME/$YOUR_ARTIFACT_REPO_NAME
```

6. Install helm chart on GKE

6.1 Open a terminal on GCP, connect to the correct cluster and type in
```
helm install $HELM_CHART oci://us-central1-docker.pkg.dev/$YOUR_PROJECT_NAME/$YOUR_ARTIFACT_REPO_NAME/$HELM_CHART --version 0.1.0
```


## Presentation

1. Architecture

2. Scaling

3. Upgrade and re-deployment

3.1 deployment rollout

3.2 canary update




## Fullfilled requirements


1. Persistent layer (SQL or No-SQL database)

2. REST API

3. Web front-end

4. Transport Level Security

5. Helm Chart

6. Security - Network policies

7. Google Cloud Platform (or other public cloud)



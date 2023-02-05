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
kubectl get deploy
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
To be able to push it to Container Registry, your gcloud must be authenticated first. Please refer to https://cloud.google.com/container-registry/docs/advanced-authentication#gcloud-helper for more information.

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


5. Set up Artifact Registry on GCP

5.1 Create a docker repository

5.2 Authenticate with an access token
```
gcloud auth print-access-token | helm registry login -u oauth2accesstoken  --password-stdin https://us-central1-docker.pkg.dev
```
You should see a message "Login succeeded"


6. Package the helm chart and push it to Artifact Registry
```
helm package helm
helm push software-containerization-0.1.0.tgz oci://us-central1-docker.pkg.dev/$YOUR_PROJECT_NAME/$YOUR_ARTIFACT_REPO_NAME
```

7. Install helm chart on GKE

7.1 Open a terminal on GCP, connect to the correct cluster and type in
```
helm install $HELM_CHART oci://us-central1-docker.pkg.dev/$YOUR_PROJECT_NAME/$YOUR_ARTIFACT_REPO_NAME/$HELM_CHART --version 0.1.0
```

## RBAC Permissions

    Check your permissions by running the example comand (replace get congigmaps with any other resource management comand)

    ```
    kubectl auth can-i get configmaps --as <gcloud-user-email>
    ```


## Presentation

Architecture:

Describe the architecture of the application using one or more types of UML diagrams - Max 2 points
Show and describe the artifacts you created to build the docker images - Max 1 point. 
Show and describe the artifacts created to deploy the application to Kubernetes - Max 2 points.

Show how you configured the pre-requisites for the application - Max 5 points
![Kubernetes Architecture](presentation_/architecture.svg)
Our Load Balancer is managed by Google and is automatically created, when the ingress resource is applied
We are not using the default gce ingress resource, but the more advanced nginx ingress controller

    helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
    helm repo update
    helm install nginx-ingress ingress-nginx/ingress-nginx

For our persistent volume we are using the standard storage class which is working fine with GKE. Adapted the mount
path to fit with the GCP path.

Our docker images are pushed to Container Registry and are also retrieved from there. Our helm charts are stored in 
Artifact Registry. Both are services provided by GCP.

![Docker](presentation_/docker_architecture.png)

Certificates: Explain how we create the TLS certificate

We decided to implement the following three roles: developer, devops-engineer and manager. We are adjusting the
permissions of the google users by binding these roles to them. 
    kubectl auth can-i delete pod --as g.savchenko@student.vu.nl

Network policies:


Show how you build the container images and publish to a registry (1 point):

    docker build . -t gcr.io/diesel-dominion-375713/frontend:vp1
    docker push gcr.io/diesel-dominion-375713/frontend:vp1

    docker build . -t gcr.io/diesel-dominion-375713/backend:vp1
    docker push gcr.io/diesel-dominion-375713/backend:vp1

Show how you deploy the application for the first time (1 point):

    helm package helm
    gcloud auth print-access-token | helm registry login -u oauth2accesstoken  --password-stdin https://us-central1-docker.pkg.dev
    helm push software-containerization-0.1.0.tgz oci://us-central1-docker.pkg.dev/diesel-dominion-375713/helm-repo
    gcloud artifacts docker images list us-central1-docker.pkg.dev/diesel-dominion-375713/helm-repo
    helm install software-containerization oci://us-central1-docker.pkg.dev/diesel-dominion-375713/helm-repo/software-containerization --version 0.1.0

Show how to scale the application horizontally (stateless parts only) (1 point):

    change replicaCount to 5 in values.yaml and version to 0.1.1 in charts.yaml
    helm upgrade software-containerization software-containerization-0.1.1.tgz

    or

    kubectl scale -n default deploy software-containerization-frontend-deployment --replicas=5
    kubectl scale -n default deploy software-containerization-backend-deployment --replicas=5


Show how you re-build the application after a source code change (1 point):

    docker build . -t gcr.io/diesel-dominion-375713/frontend:vptest1
    docker push gcr.io/diesel-dominion-375713/frontend:vptest1
    kubectl set image deployment/software-containerization-frontend-deployment software-containerization-frontend-container=gcr.io/diesel-dominion-375713/frontend:vptest1


Show how you upgrade the running application in two ways:
deployment rollout (2 points):

canary update (2 points):


Show how to uninstall the application (1 point):

    helm uninstall software-containerization
    kubectl get all -n default



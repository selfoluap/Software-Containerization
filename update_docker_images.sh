sudo docker build . -t localhost:32000/frontend:versionNumber frontend
sudo docker push localhost:32000/frontend:versionNumber 

sudo docker build . -t localhost:32000/backend:versionNumber
sudo docker push localhost:32000/backend:versionNumber

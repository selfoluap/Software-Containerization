# Software-Containerization
App for WS2022 Course Software Containerization at VU

cd frontend
npm install 

docker build -t frontend .
-> creates docker image

docker run -p 3001:3000 dev:frontend
-> runs docker and exposes port 3000 to other docker containers and 3001 to host
# Software-Containerization
App for WS2022 Course Software Containerization at VU

docker build --file=frontend/Dockerfile  -t frontend .
docker build --file=backend/Dockerfile  -t backend .
-> creates docker images

docker compose up -d db
docker compose up backend
docker compose up frontend

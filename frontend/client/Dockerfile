# Build image
FROM node as build-container 
WORKDIR /app 
COPY package*.json /app/ 
RUN npm install 
COPY . /app 
ARG configuration=production 
RUN npm run build --configuration $configuration 

# Create container with nginx 
FROM nginx 
COPY --from=build-container /app/build/ /usr/share/nginx/html 
COPY /frontend-nginx-custom.conf /etc/nginx/conf.d/default.conf

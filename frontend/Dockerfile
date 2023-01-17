FROM node:17-alpine

WORKDIR /app

COPY frontend/package*.json ./

RUN npm install

COPY . .

CMD ["npm", "start"]
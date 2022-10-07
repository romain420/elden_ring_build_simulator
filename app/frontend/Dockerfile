FROM node:12 AS build

WORKDIR /app

EXPOSE 5000:80
COPY package.json ./
RUN npm install
COPY . ./
RUN npm build

FROM nginx:1.19-alpine
COPY --from=build /app /usr/share/nginx/html
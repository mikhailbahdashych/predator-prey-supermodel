FROM node:11.13.0-alpine

RUN mkdir -p /usr/src/nuxt-app
WORKDIR /usr/src/nuxt-app

RUN apk update && apk upgrade
RUN apk add git

COPY . /usr/src/nuxt-app
RUN npm run build

EXPOSE 5000

ENV NUXT_HOST=127.0.0.1
ENV NUXT_PORT=5000

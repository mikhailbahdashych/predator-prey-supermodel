FROM node

ENV ENV_HOST=0.0.0.0

WORKDIR /pnbfront

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 8010

CMD [ "npm", "start" ]

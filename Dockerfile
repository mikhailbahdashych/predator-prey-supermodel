FROM node

WORKDIR /pnbfront

COPY package.json ./

RUN npm install

COPY . .

RUN npm run build

ENV ENV_HOST=0.0.0.0

EXPOSE 8010

CMD [ "npm", "start" ]

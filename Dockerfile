FROM node

WORKDIR /pnbfront

COPY . .

RUN npm install

EXPOSE 8010

CMD [ "npm", "start" ]

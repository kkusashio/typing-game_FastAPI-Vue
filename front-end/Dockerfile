FROM node:14.17.1
WORKDIR /src
RUN yarn global add @vue/cli
COPY package.json yarn.lock ./
RUN yarn install
CMD ["yarn", "serve"]
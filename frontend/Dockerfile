# используем официальный образ Node.js
FROM node:lts-alpine as build-frontend

# устанавливаем приложение Quasar CLI глобально
RUN npm install -g @quasar/cli

# создаем директорию приложения и устанавливаем ее в качестве рабочей
WORKDIR /app

# копируем файлы package.json и package-lock.json
COPY package*.json ./

# устанавливаем зависимости
RUN npm install

# копируем все файлы приложения в контейнер
COPY . .


# собираем приложение Quasar
RUN quasar build

# указываем порт, на котором будет работать приложение
EXPOSE 8080
#EXPOSE 8443

WORKDIR /app/dist/spa


# запускаем приложение
#CMD [ "quasar", "serve", "--history" , "--https", "--hostname", "dreammanor.ru", "--cert", "./certificate.crt", "--key", "./private.key"]
#CMD [ "quasar", "serve", "--history" , "--port", "80"]

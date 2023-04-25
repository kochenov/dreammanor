### Команды 

```lang=bash
# Переход в корень сервера
cd ..

# переход в рабочую директорию
cd dreammanor

# обновить до текущей версии с GitHub
git pull

# запустить докер компос в фоне
docker-compose up -d --build

# показать все процессы
docker-compose ps -a

# показать все образы
docker-compose images

```

### Логи

```
# Вывести логи для всех контейнеров
docker-compose logs

# Вывести логи только для контейнера с именем "db"
docker-compose logs db

# Вывести логи в режиме реального времени с временными метками
docker-compose logs -f -t
```


## Рабочая версия для ngnix
***


```
worker_processes 1;

events {
    worker_connections 1024;
}

http {
    upstream backend {
        server backend:8000;
    }

    server {
        listen 80;
        server_name dreammanor.ru;
        return 301 https://$server_name$request_uri;
    }

    server {
        listen 443 ssl http2;
        server_name dreammanor.ru;

        ssl_certificate /etc/letsencrypt/live/dreammanor.ru/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/dreammanor.ru/privkey.pem;

        location / {
            proxy_pass https://dreammanor.ru:8080;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }

    server {
        listen 80;
        server_name api.dreammanor.ru;
        return 301 https://$server_name$request_uri;
    }

    server {
        listen 443 ssl http2;
        server_name api.dreammanor.ru;

        ssl_certificate /etc/letsencrypt/live/api.dreammanor.ru/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/api.dreammanor.ru/privkey.pem;

        location / {
            proxy_pass https://api.dreammanor.ru:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}

```


##  Настройка рабочая (резерв) docker-compose.yml

***

```
version: "3.9"
services:
  db:
    image: postgres:15
    container_name: db_app
    command: -p 5432
    volumes:
      - ./database/postgres:/var/lib/postgresql/data
    expose:
      - 5432
    env_file:
      - ./backend/.env-non-dev

  redis:
    image: redis:7
    container_name: redis_app
    command: --port 6379
    expose:
      - 6379

  backend:
    build:
      context: ./backend
    env_file:
      - ./backend/.env-non-dev
    environment:
      - DOMAIN=api.dreammanor.ru
      - FASTAPI_ENVIRONMENT=production
      - FASTAPI_HTTPS_REDIRECT=true
      - FASTAPI_SSL_CERT_FILE=/etc/letsencrypt/live/api.dreammanor.ru/fullchain.pem
      - FASTAPI_SSL_KEY_FILE=/etc/letsencrypt/live/api.dreammanor.ru/privkey.pem
    container_name: fastapi_app
    command: ["/fastapi_app/docker/app.sh"]
    ports:
      - 8000:8000
    volumes:
      - /etc/letsencrypt/:/etc/letsencrypt/
    depends_on:
      - db
      - redis

  celery:
    build:
      context: ./backend
    env_file:
      - ./backend/.env-non-dev
    container_name: celery_app
    command: ["/fastapi_app/docker/celery.sh", "celery"]
    depends_on:
      - redis
  flower:
    build:
      context: ./backend
    env_file:
      - ./backend/.env-non-dev
    container_name: flower_app
    command: ["/fastapi_app/docker/celery.sh", "flower"]
    depends_on:
      - redis
      - celery
    ports:
      - 8888:5555
  frontend:
    build:
      context: ./frontend
    container_name: frontend_quasar
    ports:
      - 8080:8080
    depends_on:
      - backend
    environment:
      - NODE_ENV=production
      - API_URL=https://api.dreammanor.ru
    volumes:
      - frontend:/app/dist/spa
      - /etc/letsencrypt/:/etc/letsencrypt/
    command: "quasar serve --host 0.0.0.0  --https --port 8080 --history --cert /etc/letsencrypt/live/dreammanor.ru/cert.pem --key /etc/letsencrypt/live/dreammanor.ru/privkey.pem"
  nginx:
    image: nginx:alpine
    container_name: nginx_app
    ports:
      - 80:80
      - 443:443
    volumes:
      - /etc/letsencrypt/:/etc/letsencrypt/
      - ./frontend/nginx.conf:/etc/nginx/nginx.conf
      - frontend:/app/dist/spa
    depends_on:
      - frontend
      - backend
    #command: "nginx -g 'daemon off;'"
volumes:
  frontend:
```
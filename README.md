## Тестовое задание

___
### Описание
REST-API приложение на Python сделаное в рамках тестового задания.

- Проект доступен по [адресу](https://plate.boostnet.ru/auth/users/)


### Технологии
- [Python]
- [Django]
- [Django REST Framework]
- [Docker]
- [Gunicorn]
- [PostgreSQL]
___

### Примеры работы с API для неавторизованных пользователей

Для неавторизованных пользователей работа с API ограничена, доступна только регистрация аккаунта.

  

Регистрация пользователей:

```bash

POST https://plate.boostnet.ru/auth/users/

```

В теле запроса отправляем:

```json

{
    "username": "string",
    "password": "string"
}

```

Пример ответа:

```json

{
    "email": "",
    "username": "string",
    "id": "f19f56bf-79ab-46cb-a8a3-50edf4e65ca4"
}

```

### JWT-токен:

Получить JWT-токен

```bash

POST https://plate.boostnet.ru/jwt/create/

```

Передав в body данные пользователя:

```json

{

"username": "string",

"password": "string"

}

```


Обновить JWT-токен:

```bash

POST https://plate.boostnet.ru/jwt/refresh/

```

В теле запроса:

```json

{

"refresh": "string"

}

```

Проверить JWT-токен:

```bash

POST https://plate.boostnet.ru/jwt/verify/

```

В теле запроса:
```json
{

"access": "string"

}
```  

### Примеры работы с API для авторизованных пользователей
Получение учетных данных пример с помощью curl:
```bash

curl -LX GET https://plate.boostnet.ru/auth/users/me/ -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjczODcxODI4LCJqdGkiOiIyYmI5M2UwZjY3ZTA0ZmQ4OTkyMjBiZjIyMDY1ODJjOSIsInVzZXJfaWQiOjF9.JG-ow3toDAMBSfPM8x2Wb7d6E0tgPP_BrSLUh02ngy0'

```

Генерация государственных номеров автомобилей:

```bash

GET https://plate.boostnet.ru/api/plate/generate

```

В теле запроса:

```json
{
    "generated_plate": [
        "X701CC"
    ]
}

```

```bash

GET https://plate.boostnet.ru/api/plate/generate/5

```

Пример ответа:

```json

{
    "generated_plate": [
        "P788KP",
        "P946OH",
        "K319HC",
        "C375CH",
        "M868AH"
    ]
}

```

Добавление государственных номеров автомобилей в базу данных:

```bash

POST https://plate.boostnet.ru/api/plate/add

```
В теле запроса:
```json
{
    "plate": "Y684YY"
}
```  


Пример ответа:

```json

{
    "id": "da9ef3e2-d82d-412d-a14b-9f2167a2c26d",
    "plate": "Y684YY"
}

```

Получение государственных номеров автомобилей:

```bash

GET https://plate.boostnet.ru/api/plate/get/da9ef3e2-d82d-412d-a14b-9f2167a2c26d

```

Пример ответа:

```json

{
    "id": "da9ef3e2-d82d-412d-a14b-9f2167a2c26d",
    "plate": "Y684YY"
}

```

### Запуск проекта в dev-режиме

- Клонировать репозиторий.

```bash

git clone git@github.com:Tozix/api_final_yatube.git

```

- Установить и активировать виртуальное окружение c учетом версии Python 3.7

```bash

python3.10 -m venv venv

venv/bin/activate

python -m pip install --upgrade pip

```

- Для переключения на SQL нужно отредактировать "блок" DATABASES в settings.py проекта.

```bash

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```

- Установить зависимости

```bash

pip install -r requirements.txt

```

- Выполнить миграции:

```bash

python manage.py migrate

```

Создать суперпользователя:

```bash

python manage.py createsuperuser

```

Запуск проекта:

```bash

python manage.py runserver

```

___


## Шаблон наполнения .env
```
# секретный ключ Django проекта
SECRET_KEY='asdasdasdsW45RF324ADSTAST4ADFS'     
# Дебаг режим
DEBUG=True
# Список разршенных хостов через запятую
ALLOWED_HOSTS='*,localhost' 
DB_ENGINE='django.db.backends.postgresql'
DB_NAME='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='postgres'
DB_HOST='db'
# 5432 (порт по умолчанию)
DB_PORT=5432                 
```

## Автоматизация развертывания серверного ПО
Для автоматизации развертывания ПО на боевых серверах используется среда виртуализации Docker, а также Docker-compose - инструмент для запуска многоконтейнерных приложений. Docker позволяет «упаковать» приложение со всем его окружением и зависимостями в контейнер, который может быть перенесён на любую Linux -систему, а также предоставляет среду по управлению контейнерами. Таким образом, для разворачивания серверного ПО достаточно чтобы на сервере с ОС семейства Linux были установлены среда Docker и инструмент Docker-compose.

Ниже представлен docker-compose.yaml - файл с инструкцией по разворачиванию Docker-контейнера приложения:

```Dockerfile
version: '3.8'

services:
  db:
    image: postgres:14.0-alpine
    volumes:
      - db_data:/var/lib/postgresql/data/
    env_file:
      - ./.env
    restart: always

  web:
    build: ../car_numbers
    restart: always
    volumes:
      - static_value:/app/static/
      - media_value:/app/media/
    env_file:
      - ./.env
    depends_on:
      - db

  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - static_value:/var/html/static/
      - media_value:/var/html/media/
    restart: always
    depends_on:
      - web

volumes:
  static_value:
  media_value:
  db_data:
```



## Описание команд для запуска приложения в контейнерах
Для запуска проекта в контейнерах используем **docker-compose** : ```docker-compose up -d --build```, находясь в директории (infra) с ```docker-compose.yaml```

После сборки контейнеров выполяем:
```bash
# Выполняем миграции
sudo docker-compose exec web python manage.py migrate
# Создаем суперппользователя
docker-compose exec web python manage.py createsuperuser
# Собираем статику со всего проекта
docker-compose exec web python manage.py collectstatic --no-input
```
Пример настройки хоста для nginx
```
server {
    listen 80;
    listen [::]:80;
    server_name plate.boostnet.ru;
    server_tokens off;
    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }
    if ($host = plate.boostnet.ru) {
        return 301 https://$host$request_uri;
    }
}
server {
    server_tokens off;
    listen 443 default_server ssl http2;
    listen [::]:443 ssl http2;
    server_name plate.boostnet.ru;
    ssl_certificate /etc/nginx/ssl/live/foodgram.boostnet.ru/fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/live/foodgram.boostnet.ru/privkey.pem;
 
    location / {
        proxy_set_header Host $host;
        proxy_set_header        X-Forwarded-Host $host;
        proxy_set_header        X-Forwarded-Server $host;
        proxy_pass http://backend:8000;
    }
}
```


### Автор backend'а:
[Никита Емельянов]


[//]: # (Ниже находятся справочные ссылки)

   [Python]: <https://www.python.org/downloads/release/python-370/>
   [Django]: <https://www.djangoproject.com/download/>
   [Django REST Framework]: <https://www.django-rest-framework.org/community/release-notes/>
   [Docker]: <https://www.docker.com/>
   [Gunicorn]: <https://gunicorn.org/>
   [PostgreSQL]:<https://www.postgresql.org/>  
   [Никита Емельянов]: <https://github.com/Tozix>

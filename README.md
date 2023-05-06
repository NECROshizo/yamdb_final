# Проект Docker контейнера для проекта YaMDB
## Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=gray)](https://www.python.org/) [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=gray)](https://www.postgresql.org/) [![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=56C0C0&color=gray)](https://nginx.org/ru/) [![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=gray)](https://gunicorn.org/) [![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=gray)](https://www.docker.com/) [![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=56C0C0&color=gray)](https://www.docker.com/) [![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=56C0C0&color=gray)](https://www.docker.com/products/docker-hub)
## Статус CI/CD
![Workflow](https://github.com/NECROshizo/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание проекта
Проект Docker контейнера для проекта YaMDB. Подробно о проекте YAMDB и его локальной развертке [здесь](https://github.com/NECROshizo/infra_sp2/api_yamdb/README.md)

## Установка и настройки из контейнера Docker
#### Запуск сборки из файл docker-compose.yaml:

```
cd infra_sp2/infra
docker-compose up -d
```
**При необходимости пересборки контейнера:**
```
docker-compose up -d --build
```
#### Создание и применение миграции:
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```
#### Создание суперпользовотеля:
```
docker-compose exec web python manage.py createsuperuser
```
#### Сбор статистики:
```
docker-compose exec web python manage.py collectstatic --no-input
```
#### Импорт данных в базу данных::
```
docker-compose exec web python manage.py loaddata fixtures.json
```
#### Проект с рабочей базой
Проект можно посмотреть по адрессу [neoshi.sytes.net](https://neoshi.sytes.net/api/v1/)
#### Настройка параметров допуска оуружения к базе данных
```
touch .env
```
Шаблон файла **.env**
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<имя БД>
POSTGRES_USER=<Имя пользователя>
POSTGRES_PASSWORD=<пароль>
DB_HOST=<хост БД>
DB_PORT=<порт для допуска к БД>
```
## Автор
[**Оганин Пётр**](https://github.com/NECROshizo) 
2023 г.
# Проект YaMDb


## Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=gray)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=gray)](https://www.djangoproject.com/) [![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=gray)](https://www.django-rest-framework.org/)
## Линтеры
[![Flake8](https://img.shields.io/badge/-flake8-464646?style=flat&logo=flake8&logoColor=56C0C0&color=gray)](https://flake8.pycqa.org/)
##### Полный список модулей, используемых в проекте, доступен в [api_yamdb/requirements.txt](https://github.com/NECROshizo/api_yamdb/blob/36c25de83bbede5c160216861d38fee3cc540a06/requirements.txt)

## Описание проекта
Проект YaMDb собирает **отзывы** пользователей на **произведения**. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Произведения делятся на **категории**, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 

Добавлять произведения, категории и **жанры** может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — **рейтинг** (целое число). На одно произведение пользователь может оставить только один отзыв.

Пользователи могут оставлять **комментарии** к отзывам.

Добавлять отзывы, **комментарии** и ставить оценки могут только аутентифицированные пользователи.

## Установка и настройки
#### Создание виртуального окружения:

```
python -m venv venv
```

#### Запуск виртуального окружения:

```
source venv/Scripts/activate - команда для Windows
source venv/bin/activate - команда для Linux и macOS
```
#### Установка зависимостей:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### Применение миграций:
```
cd api_yamdb/
python manage.py migrate 
```
#### Запуск django сервера:

```
python manage.py runserver 
```

## Структура базы данных
<div align="center">
    <img src="https://raw.githubusercontent.com/NECROshizo/api_yamdb/master/api_yamdb/static/ER.png?token=GHSAT0AAAAAABY6TRND4P3VPFBUJPWMOKA6Y7D3UIQ" alt="Диаграмма">
</div>

## Заполнение базы данных из CSV:

Заполнение базы из тестовых подготовленных таблиц располагающихся [api_yamdb/api_yamdb)/static/data/](https://github.com/NECROshizo/api_yamdb/tree/master/api_yamdb/static/data)

```
python manage.py getdata
```
## Документация:
Полная документация к API доступна по http://\<localhost>/redoc/

## Примеры запросов к API:
*запросы к API начинаются с* `/api/v1/`
### Регистрация нового пользователя
```
POST auth/signup/
```

**Request**
```json
{
"email": "string",
"username": "string"
}
```
**Response**
```json
{
  "username": "string",
  "confirmation_code": "string"
}
```
### Получение списка всех произведений
```
GET /titles/
```
**Response**
```json
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "name": "string",
      "year": 0,
      "rating": 0,
      "description": "string",
      "genre": [
        {
          "name": "string",
          "slug": "string"
        }
      ],
      "category": {
        "name": "string",
        "slug": "string"
      }
    }
  ]
}
```
### Частичное обновление отзыва по id:
```
PATCH titles/{title_id}/reviews/{review_id}/
```
**Request**
```json
{
  "text": "string",
  "score": 1
}
**Response**
```json
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```

## Разработчики:
-  [**Денис Филиппов**](https://github.com/Sun-Mon-Fil) - в роли первого разработчика
-  [**Пётр Оганин**](https://github.com/NECROshizo) - в роли третьего разработчика(Тимлидер)
-  [**Мстислав Грацкий**](https://github.com/gratsky) - в роли второго разработчика
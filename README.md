# REST API для приложения «Посты», реализованное с использованием FastAPI и взаимодействующее с базой данных PostgreSQL через async SQLAlchemy.

## ⚒️ Технологический стек
```
fastapi, postgres, uvicorn, async sqlalchemy, pydantic, asyncpg, docker

```
## Запуск (указаны команды для Windows):
Для запуска проекта у вас должны быть установлены Docker и Docker Compose.
1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Enigmatica33/Posts.git
``` 

2. Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
```

3. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
4. Создать файл .env в корневой директории проекта (пример .env.example)
5. Сборка и запуск проекта:
```
docker compose up --build
```
После успешного запуска:

* API будет доступно по адресу: http://localhost:8000/api/v1/
* Документация Swagger UI: http://localhost:8000/docs
* Документация ReDoc: http://localhost:8000/redoc

## Набор доступных эндпоинтов для API POSTS

```/posts/```	Создание нового поста (POST)
```/posts/```	Получение списка всех постов (GET)
```/posts/{post_id}```	Получение одного поста по его id (GET)
```/posts/{post_id}```	Частичное обновление поста по его id (PATCH)
```/posts/{post_id}```	Удаление поста по его id (DELETE)

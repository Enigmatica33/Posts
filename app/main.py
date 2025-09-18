from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.routers.post_router import router
from database.session import async_engine
from database.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Приложение запускается, создаем таблицы...')
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print('Таблицы были успешно созданы (или уже существовали).')
    yield
    print('Приложение останавливается.')


app = FastAPI(
    title='REST API для приложения «Посты»',
    description='Реализовано на FastAPI с PostgreSQL.',
    version='1.0.0',
    lifespan=lifespan
)

app.include_router(router, prefix='/api/v1')


@app.get('/')
def read_root():
    return {
        'message':
        'Добро пожаловать в REST API приложения «Посты»! '
        'Перейдите на /docs для просмотра документации.'
    }

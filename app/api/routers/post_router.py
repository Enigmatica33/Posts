from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query

from sqlalchemy.ext.asyncio import AsyncSession
from crud import crud_post
from schemas.post import PostCreate, PostResponse, PostUpdate
from database.session import get_db

router = APIRouter()


@router.post(
        '/posts/',
        response_model=PostResponse,
        status_code=status.HTTP_201_CREATED
    )
async def create_new_post(
    *,
    db: AsyncSession = Depends(get_db),
    post_in: PostCreate,
):
    """Создать новый пост."""
    post = await crud_post.create_post(db=db, post_in=post_in)
    return post


@router.get('/posts/', response_model=List[PostResponse])
async def read_posts(
    db: AsyncSession = Depends(get_db),
    skip: int = Query(0, ge=0, description='Смещение (offset)'),
    limit: int = Query(10, ge=1, le=100, description='Количество (limit)'),
):
    """Получить список постов."""
    posts = await crud_post.get_posts_list(db, skip=skip, limit=limit)
    return posts


@router.get('/posts/{post_id}', response_model=PostResponse)
async def read_post_by_id(
    post_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Получить пост по его ID."""
    post = await crud_post.get_post(db=db, post_id=post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пост с таким ID не найден',
        )
    return post


@router.patch('/posts/{post_id}', response_model=PostResponse)
async def update_existing_post(
    *,
    db: AsyncSession = Depends(get_db),
    post_id: int,
    post_in: PostUpdate,
):
    """Обновить пост по ID."""
    post = await crud_post.get_post(db=db, post_id=post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пост с таким ID не найден',
        )
    updated_post = await crud_post.update_post(
        db=db,
        db_obj=post,
        obj_in=post_in
    )
    return updated_post


@router.delete('/posts/{post_id}', response_model=PostResponse)
async def delete_existing_post(
    *,
    db: AsyncSession = Depends(get_db),
    post_id: int,
):
    """Удалить пост по ID."""
    post = await crud_post.delete_post(db=db, post_id=post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пост с таким ID не найден',
        )
    return post

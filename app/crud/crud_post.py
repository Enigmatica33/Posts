from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional

from models.post import Post
from schemas.post import PostCreate, PostUpdate


async def create_post(db: AsyncSession, *, post_in: PostCreate) -> Post:
    """Создание нового поста."""
    db_obj = Post(title=post_in.title, content=post_in.content)
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def get_post(db: AsyncSession, post_id: int) -> Optional[Post]:
    """Получение поста по ID."""
    result = await db.execute(select(Post).filter(Post.id == post_id))
    return result.scalars().first()


async def get_posts_list(db: AsyncSession, *, skip: int = 0,
                         limit: int = 100) -> List[Post]:
    """Получение списка постов с пагинацией."""
    result = await db.execute(select(Post).offset(skip).limit(limit))
    return result.scalars().all()


async def update_post(db: AsyncSession,
                      *,
                      db_obj: Post,
                      obj_in: PostUpdate) -> Post:
    """Обновление поста (PATCH)."""
    update_data = obj_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def delete_post(db: AsyncSession, *, post_id: int) -> Optional[Post]:
    """Удаление поста."""
    db_obj = await get_post(db, post_id)
    if db_obj:
        await db.delete(db_obj)
        await db.commit()
    return db_obj

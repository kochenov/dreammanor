from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from starlette.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from database import get_async_session

from news.models import Post, Category
from news.schemas import PostCreate, ViewNews, PostCreateAd, NewCategory

router = APIRouter(
    prefix="/news",
    tags=["News"]
)


async def get_count(model, session, category_id=0) -> int:
    """
    Получает количество всех записей в базе, конкретной таблицы
    :param category_id:
    :param model: Model DataBase
    :param session: This Sessions
    :return: Int
    """
    if category_id == 0:
        rows = await session.execute(select(func.count()).select_from(model))
    else:
        rows = await session.execute(select(func.count()).filter(model.category_id == category_id).select_from(model))
    return rows.scalar()


@router.get("")
async def get_news(category: int = 0, limit: int = 1, offset: int = 0,
                   popular: int = 0,
                   session: AsyncSession = Depends(get_async_session)):
    try:
        if popular == 1:
            order = Post.count_views.desc()
        elif popular == 0:
            order = Post.created_ad.desc()
        if category == 0:
            query = select(Post).options(selectinload(Post.category)).order_by(order).offset(
                offset).limit(limit)
        else:
            query = select(Post).where(Post.category_id == category).options(selectinload(Post.category)).order_by(
                order).offset(
                offset).limit(limit)
        result = await session.execute(query)
        result = result.scalars().all()
        if len(result) < 1:
            return JSONResponse(status_code=404, content={"message": "Item not found"})

        return {
            "status": "success",
            "data": result,
            "details": {
                "count": await get_count(Post, session, category)
            },
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.get("/category/{category_id}/post/{post_id}")
async def get_news_post(category_id: int, post_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Post).where(Post.id == post_id, Post.category_id == category_id).options(
            selectinload(Post.category))
        result = await session.execute(query)
        result = result.scalars().first()
        if not result:
            return JSONResponse(status_code=404, content={"message": "Item not found"})

        return {
            "status": "success",
            "data": result,
            "details": {},
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.get("/categories")
async def get_list_categories(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Category)
        result = await session.execute(query)
        result = result.scalars().all()

        return {
            "status": "success",
            "data": result,
            "details": {
                "count": await get_count(Category, session)
            },
        }
    except IntegrityError as e:
        print(e)
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.get("/category-info/{category}")
async def get_one_category(category: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Category).where(Category.id == category)
        result = await session.execute(query)
        result = result.scalars().first()
        if not result:
            return JSONResponse(status_code=404, content={"message": "Item not found"})
        return {
            "status": "success",
            "data": result,
            "details": {
                # "count": await get_count(Category, session)
            },
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("/add")
async def add_link_to_ads(new_post: PostCreateAd, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Post).values(**new_post.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/add/new-category")
async def add_link_to_ads(new_category: NewCategory, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Category).values(**new_category.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

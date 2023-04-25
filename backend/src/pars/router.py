from typing import Dict, Union

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from database import get_async_session
from pars.models import Link, Status
from pars.schemas import LinkCreate, LinkUpdate, LinkView
from pars.tasks import start_parser

router = APIRouter(
    prefix="/pars",
    tags=["Парсер ссылок"]
)


@router.get("/links", summary="Список ссылок на объявления")
async def get_links_to_ads(limit: int = 1, offset: int = 0,
                           status_id: int = 10,
                           session: AsyncSession = Depends(get_async_session)):
    """
    Получить список ссылок на объявления с заданным статусом.

    Аргументы:
    - limit: int - максимальное количество ссылок, которые нужно получить (по умолчанию 1).
    - offset: int - смещение относительно начала списка (по умолчанию 0).
    - status_id: int - идентификатор статуса объявлений (по умолчанию 10).
    - session: AsyncSession - сессия базы данных.

    Возвращает:
    - dict - словарь с ключами "status", "data" и "details".
      Ключ "status" содержит строку "success" или "error", в зависимости от результата операции.
      Ключ "data" содержит список объектов Link, которые представляют ссылки на объявления.
      Ключ "details" содержит количество полученных ссылок в виде строки.
    """
    try:
        order = Link.id.desc()
        query = select(Link).where(Link.status_id == status_id).options(selectinload(Link.status)).order_by(
            order).offset(
            offset).limit(limit)
        result = await session.execute(query)
        links = result.scalars().all()
        return {
            "status": "success",
            "data": links,
            "details": str(len(links))
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.get("/links-status")
async def get_links_status_to_ads(session: AsyncSession = Depends(get_async_session)):
    """Список статусов ссылок"""
    try:
        query = select(Status)
        result = await session.execute(query)
        status = result.scalars().all()
        return {
            "status": "success",
            "data": status,
            "details": str(len(status))
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("/links/new")
async def add_link_to_ads(new_link: LinkCreate, session: AsyncSession = Depends(get_async_session)):
    """Записать новую ссылку"""
    stmt = insert(Link).values(**new_link.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/links/edit/{link_id}")
async def update_link_to_ads(link_id: int, edit_link: LinkUpdate, session: AsyncSession = Depends(get_async_session)):
    """Изменение ссылки"""
    stmt = update(Link).where(Link.id == link_id).values(**edit_link.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/link/find/{home_id}")
async def get_house(home_id: int, session: AsyncSession = Depends(get_async_session)):
    """Список объявлений"""
    try:
        query = select(Link).where(Link.id == home_id)

        result = await session.execute(query)
        link = result.scalars().first()
        return {
            "status": "success",
            "data": link,
            "message": ""
        }
    except Exception as e:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "message": f"Неприведенная ошибка: {e}"
        })


@router.post("/start", summary="Старт парсинга")
async def add_link_to_ads():
    """Начать парсинг"""
    start_parser.delay()
    # await run()
    return {"message": "Задача на запуск парсера добавлена в очередь."}

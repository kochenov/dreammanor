from typing import List, Dict, Union

import urllib.parse

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import insert, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from node.models import Node
from node.schemas import NodeBase, NodeRead, NodeResponseRead, NodeResponseUpdate

router = APIRouter(
    prefix="/node",
    tags=["Страницы сущностей"]
)


@router.post("/", response_model=Dict[str, Union[str, None]])
async def create_node_item(node_item: NodeBase, session: AsyncSession = Depends(get_async_session)):
    """ Добавляет новый пункт меню """
    stmt = insert(Node).values(**node_item.dict(exclude_unset=True))
    try:
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "message": "Страница сущности успешно добавлена"
        }
    except IntegrityError as e:
        print(e)
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "message": "Такая сущность уже есть: Измените адрес"
        })
    


@router.get("/{node_url:path}", response_model=NodeResponseRead)
async def get_node(node_url: str, session: AsyncSession = Depends(get_async_session)):
    """Список объявлений"""
    try:
        """ """
        #decoded_url = "/".join([urllib.parse.unquote(segment) for segment in node_url.split("/")])

        query = select(Node).filter(Node.url == node_url)
        result = await session.execute(query)
        node = result.scalars().first()
        if not node:
            raise HTTPException(status_code=404, detail={
                "status": "error",
                "data": None,
                "message": "Список регионов пуст. Добавь новый регион"
            })
        else:
            return {
                "status": "success",
                "data": node,
                "message": ""
            }
    except Exception as e:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "message": f"Неприведенная ошибка: {e}"
        })


@router.put("/{menu_item_id}", response_model=NodeResponseUpdate)
async def update_menu_item(node_item_id: int, node_item: NodeBase,
                           session: AsyncSession = Depends(get_async_session)):
    """ Обновляет пункт меню по ID """
    stmt = update(Node).where(Node.id == node_item_id).values(**node_item.dict(exclude_unset=True))
    try:
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": node_item,
            "message": "Пункт меню изменён"
        }
    except IntegrityError as e:
        print(e)
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "message": "Такой пункт меню уже есть: Измените имя"
        })


@router.delete("/{node_item_id}", response_model=NodeBase)
async def delete_node_item(node_item_id: int, session: AsyncSession = Depends(get_async_session)):
    """ Удаляет пункт меню """
    pass


@router.get("/", response_model=NodeResponseRead)
async def read_node_items(skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_async_session)):
    """ Выводит список пунктов меню """
    try:
        query = select(Node).offset(skip).limit(limit)
        result = await session.execute(query)
        node_items = result.scalars().all()

        if not node_items:
            raise HTTPException(status_code=404, detail={
                "status": "error",
                "data": None,
                "message": "В меню нет элементов. Добавь новый"
            })
        return {
            "status": "success",
            "data": node_items,
            "message": "Получен список сущностей"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "message": f"Ошибка при получении списка: {str(e)}"
        })

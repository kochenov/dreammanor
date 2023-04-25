from typing import List, Dict, Union

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import insert, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from menu.models import MenuItem
from menu.schemas import MenuItemBase, MenuItemRead, MenuItemResponseRead, MenuItemResponseUpdate

router = APIRouter(
    prefix="/menu",
    tags=["Меню"]
)


@router.post("/", response_model=Dict[str, Union[str, None]])
async def create_menu_item(menu_item: MenuItemBase, session: AsyncSession = Depends(get_async_session)):
    """ Добавляет новый пункт меню """
    stmt = insert(MenuItem).values(**menu_item.dict(exclude_unset=True))
    try:
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "message": "Пункт меню успешно добавлен"
        }
    except IntegrityError as e:
        print(e)
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "message": "Такой пункт меню уже есть: Измените имя"
        })


@router.get("/{menu_item_id}", response_model=MenuItemBase)
async def read_menu_item(menu_item_id: int, session: AsyncSession = Depends(get_async_session)):
    """ Выводит пункт меню по ID """
    pass


@router.put("/{menu_item_id}", response_model=MenuItemResponseUpdate)
async def update_menu_item(menu_item_id: int, menu_item: MenuItemBase,
                           session: AsyncSession = Depends(get_async_session)):
    """ Обновляет пункт меню по ID """
    stmt = update(MenuItem).where(MenuItem.id == menu_item_id).values(**menu_item.dict(exclude_unset=True))
    try:
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": menu_item,
            "message": "Пункт меню изменён"
        }
    except IntegrityError as e:
        print(e)
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "message": "Такой пункт меню уже есть: Измените имя"
        })


@router.delete("/{menu_item_id}", response_model=MenuItemBase)
async def delete_menu_item(menu_item_id: int, session: AsyncSession = Depends(get_async_session)):
    """ Удаляет пункт меню """
    pass


@router.get("/", response_model=MenuItemResponseRead)
async def read_menu_items(skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_async_session)):
    """ Выводит список пунктов меню """
    try:
        query = select(MenuItem).offset(skip).limit(limit)
        result = await session.execute(query)
        menu_items = result.scalars().all()

        if not menu_items:
            raise HTTPException(status_code=404, detail={
                "status": "error",
                "data": None,
                "message": "В меню нет элементов. Добавь новый"
            })
        return {
            "status": "success",
            "data": menu_items,
            "message": "Получен список пунктов меню"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "message": f"Ошибка при получении списка пунктов меню: {str(e)}"
        })

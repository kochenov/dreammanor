import shutil
import time
import os
from typing import List, Dict, Union

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File

from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, NoResultFound

from auth.base_config import current_user
from auth.schemas import UserRead
from database import get_async_session

from realty.models import Home, Region, Districts, Settlements, SettlementType
from realty.schemas import Image, RegionCreate, RegionRead, RegionBase, AddOkey, DistrictRead, \
    DistrictCreate, SettlementRead, SettlementCreate, SettlemenTypeCreate, SettlemenTypeRead, HomeRead, HomeCreate, \
    HomeList, SettlementListRead
from fastapi_cache.decorator import cache
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/realty",
    tags=["Realty"]
)


@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(20)
    return "Много много данных, которые вычислялись сто лет"


@router.post("/upload-images/")
async def upload_images(images: List[UploadFile] = File(...)):
    uploaded_images = []
    for image in images:
        image_name = f"{time.time()}_{image.filename}"
        file_location = f"../files/images/{image_name}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
            os.chmod(file_location, 0o644)
        uploaded_images.append(Image(name=image.filename, url=f"/files/images/{image_name}"))
    return uploaded_images


# @app.post("/upload-images/")
# async def upload_images(images: List[UploadFile] = File(...)):
#     uploaded_images = []
#     for image in images:
#         file_location = f"images/{image.filename}"
#         with open(file_location, "wb") as buffer:
#             shutil.copyfileobj(image.file, buffer)
#         uploaded_images.append({"name": image.filename, "url": file_location})
#     return {"uploaded_images": uploaded_images}


# @router.post("/upload")
# async def create_upload_file(file: UploadFile = File(...)):
#     contents = await file.read()
#     with open(f"images/{file.filename}", "wb") as f:
#         f.write(contents)
#     return {"filename": file.filename}


@router.get("/houses", response_model=HomeList)
async def get_house_list(limit: int = 1, offset: int = 0,
                         status: bool = True,
                         session: AsyncSession = Depends(get_async_session)):
    """Список объявлений"""
    try:
        order = Home.id.desc()
        # .join(Region) \
        # .join(Districts) \
        # .join(Settlements) \
        query = select(Home) \
            .options(joinedload(Home.region), joinedload(Home.district),
                     joinedload(Home.settlement).joinedload(Settlements.settlement_type)) \
            .where(Home.status == status) \
            .order_by(order) \
            .offset(offset) \
            .limit(limit)
        result = await session.execute(query)
        homes = result.scalars().all()

        if not homes:
            raise HTTPException(status_code=500, detail={"status": "info", "data": None,
                                                         "message": "Объявлений о продаже домов пока ещё нет"})
        return {"status": "success", "data": homes, "message": ""}

    except SQLAlchemyError as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail={"status": "error", "data": None, "message": "Ошибка сервера"})


# Regions
@router.post("/regions/", response_model=AddOkey)
async def create_region(region: RegionCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Region).values(**region.dict(exclude_unset=True))
    try:
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "message": "Новый регион успешно добавлен"
        }
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "message": "Регион с таким именем уже существует"
        })


@router.get("/regions/", response_model=Dict[str, Union[str, List[RegionRead]]])
async def read_regions(skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_async_session)):
    query = select(Region).offset(skip).limit(limit)
    # regions = session.query(Region).offset(skip)
    result = await session.execute(query)
    regions = result.scalars().all()
    if not regions:
        raise HTTPException(status_code=404, detail={
            "status": "error",
            "data": None,
            "message": "Список регионов пуст. Добавь новый регион"
        })
    return {
        "status": "success",
        "data": regions,
        "message": "Получен список регионов"
    }


@router.get("/districts/{region_id}", response_model=Dict[str, Union[str, List[DistrictRead]]])
async def read_districts(region_id: int, skip: int = 0, limit: int = 100,
                         session: AsyncSession = Depends(get_async_session)):
    query = select(Districts).where(Districts.region_id == region_id).offset(skip).limit(limit)
    # regions = session.query(Region).offset(skip)
    result = await session.execute(query)
    districts = result.scalars().all()

    if not districts:
        raise HTTPException(status_code=404, detail={
            "status": "error",
            "data": None,
            "message": "Нет записей! Добавьте новый район"
        })
    return {
        "status": "success",
        "data": districts,
        "message": "Получен список районов"
    }


@router.post("/district/", response_model=AddOkey)
async def create_region(region: DistrictCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Districts).values(**region.dict(exclude_unset=True))
    try:
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "message": "Новый район успешно добавлен"
        }
    except IntegrityError as e:
        print(e)
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "message": "Район с таким именем уже существует"
        })


@router.get("/settlements/{region_id}/{district_id}/{settlement_type_id}",
            response_model=Dict[str, Union[str, List[SettlementListRead]]])
async def read_settlements(region_id: int, district_id: int, settlement_type_id: int, skip: int = 0, limit: int = 100,
                           session: AsyncSession = Depends(get_async_session)):
    query = select(Settlements).filter(Settlements.region_id == region_id, Settlements.district_id == district_id,
                                       Settlements.settlement_types_id == settlement_type_id).offset(skip).limit(limit)
    result = await session.execute(query)
    settlements = result.scalars().all()

    if not settlements:
        raise HTTPException(status_code=404, detail={
            "status": "error",
            "data": None,
            "message": "Нет записей! Добавьте новое поселение"
        })
    return {
        "status": "success",
        "data": settlements,
        "message": "Получен список поселений"
    }


@router.post("/settlement/", response_model=AddOkey)
async def create_settlement(settlement: SettlementCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Settlements).values(**settlement.dict(exclude_unset=True))
    try:
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "message": "Новое поселение успешно добавлено"
        }
    except IntegrityError as e:
        print(e)
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "message": "Поселение с таким именем уже существует"
        })


@router.post("/settlement-type/", response_model=AddOkey)
async def create_settlement_type(settlement_type: SettlemenTypeCreate,
                                 session: AsyncSession = Depends(get_async_session)):
    stmt = insert(SettlementType).values(**settlement_type.dict(exclude_unset=True))
    try:
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "message": "Новый тип успешно добавлен"
        }
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "message": "Тип поселения с таким именем уже существует"
        })


@router.get("/settlement-type/", response_model=Dict[str, Union[str, List[SettlemenTypeRead]]])
async def read_settlement_types(skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_async_session)):
    query = select(SettlementType).offset(skip).limit(limit)
    # regions = session.query(Region).offset(skip)
    result = await session.execute(query)
    settlement_types = result.scalars().all()
    if not settlement_types:
        raise HTTPException(status_code=404, detail={
            "status": "error",
            "data": None,
            "message": "Список типов поселений пуст. Добавь новый тип поселения"
        })
    return {
        "status": "success",
        "data": settlement_types,
        "message": "Получен список регионов"
    }


@router.post("/home/", response_model=AddOkey)
async def create_home(home: HomeCreate, user: UserRead = Depends(current_user),
                      session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Home).values(**home.dict(exclude_unset=True), user_id=user.id)
    try:
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "message": "Объявление успешно добавлено"
        }
    except IntegrityError as e:
        print(e)
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "message": "Такое объявление уже есть:Измените заголовок"
        })


@router.get("/house/{home_id}", response_model=Dict[str, Union[str, HomeRead]])
async def get_house(home_id: int, session: AsyncSession = Depends(get_async_session)):
    """Список объявлений"""
    try:
        """ """

        query = select(Home).where(Home.id == home_id).options(selectinload(Home.region),
                                                               selectinload(Home.district),
                                                               selectinload(Home.settlement).options(
                                                                   selectinload(Settlements.settlement_type)
                                                               )
                                                               )

        result = await session.execute(query)
        links = result.scalars().first()
        return {
            "status": "success",
            "data": links,
            "message": ""
        }
    except Exception as e:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "message": f"Неприведенная ошибка: {e}"
        })


@router.get("/find-house/{uid}", response_model=Dict[str, Union[str, HomeRead]])
async def get_find_house_uid(uid: int, session: AsyncSession = Depends(get_async_session)):
    """Список объявлений"""
    try:
        query = select(Home).where(Home.uid == uid).options(selectinload(Home.region),
                                                            selectinload(Home.district),
                                                            selectinload(Home.settlement).options(
                                                                selectinload(Settlements.settlement_type)
                                                            )
                                                            )

        result = await session.execute(query)
        link = result.scalars().one_or_none()

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

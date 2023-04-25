from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class Image(BaseModel):
    name: str
    url: str


class RegionBase(BaseModel):
    label: str


class RegionCreate(RegionBase):
    pass


class RegionUpdate(RegionBase):
    pass


class AddOkey(BaseModel):
    status: str
    data: Optional[str] = None
    message: str


class RegionRead(RegionBase):
    id: int

    class Config:
        orm_mode = True


class SettlemenTypeBase(BaseModel):
    label: str
    label_i: str


class SettlemenTypeCreate(SettlemenTypeBase):
    pass


class SettlemenTypeUpdate(SettlemenTypeBase):
    pass


class SettlemenTypeRead(SettlemenTypeBase):
    id: int

    class Config:
        orm_mode = True


class DistrictBase(BaseModel):
    label: str
    region_id: int


class DistrictCreate(DistrictBase):
    pass


class DistrictUpdate(DistrictBase):
    pass


class DistrictRead(DistrictBase):
    id: int

    class Config:
        orm_mode = True


class SettlementBase(BaseModel):
    label: str
    label_i: str
    region_id: int
    district_id: int
    settlement_types_id: int


class SettlementCreate(SettlementBase):
    pass


class SettlementUpdate(SettlementBase):
    pass


class SettlementListRead(SettlementBase):
    id: int

    class Config:
        orm_mode = True


class SettlementRead(SettlementBase):
    id: int
    settlement_type: Optional[SettlemenTypeRead] = None

    class Config:
        orm_mode = True


class HomeBase(BaseModel):
    uid: int
    title: str
    description: str
    meta_description: str
    meta_title: str
    status: bool
    region_id: int
    district_id: int
    settlement_id: int
    full_adress: str
    main_image: str
    video_zen: str = None
    video_rutube: str = None
    link_to_ads: str
    price: int
    area_of_house: int
    plot_area: int
    bathroom_in_house: bool
    gaz: bool
    #
    number_of_rooms: int = None  # Количество комнат
    number_of_floors: int = None  # количество этажей
    sauna: Optional[bool]  # наличие бани
    plastic_windows: Optional[bool]  # наличие пластиковых окон
    bus_stop: Optional[bool]  # наличие автобусной остановки
    rail_station: Optional[bool]  # наличие железнодорожной станции
    distance_to_the_river: int = None  # Расстояние до реки
    distance_to_the_lake: int = None  # Расстояние до озера
    there_is_a_forest_nearby: Optional[bool]  # наличие рядом леса
    distance_to_the_city: int = None  # Расстояние до города
    gas_heating: Optional[bool]  # наличие газового отопления
    furnace_heating: Optional[bool]  # наличие печного отопления
    sewerage: Optional[bool]  # канализация
    year_of_construction: int = None  # Год постройки
    wall_material_id: int = None  # Материал стен
    #  wall_material = relationship("WallMaterial")
    alarm_status: Optional[bool]  # аварийное состояние


class HomeCreate(HomeBase):
    pass


class HomeUpdate(HomeBase):
    pass


class HomeRead(HomeBase):
    id: int
    created_ad: Optional[datetime]
    updated_ad: Optional[datetime]
    user_id: int
    views_count: Optional[int] = None
    region: RegionRead
    district: DistrictRead
    settlement: SettlementRead

    class Config:
        orm_mode = True


class HomeList(BaseModel):
    status: str
    data: Optional[List[HomeRead]] = None
    message: str


class HomeInResponse(BaseModel):
    count: int
    items: List[HomeRead]

    class Config:
        orm_mode = True

from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from database import Base, metadata


class Region(Base):
    __tablename__ = "regions"
    id = Column(Integer, primary_key=True)
    label = Column(String(255), nullable=False, unique=True)

    class Config:
        orm_mode = True


class Districts(Base):
    __tablename__ = "districts"
    id = Column(Integer, primary_key=True)
    label = Column(String(255), nullable=False, unique=True)
    region_id = Column(Integer, ForeignKey("regions.id"), nullable=False)  # Область

    class Config:
        orm_mode = True


class SettlementType(Base):
    __tablename__ = "settlement_types"
    id = Column(Integer, primary_key=True)
    label = Column(String(255), nullable=False, unique=True)
    label_i = Column(String(255), nullable=False, unique=True)  # (где) в городе


class Settlements(Base):
    __tablename__ = "settlements"
    id = Column(Integer, primary_key=True)
    label = Column(String(255), nullable=False)
    label_i = Column(String(255), nullable=False)
    region_id = Column(Integer, ForeignKey("regions.id"))  # Область
    district_id = Column(Integer, ForeignKey("districts.id"))  # Район
    settlement_types_id = Column(Integer, ForeignKey("settlement_types.id"))
    settlement_type = relationship("SettlementType")

    class Config:
        orm_mode = True


class Home(Base):
    __tablename__ = "overview_of_houses"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, unique=True)
    description = Column(String(15000), nullable=False)
    status = Column(Boolean, nullable=False)
    region_id = Column(Integer, ForeignKey("regions.id"))  # Область
    district_id = Column(Integer, ForeignKey("districts.id"))  # Районы
    settlement_id = Column(Integer, ForeignKey("settlements.id"))  # Поселения
    full_adress = Column(String(500), nullable=False)
    main_image = Column(String(1000), nullable=False)
    video_zen = Column(String(1000), nullable=True)
    video_rutube = Column(String(1000), nullable=True)
    link_to_ads = Column(String(1000), nullable=False)
    price = Column(Integer, nullable=False)
    area_of_house = Column(Integer, nullable=False)  # площадь дома
    plot_area = Column(Integer, nullable=False)  # площадь участка
    bathroom_in_house = Column(Boolean, nullable=False)  # Туалет в доме
    gaz = Column(Boolean, nullable=False, default=False)  # Есть газ
    created_ad = Column(DateTime, default=datetime.utcnow)
    updated_ad = Column(DateTime, nullable=True)
    region = relationship("Region")
    district = relationship("Districts")
    settlement = relationship('Settlements')
    user_id = Column(Integer, nullable=False)
    views_count = Column(Integer, default=0)
    uid = Column(Integer, unique=True)
    meta_title = Column(String(255), unique=True)
    meta_description = Column(String(500))
    #
    number_of_rooms = Column(Integer, nullable=True)  # Количество комнат
    number_of_floors = Column(Integer, default=1)  # количество этажей
    sauna = Column(Boolean, nullable=False, default=False)  # наличие бани
    plastic_windows = Column(Boolean, nullable=False, default=False)  # наличие пластиковых окон
    bus_stop = Column(Boolean, nullable=False, default=False)  # наличие автобусной остановки
    rail_station = Column(Boolean, nullable=False, default=False)  # наличие железнодорожной станции
    distance_to_the_river = Column(Integer, nullable=True)  # Расстояние до реки
    distance_to_the_lake = Column(Integer, nullable=True)  # Расстояние до озера
    there_is_a_forest_nearby = Column(Boolean, nullable=False, default=False)  # наличие рядом леса
    distance_to_the_city = Column(Integer, nullable=True)  # Расстояние до города
    gas_heating = Column(Boolean, nullable=False, default=False)  # наличие газового отопления
    furnace_heating = Column(Boolean, nullable=False, default=False)  # наличие печного отопления
    sewerage = Column(Boolean, nullable=False, default=False)  # канализация
    year_of_construction = Column(Integer, nullable=True)  # Год постройки
    wall_material_id = Column(Integer, nullable=True)  # Материал стен
    #  wall_material = relationship("WallMaterial")
    alarm_status = Column(Boolean, nullable=False, default=False)  # аварийное состояние

    class Config:
        orm_mode = True

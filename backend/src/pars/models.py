from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from database import Base, metadata


class Status(Base):
    """Таблица в которой хранятся данный статусов ссылок на объявления"""
    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    label = Column(String(255), nullable=False)

    class Config:
        orm_mode = True


class Link(Base):
    """Таблица url объявлений с видео обзорами"""
    __tablename__ = "link"
    id = Column(Integer, primary_key=True)
    link = Column(String(500), unique=True)
    price = Column(Integer, nullable=True, default=None)
    status_id = Column(Integer, ForeignKey("status.id"), default=10)
    comment = Column(String(500), nullable=True)
    created_ad = Column(TIMESTAMP, default=datetime.utcnow)
    status = relationship("Status")

    class Config:
        orm_mode = True


class ParsConfig(Base):
    __tablename__ = "pars_config"
    id = Column(Integer, primary_key=True)
    number_pars = Column(Integer)
    created_ad = Column(TIMESTAMP, default=datetime.utcnow)

    class Config:
        orm_mode = True

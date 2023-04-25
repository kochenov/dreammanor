from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

from database import Base, metadata


class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True)
    # имя пункта меню
    name = Column(String(255), nullable=False)
    # ссылка на сущность
    url = Column(String(255), nullable=False)
    # 1 - super user; 2- admin; 3-user; 0 гость
    role_id = Column(Integer, nullable=True, default=0)
    # id родителя
    parent_id = Column(Integer, nullable=True, default=0)
    # publish status
    status = Column(Boolean, default=0)
    # порядок вывода (приоритет)
    priority = Column(Integer, nullable=True, default=0)

    class Config:
        orm_mode = True

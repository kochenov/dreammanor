from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

from database import Base, metadata

# category = Table(
#     "categories",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(255), nullable=False),
# )
#
# post = Table(
#     "news",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("title", String(255), nullable=False, unique=True),
#     Column("category_id", Integer, ForeignKey("categories.id")),
#     Column("short_description", String(500), nullable=True),
#     Column("content", String(15000), nullable=False),
#     Column("created_ad", TIMESTAMP, default=datetime.utcnow, nullable=False),
#     Column("count_views", Integer, default=0)
#
# )
#

# class Post(Base):
#     id = Column(...)
#     category_id = Column(ForeignKey...)  # делаем связь с таблицей категорий
#
#     category = relationship("Category")  # здесь Category - это название класса/модели для таблицы с категориями
#
# # при асинхронной работе нужно юзать options:
# query = select(Post).options(selectinload(Post.category))
# result = await session.execute(query)
# result = result.all()
# for post in result:
#     print(post[0].category.__dict__)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    class Config:
        orm_mode = True


class Post(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, unique=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    short_description = Column(String(500), nullable=False)
    content = Column(String(15000), nullable=False)
    created_ad = Column(TIMESTAMP, default=datetime.utcnow)
    count_views = Column(Integer, default=0)
    category = relationship("Category")

    class Config:
        orm_mode = True



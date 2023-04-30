from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

from database import Base, metadata


class Node(Base):
    """
    - `id` - уникальный номер ноды
    - `url` - адрес
    - `module` - название модуля
    - `page` - название шаблона страницы
    - `component` - название текущего компонента
    - `slug` - id, alias, short_name
    - `title` - Заголовок Node
    - `sub_title` - Второй заголовок
    - `description`- мета описание страницы
    - `keywords` - мета ключевые слова
    - `robots` - доступ к индексации
    - `canonical_full_url` - полный адрес к страницы для ПСЯ
    - `user_role_id` - null - публичный, если есть id (Только для этой роли)
    - `user_auth` - false для всех, true - только для авторизированных
    - `name_menu` - короткое название для меню
    - `icon` - иконка, которая отображает смысл содержимого (для меню)
    """
    __tablename__ = "nodes"
    id = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False) 
    module = Column(String(255), nullable=False)
    component = Column(String(255), nullable=True)
    page = Column(String(255), nullable=True)
    slug = Column(Boolean, default=False)
    title = Column(String(255), nullable=False)
    sub_title = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    keywords = Column(String(255), nullable=True)
    canonical_full_url = Column(String(255), nullable=False)
    user_role_id = Column(Integer, nullable=True)
    user_auth = Column(Boolean, default=False)
    robots = Column(Boolean, default=True)
    name_menu = Column(String(255), nullable=True)
    icon = Column(String(255), nullable=True)
    

    class Config:
        orm_mode = True

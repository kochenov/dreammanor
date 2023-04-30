import os

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import xml.etree.ElementTree as ET

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from typing import Optional, List
from pydantic import BaseModel, Field

from redis import asyncio as aioredis
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate, UserUpdate
from news.router import router as router_news
from realty.router import router as router_realty
from pars.router import router as router_pars
from menu.router import router as router_menu
from node.router import router as router_node

env = os.getenv("APP_ENV", "production")

app = FastAPI(title='DreamManor API', version='0.0.1', openapi_url='/dreammanor.ru')

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

origins = [
    "http://127.0.0.1:9000",
    "https://dreammanor.ru",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)
app.mount("/files", StaticFiles(directory="../files"), name="files")

app.include_router(router_pars)
app.include_router(router_realty)
app.include_router(router_news)
app.include_router(router_menu)
app.include_router(router_node)


class SitemapURLs(BaseModel):
    urls: list[str]


@app.post("/sitemap")
def sitemap(urls_data: SitemapURLs):
    urls = urls_data.urls

    # Создаем корневой элемент XML
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    # Добавляем каждый URL в карту сайта
    for url in urls:
        url_element = ET.SubElement(urlset, "url")
        loc_element = ET.SubElement(url_element, "loc")
        loc_element.text = url

    # Создаем XML-документ из корневого элемента
    xml_string = ET.tostring(urlset, encoding="UTF-8")

    # Сохраняем XML-документ как файл

    directory_name = "files/sitemap"
    directory = f"../{directory_name}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, "sitemap.xml")
    with open(file_path, "wb") as f:
        f.write(xml_string)

    # Отправляем путь к файлу как ответ клиенту
    return {"sitemap_path": f"/{directory_name}/sitemap.xml"}


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://redis", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

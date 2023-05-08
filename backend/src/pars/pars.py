import re
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from sqlalchemy import select, desc
from sqlalchemy.orm.exc import NoResultFound

from database import async_session_maker
from pars.models import Link, ParsConfig

avito = 'https://www.avito.ru/'

# до 350 000 (ot 10 sot)
url0 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwWeyJmcm9tIjowLCJ0byI6MzUwMDAwfeb6DhV7ImZyb20iOjEwLCJ0byI6bnVsbH0'
# до 350 - 450
url1 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwbeyJmcm9tIjozNTAwMDAsInRvIjo0NTAwMDB95voOFXsiZnJvbSI6MTAsInRvIjpudWxsfQ'
# 450 - 550
url2 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwbeyJmcm9tIjo0NTAwMDAsInRvIjo1NTAwMDB95voOFXsiZnJvbSI6MTAsInRvIjpudWxsfQ'
# 550 - 650
url3 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwbeyJmcm9tIjo1NTAwMDAsInRvIjo2NTAwMDB95voOFXsiZnJvbSI6MTAsInRvIjpudWxsfQ'
# 650 - 750
url4 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwbeyJmcm9tIjo2NTAwMDAsInRvIjo3NTAwMDB95voOFXsiZnJvbSI6MTAsInRvIjpudWxsfQ'
# 750 - 850
url5 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwbeyJmcm9tIjo4NTAwMDAsInRvIjo5NTAwMDB95voOFXsiZnJvbSI6MTAsInRvIjpudWxsfQ'
# 950 000 - 1 000 000
url6 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwceyJmcm9tIjo5NTAwMDAsInRvIjoxMDAwMDAwfeb6DhV7ImZyb20iOjEwLCJ0byI6bnVsbH0'
# 1 000 000 -1 100 000
url7 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwdeyJmcm9tIjoxMDAwMDAwLCJ0byI6MTEwMDAwMH3m~g4VeyJmcm9tIjoxMCwidG8iOm51bGx9'
# 1 100 000 -1 250 000
url8 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwdeyJmcm9tIjoxMTAwMDAwLCJ0byI6MTI1MDAwMH3m~g4VeyJmcm9tIjoxMCwidG8iOm51bGx9'
# 1 250 000 -1 500 000
url9 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwdeyJmcm9tIjoxMjUwMDAwLCJ0byI6MTUwMDAwMH3m~g4VeyJmcm9tIjoxMCwidG8iOm51bGx9'
# 1 500 000 - 1 750 000
url10 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwdeyJmcm9tIjoxNTAwMDAwLCJ0byI6MTc1MDAwMH3m~g4VeyJmcm9tIjoxMCwidG8iOm51bGx9'
# 1 750 000 - 2 000 0000
url11 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwdeyJmcm9tIjoxNzUwMDAwLCJ0byI6MjAwMDAwMH3m~g4VeyJmcm9tIjoxMCwidG8iOm51bGx9'
# 2.0 - 2.5
url12 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwdeyJmcm9tIjoyMDAwMDAwLCJ0byI6MjUwMDAwMH3m~g4VeyJmcm9tIjoxMCwidG8iOm51bGx9'
# 2.5 - 3.0
url13 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwdeyJmcm9tIjoyNTAwMDAwLCJ0byI6MzAwMDAwMH3m~g4VeyJmcm9tIjoxMCwidG8iOm51bGx9'
# 3.0 - 3.5
url14 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwdeyJmcm9tIjozMDAwMDAwLCJ0byI6MzUwMDAwMH3m~g4VeyJmcm9tIjoxMCwidG8iOm51bGx9'
url15 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQAkDYCBTOWY7eDhQCBEWSCBV7ImZyb20iOjUwLCJ0byI6bnVsbH2WCBV7ImZyb20iOjEwLCJ0byI6bnVsbH3GmgwdeyJmcm9tIjozNTAwMDAwLCJ0byI6NTAwMDAwMH3m~g4VeyJmcm9tIjoxMCwidG8iOm51bGx9'
url16 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQBEDYCBTOWYS9DhTYpNEBkL0OFPKk0QGO3g4UAgRFkggVeyJmcm9tIjo1MCwidG8iOm51bGx9lggVeyJmcm9tIjoxMCwidG8iOm51bGx9xpoMHXsiZnJvbSI6MzUwMDAwMCwidG8iOjUwMDAwMDB95voOFXsiZnJvbSI6MTAsInRvIjpudWxsfQ'
url17 = 'https://www.avito.ru/all/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?f=ASgBAQECAUSUA9AQBEDYCBTOWYS9DhTYpNEBkL0OFPKk0QGO3g4UAgRFkggVeyJmcm9tIjo1MCwidG8iOm51bGx9lggVeyJmcm9tIjozMCwidG8iOm51bGx9xpoMHHsiZnJvbSI6NTAwMDAwLCJ0byI6NTAwMDAwMH3m~g4VeyJmcm9tIjoxMCwidG8iOm51bGx9'
urls = [url0, url1, url2, url3, url4, url5, url6, url7,
        url8, url9, url10, url11, url12, url13, url14, url15, url16, url17]


def get_count_pages(url):
    """ Получаем количество страниц """
    page_html = get_source_page(url)
    if page_html is None:
        print('page_html не получен')
    soup = BeautifulSoup(page_html, 'html.parser')
    next_page_button = soup.find('a', {'data-marker': 'pagination-button/nextPage'})
    print(next_page_button)
    if next_page_button is not None:
        count_pages = next_page_button.previous_element.previous_element
    else:
        count_pages = 100
    return int(count_pages)


def check_page_in_video(source):
    """
        Проверка наличия на странице объявления с видео

        return: код блоков с видео
    """
    soup = BeautifulSoup(source, 'html.parser')
    vid = soup.find('i', class_=re.compile('index-video'))

    if not vid:
        return False
    blocks = soup.find_all('div', class_=re.compile('iva-item-content'))
    return blocks


def get_items_ads(blocks):
    data = []
    for block in blocks:
        video = block.find('i', class_=re.compile('index-video'))
        if video:
            link = 'https://www.avito.ru' + \
                   block.find('a', class_=re.compile('link-link')).get('href')
            price = block.find('meta', itemprop='price').get('content')

            data.append({'link': link, 'price': int(price)})
    return data


async def save_links(data):
    async with async_session_maker() as session:
        for item in data:
            try:
                stmt = select(Link).where(Link.link == item['link'])
                result = await session.execute(stmt)
                link = result.scalars().one_or_none()
                if link is not None:
                    print(
                        f"Ссылка уже есть в базе данных под номером - [{link.id}]")
                    if link.price is None:
                        link.price = item['price']
                        await session.commit()
                        print("Обновление записи :" + str(link.id))
                else:
                    print(
                        f"{item['link']} отсутствует в базе данных, записываю...")
                    session.add(Link(link=item['link']))
                    await session.commit()
                    print('Запись в базу успешно произведена')
            except NoResultFound:
                print(
                    f"{item['link']} отсутствует в базе данных, записываю...")
                session.add(Link(link=item['link']))
                await session.commit()
                print('Запись в базу успешно произведена')
            except Exception as e:
                import traceback
                print(f"Ошибка 91-pars.py:\n{traceback.format_exc()}")


def getWebDriver():
    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_argument('--headless')
    options.add_argument('--disable-extensions')
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-background-networking')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--log-level=3")  # fatal
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-features=site-per-process")
    options.add_argument("--enable-features=NetworkServiceInProcess")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-translate")

    executor = 'http://dreammanor.ru:4444/wd/hub'

    return webdriver.Remote(command_executor=executor, desired_capabilities=options.to_capabilities())


def get_web_driver():
    """Получить веб драйвер с куками"""
    driver = getWebDriver()
    # открываем главную страницу и ставим куки
    driver.get("https://www.avito.ru")
    driver.add_cookie({"name": "view", "value": "gallery"})
    return driver


def get_source_page(url):
    try:
        """Получить код страницы"""
        driver = get_web_driver()
        driver.get(url)
        sleep(5)
        source = driver.page_source
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()
    return source if source else None


async def numberIteration():
    """Запрос к базе данных для получения текущей итерации"""
    async with async_session_maker() as session:
        try:
            stmt = select(ParsConfig).order_by(desc(ParsConfig.id)).limit(1)
            result = await session.execute(stmt)
            num = result.scalars().one_or_none()
            if num is not None:
                return num.number_pars
            else:
                return 1
        except Exception as e:
            print(
                f"Не могу получить номер итерации из базы данных. Ошибка: {e}")
            return 1


async def numberIncrement(num):
    num = num + 1
    async with async_session_maker() as session:
        try:
            session.add(ParsConfig(number_pars=num))
            await session.commit()
        except:
            print("Не удалось увеличить итерацию")


async def run(count_pages=0, sorts=True, agent=False):
    # получаем номер текущей итерации
    count = await numberIteration()
    print(f"\nЗапуск новой итерации под номером [{count}]")
    # поочерёдно проводим парсинг по фильтрованным спискам urls
    for i, url in enumerate(urls):
        # параметры адреса
        options = f"{'&s=104' if sorts else ''}{'' if agent else '&user=1'}"
        print(f"\n\n\n Номер {i} \n {url}{options} \n\n\n")

        # получить количество страниц
        if count_pages == 0:
            count_pages = get_count_pages(url + options)
            print(f"Количество страниц - [{str(count_pages)}]")
        # проверяем постранично наличие объявлений с видео
        for page in range(1, count_pages):
            # получаем код текущей страницы
            current_source_page = get_source_page(f"{url}{options}&p={page}")
            # поверим код страницы на наличие видео
            video_html_blocks = check_page_in_video(current_source_page)
            # если видео нет на странице переход на следующую
            if not video_html_blocks:
                print(
                    f'\n\n\nНа странице {i}/{page} нет объявлений с видео. \nПерехожу на следующею страницу...\n\n\n')
            else:
                # получение ссылок на объявления
                data = get_items_ads(video_html_blocks)
                print(
                    f'\n\n\nНа странице {page} есть [{len(data)}] видео... \n\n\n')
                if data:
                    # сохранить ссылки в базе данных
                    await save_links(data)
    await numberIncrement(count)
    print(f"\n\nИтерация завершена ...\n\n\n\n\n\n")
    return True;

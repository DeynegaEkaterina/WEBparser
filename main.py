import requests
import urllib.parse
from bs4 import BeautifulSoup
from data import headers, cookies, url as main_url


def get_product_info(link):
    encoded_link = urllib.parse.quote(link).replace("%3F", "?").replace("%3D", "=").replace("%26", "&").replace('%3A', ':')
    response = requests.get(url=encoded_link, headers=headers, cookies=cookies)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        try:
            title = soup.find("h1", class_="product_main-title").text
        except AttributeError:
            title = "Заголовок отсутствует"
            print(AttributeError)
            return 0
        try:
            price = soup.find('span', class_='product_pri_all').text.replace(' ', '')[:-4]
        except AttributeError:
            price = "Цена отсутствует"
        try:
            reviews = soup.find('a', class_='product_ref').text.split()[0]
        except AttributeError:
            reviews = "Отзывы отсутствуют"
        try:
            description = soup.find('div', class_='product_long-text').find_all('p')
            description = " ".join([i.text for i in description])
        except AttributeError:
            description = "Описание отсутствует"
        print(f"Ссылка - {encoded_link}\n"
              f"Заголовок - {title}\n"
              f"Цена - {price}\n"
              f"Отзывы - {reviews}\n"
              f"Описание - {description}\n")
    else:
        print(response.status_code)


def get_product_links(data):
    url, pages = data
    for page in range(pages):
        url = f'{url}{page}'
        encoded_url = urllib.parse.quote(url).replace("%3F", "?").replace("%3D", "=").replace("%26", "&").replace('%3A', ':')
        response = requests.get(url=encoded_url, headers=headers, cookies=cookies)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")

            try:
                products = soup.find('div', class_='catalog_products')
                links = [f"{main_url[:-1]}{i.get('href')}" for i in products.find_all('a', class_='_model ddl_product_link')]
                result = []
                for link in links:
                    result.append(link)
                return result

            except AttributeError as ae:
                print(ae)

            print(f"Обработал страницу №{page}")
        else:
            print(response.status_code)


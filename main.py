import requests
from bs4 import BeautifulSoup
from data import headers, cookies, url as main_url
from manticore import push, write_error


def get_product_info(link: str, attempt: int = 1):
    response = requests.get(url=link, headers=headers, cookies=cookies)
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
        data = {
            "title": title, 
            "price": price, 
            "reviews": reviews, 
            "description": description
        }
        push(data)
    elif response.status_code == 404:
        write_error({
            "url": link,
            "status": response.status_code
        })
    elif response.status_code >= 500:
        if attempt > 1:
            write_error({
                "url": link,
                "status": response.status_code
            })
        else:
            get_product_info(link, 2)


def get_product_links(data, attempt: int = 1):
    url, pages = data
    for page in range(pages):
        url = f'{url}{page}'
        response = requests.get(url=url, headers=headers, cookies=cookies)
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
        elif response.status_code == 404:
            write_error({
                "url": link,
                "status": response.status_code
            })
        elif response.status_code >= 500:
            if attempt > 1:
                write_error({
                    "url": link,
                    "status": response.status_code
                })
            else:
                get_product_links(link, 2)


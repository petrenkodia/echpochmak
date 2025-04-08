# Домашка, тоже только 1 страница, буду доделывать

"""import requests
from bs4 import BeautifulSoup

url = 'https://miraculousledybug.ru/ep/s6/'
soup = BeautifulSoup(requests.get(url).content.decode('utf-8'), 'html.parser')
titles = [h2.text.strip() for h2 in soup.select('div.ep h2')]

for i, t in enumerate(titles, 1):
    print(f"{i}. {t}") """

import requests
from bs4 import BeautifulSoup

url = 'https://randewoo.ru/category/aroma-box?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Парсим все товары!!!
products = soup.select('li.products__item')

for i, product in enumerate(products, 1):

    # Название и тип
    name = product['data-name'] [:50]
    category = product.get('data-category', 'Отсутствует')[:25] # не у всех есть

    # Текущая цена (из тега <b itemprop="price">)
    price = product.select_one('b[itemprop="price"]').text.strip()

    print(f"{i:>3}. {name:<50} | Категория: {category:<30} | Цена: {price:>5}")
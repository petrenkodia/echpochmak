# Код Руслана с занятия (чуть покопалась в нем)
import requests
from bs4 import BeautifulSoup

def parse_page(soup) -> list[dict]:
    books_block = soup.find_all(class_='row')[-1]
    _books = books_block.find_all('li')
    abc = []
    for book in _books:
        title = book.find('h3').find('a')['title']
        price = book.find(class_='price_color').text
        abc.append({
            'title': title,
            'price': price
        })
    return abc

url = 'https://books.toscrape.com/' # bs4 https://pypi.org/project/beautifulsoup4/
books = [] # почитать про http запросы. какие есть, в чем отличия

""" response = requests.get(url)
soup = BeautifulSoup(response.content, features="html.parser")
books.extend(parse_page(soup)) """ #присоед. только один

books.extend(parse_page(BeautifulSoup(requests.get(url).content, features="html.parser")))

""" max_page = int(soup.find(class_='current').text.strip().split('of')[-1])
for i in range(2, max_page + 1):
    _url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    books.extend(parse_page(BeautifulSoup(requests.get(_url).content, features="html.parser"))) #присоед. остальные """

print(books)
print(len(books))

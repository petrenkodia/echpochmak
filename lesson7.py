#Мой код с занятия (только 1 страница)
import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/"
books = [] # почитать про http запросы
responce = requests.get(url)

soup = BeautifulSoup(responce.content, features="html.parser")

'''
max_page = int(soup.find(class_='current').text.strip().split('of')[-1])
for i in range(2, max_page+1):
    url=f"https://books.toscrape.com/catalogue/page-{i}.html"  
    '''

bb = soup.find_all(class_ = "row")[-1] # Запускать через Евалюейт Alt F8(?)
_books = bb.find_all('li')
for book in _books:
    title = book.find('h3').find('a')['title']
    price = book.find(class_='price_color').text
    books.append({
        'title': title,
        'price': price
    }) # Можно было кортеж

print(books)
print(" КОНЕЦ!!! ")
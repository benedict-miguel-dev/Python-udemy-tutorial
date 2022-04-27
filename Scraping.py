from random import betavariate
from turtle import title
from webbrowser import get
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(r.text, 'html.parser')

# lists = soup.findAll(class_= 'product_pod')
# Using Selector
movies = soup.select('tr')
movies.pop(0)
print(movies[0])
# for num, item in enumerate(movies):
#     print(num)
print("this is another test")
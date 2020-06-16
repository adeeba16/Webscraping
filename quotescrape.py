import requests_html
from requests_html import HTMLSession, HTMLResponse
from bs4 import BeautifulSoup

session = HTMLSession()
response = session.get('http://quotes.toscrape.com/').html
source = response.html

soup = BeautifulSoup(source, 'lxml')

box = soup.select('.col-md-8')[1]

elements = box.find_all('div')
quotes =[]
authors=[]
for element in elements:
    quote = element.find('span')
    quotes.append(quote)
    
    author = element.find('small')
    authors.append(author)

print(quotes)
print(authors)
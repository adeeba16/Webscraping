import requests_html
from requests_html import HTMLSession, HTMLResponse
from bs4 import BeautifulSoup
import csv

urls = []
for i in range(1,51):
    urls.append(f'http://books.toscrape.com/catalogue/page-{i}.html')

csv_file = open('book.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator ='\n')
csv_writer.writerow(['Title', 'Price', 'ImageUrl'])

count =1 
for url in urls:
    session = HTMLSession()
    response = session.get(url).html
    source = response.html

    soup = BeautifulSoup(source, 'lxml')

    box =  soup.find('ol')

    elements = box.find_all('li')
    # titles =[]
    # prices =[]
    # images =[]
    for element in elements:
        title = element.select('h3 a')[0]['title']
        # print(title)
        # titles.append(title)
        price = element.find('p', class_='price_color').text
        # print(price.text)
        # prices.append(price.text)

        image = element.find('img')['src']
        image_url = ('http://books.toscrape.com/'+image)
        # images.append(image_url)
        csv_writer.writerow([title, price, image_url])
        print(count ,end=' ')
        count = count+1
    # print(titles)
    # print(prices)
    # print(images)

csv_file.close()
import requests_html
from requests_html import HTMLSession, HTMLResponse
from bs4 import BeautifulSoup

session = HTMLSession()
response = session.get('https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht').html
source = response.html

soup = BeautifulSoup(source, 'lxml')

box = soup.find('tbody')
eles = box.find_all('tr')

for ele in eles:

    t1 = ele.find('td', class_= 'titleColumn')
    title = t1.find('a')
    rating = box.find('td', class_= 'ratingColumn')
    gross = box.find('span', class_='secondaryInfo')
    week = box.find('td', class_='weeksColumn')
    
    print(title.text)
    print(rating.text.strip())
    print(gross.text)
    print(week.text)
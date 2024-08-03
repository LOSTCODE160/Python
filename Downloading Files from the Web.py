
import requests
from bs4 import BeautifulSoup
def flip_spider(max_page):
    page=1
    while page <=max_page:
     url='https://www.ebay.com/sch/i.html?_from=R40&_nkw=ppokemon+cards&_sacat=0&_pgn='+str(page)
     source_code=requests.get(url)
     plain_text=source_code.text
     soup = BeautifulSoup(plain_text, 'html.parser')
     for link in soup.findAll('a',{'class':'s-item__title'}):
        div = 'https://www.ebay.com'+link.get('div')
        print(div)
    page+=1     

flip_spider(1)        





import mysql.connector
conn=mysql.connector.connect(
    host='localhost', password ='vithal1234',user='root',database='python_data'
)
if conn.is_connected():
    print("Connected to MySQL Database")





import requests
from bs4 import BeautifulSoup
def flip_spider(max_page):
    page=1
    url='https://www.ebay.com/sch/i.html?_from=R40&_nkw=ppokemon+cards&_sacat=0&_pgn='+str(page)
    source_code=requests.get(url)
    plain_text=source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for link in soup.findAll('a',{'class':'s-item__link'}):
        print(link.text,"\n")
    page+=1     

flip_spider(1)        


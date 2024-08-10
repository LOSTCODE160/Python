import requests
from bs4 import BeautifulSoup
import operator
def start(url):
    word_list=[]
    source_code=requests.get(url).text
    soup=BeautifulSoup(source_code)
    for post_text in soup.findAll('a',{'class':'s-item s-item__pl-on-bottom'}):
        content =post_text.string
        words=content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)
start(url='https://www.ebay.com/sch/i.html?_from=R40&_nkw=ppokemon+cards&_sacat=0&_pgn=1')
import requests
from bs4 import BeautifulSoup

def flip_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=' + str(page)
        response = requests.get(url) 
        plain_text = response.text  
        soup = BeautifulSoup(plain_text, 'html.parser') 

        
        for link in soup.find_all('a', {'class': 'KzDlHZS'}):
            href = link.get('href')
            full_url = "https://www.flipkart.com" + href
            print(full_url)
        
        page += 1 

flip_spider(1)



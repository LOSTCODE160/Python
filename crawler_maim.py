

import mysql.connector
import requests
from bs4 import BeautifulSoup

def connect_to_database():
    try:
        # Replace with your actual database credentials (avoid hardcoding)
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='vithal1234',
            database='python_data'
        )
        return conn
    except mysql.connector.Error as err:
        print("Error connecting to database:", err)
        return None  # Indicate failure

def flip_spider(max_page, conn):

    if not conn:
        print("Failed to connect to database. Aborting scraping.")
        return

    page = 1
    base_url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=pokemon+cards&_sacat=0&_pgn="  # Replace with actual URL
    while page <= max_page:
        url = base_url + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')

        cursor = conn.cursor()
        for link in soup.findAll('a', {'class': 's-item__link'}):

            try:
                cursor.execute("INSERT INTO ebay_listings (title) VALUES (%s)", (link.text,))
            except mysql.connector.Error as err:
                print("Error inserting data:", err)
            finally:
                pass
                # if cursor:
                #     cursor.close()

            print(link.text, "\n")

        conn.commit()
        cursor.close()
        page += 1

if __name__ == "__main__":
    conn = connect_to_database()
    flip_spider(1, conn)

    if conn:
        conn.close()
        print("Database connection closed.")

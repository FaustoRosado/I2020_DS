import requests
from bs4 import BeautifulSoup

url = 'https://www.coalitionforthehomeless.org/basic-facts-about-homelessness-new-york-city-data-and-charts/'
req = requests.get(url)

soup = BeautifulSoup(req.content)

if __name__ == '__main__':    
    print(soup.prettify())
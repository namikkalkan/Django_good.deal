import requests
import urllib.request
import time
from bs4 import BeautifulSoup
url= 'https://shop.coles.com.au/a/richmond-south/product/omo-sensitive-front-top-loader-laundry-liquid'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.findAll('a'))
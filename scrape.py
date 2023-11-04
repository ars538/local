from bs4 import BeautifulSoup
import requests


response=requests.get("http//example.com")
soup=BeautifulSoup(response.content,'html')
print(soup.prettify())
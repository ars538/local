from bs4 import BeautifulSoup
import requests


response=requests.get("http//example.com")
soup=BeautifulSoup(response.content,'lxml')
print(soup.content)

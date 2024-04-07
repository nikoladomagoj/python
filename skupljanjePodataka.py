"""
import requests
from bs4 import BeautifulSoup

url = "https://www.uciliste-virtus.hr/index.php/programi-obrazovanja"
response = requests.get(url)#respons moze biti i odgovori npr
htmlsadrzaj = response.content
soup = BeautifulSoup(htmlsadrzaj, 'html.parser')# prebaciva podatke iz htmla
programi = soup.find_all('h2')# prilagođavamo ovisno o struktruri stranice
for program in programi:
    print(program.text.strip())# sa stripom cemo maknut oznake, ostavljen samo text
"""
"""
import requests
from bs4 import BeautifulSoup

url ="https://www.emmezeta.hr/informatika.html"
response = requests.get(url)
htmlsadrzaj = response.content
soup = BeautifulSoup(htmlsadrzaj, 'html.parser')
informatika = soup.find_all('div', class_="categories-list__name")
for proizvodi in informatika:
    print(proizvodi.text.strip())
"""
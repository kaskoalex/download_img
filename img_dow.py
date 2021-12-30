#приложения для скачивания всех картинок в тегах img указанием адреса src
#если требуется установить pip через терминал, команда внизу, при наличии пакета python
#py get-pip.py


import requests 
# если требуется установить через терминал, команда внизу
# pip install requests
from bs4 import BeautifulSoup as bs
#если требуется установить через терминал, команда внизу
# pip install beautifulsoup4
from requests.models import Response
import os

url="......"
# введите адрес страницы в кавычках
# создайте в рабочей папке папку для картинок 
# в этом случае img , названия файлов остaются как в оригинале.


soup = bs(requests.get(url).content,"html.parser")

img_urls=[]

for img in soup.find_all("img"):
    print(img.attrs.get("src"))
    img_url=url+img.attrs.get("src")
    img_urls.append(img_url)

for url in img_urls:
    response =requests.get(url)
    size = int(response.headers.get("Content-Length",0))
    name=os.path.join("img", url.split("/")[-1])
    with open(name,"wb") as code:
        code.write(response.content)     




import requests
from bs4 import BeautifulSoup
import random
import wikipedia

'''
random_page = random.randint(2000, 3000)
url = f'https://nekdo.ru/short/{random_page}/'
r = requests.get(url)

print(r.status_code)
r.encoding = 'UTF-8'
#print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
ank = soup.find_all('div', class_ = 'text')
#print(ank)
all_ank = []
if r.status_code == 200:
    for i in ank:
        all_ank.append(i.getText())
    print(all_ank)
#print(random.choice(all_ank))


url = 'https://www.a1.by/ru/shop/phones/c/smartphones?q=%3Arelevance&page=1'
url2 = 'https://www.a1.by/ru/shop/phones/c/smartphones?q=%3Arelevance&page=777'
r = requests.get(url)
r2 = requests.get(url2)
print(r.status_code)
print(r2.status_code)
print(len(r.text))
print(len(r2.text))
b = BeautifulSoup(r.text, 'html.parser')
title = b.select('div.product-listing-item-title')
#print(title)
all_title = []
for i in title:
    all_title.append(i.getText())
print(all_title)
'''
wikipedia.set_lang('ru')
quest = 'fedora linux'
print(wikipedia.summary(quest, sentences=2))
print(wikipedia.page(quest).content)

print(wikipedia.page(quest).url)
print(wikipedia.page(quest).images[0])

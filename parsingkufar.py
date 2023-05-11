import requests
from bs4 import BeautifulSoup

url = 'https://www.kufar.by/l/r~minsk-frunzenskij'
r = requests.get(url)
r.encoding = 'UTF-8'
#print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
ank = soup.select('div', class_ = 'styles')
print(ank)
all_ank = []
for i in ank:
    all_ank.append(i.getText())
print(all_ank)
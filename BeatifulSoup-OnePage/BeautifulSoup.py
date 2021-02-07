import urllib

import requests
from bs4 import BeautifulSoup as bs
links=[]
sayfa =("https://www.google.com/search?q=baklava&sxsrf=ALeKk00EVm8ZX8NQuJJaQAJQHTHamSlOSA:1612721802645&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjP56vxsNjuAhVSzBoKHQY9D1UQ_AUoAXoECAUQAw&biw=622&bih=610&dpr=1.5")
r = requests.get(sayfa)
soup = bs(r.content,'html.parser')
entryler = soup.findAll("img")
#print(entryler)
for img in entryler:
    link=img.get('src')
    if "https" in link:
        links.append(link)
print(len(links))
for i in range(len(links)):
    filename = 'img{}.png'.format(i)
    urllib.request.urlretrieve(links[i],filename)
#print(filename)





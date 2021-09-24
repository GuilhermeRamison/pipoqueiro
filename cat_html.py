
import requests
from bs4 import BeautifulSoup

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}
wiki = "https://www.l2code.com.br/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
r = requests.get(wiki, headers=headers)
c = r.content
soup = BeautifulSoup(c, features="html.parser")
print(soup.encode('utf-8'))
#file = open("index.html", "a")
#file.write(str(soup))
#file.close()
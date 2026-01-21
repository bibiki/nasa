import html
import requests
from bs4 import BeautifulSoup

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "3600",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
}

result = []

print("********************")
#----------manx.news
url = "https://www.manx.news/"
req = requests.get(url, headers)
soup = BeautifulSoup(html.unescape(req.text), "html.parser")

for e in soup.select("h3.entry-title a"):
    if "javascript" not in e['href']:
        result.append(e['href'])
#        print(e)
#------------------
print("********************")
#---------iomtotday.co.io
url = "https://www.iomtoday.co.im/news"
req = requests.get(url, headers)
soup = BeautifulSoup(html.unescape(req.text), "html.parser")
for e in soup.select("div div div div div.inner_wrapper div a"):
    if 'class' not in e and "news" in e['href'] and e['href'][-1] in "0123456789":
        result.append("https://iomtoday.co.im" + e['href'])
#        print("https://iomtoday.co.im" + e['href'])
#------------------------
print("********************")
#-----------------gef-im
url = "https://gef.im/"
req = requests.get(url, headers)
soup = BeautifulSoup(html.unescape(req.text), "html.parser")
for e in soup.select("div.mvp-widget-feat2-right a"):
    result.append(e['href'])
#    print(e['href'])

def mapper(link):
    return "<a href=\""+link+"\">"+link+"</a></br>"

result = map(mapper, result)
with open("../docs/index.html", "w", encoding="utf-8") as f:
    f.write("".join(result))

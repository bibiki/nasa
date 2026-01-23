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
def mapper(link):
    return "<a href=\""+link+"\">"+link+"</a></br>"

print("********************")
#----------manx.news
def crawl_manx(url, headers):
    req = requests.get(url, headers)
    soup = BeautifulSoup(html.unescape(req.text), "html.parser")
    result = []
    for e in soup.select("h3.entry-title a"):
        if "javascript" not in e['href']:
            result.append(e['href'])
    result = map(mapper, result)
    return "</br>".join(result)
#------------------
print("********************")
#---------iomtotday.co.io
def crawl_iomtoday(url, headers):
    req = requests.get(url, headers)
    soup = BeautifulSoup(html.unescape(req.text), "html.parser")
    result = []
    for e in soup.select("div div div div div.inner_wrapper div a"):
        if 'class' not in e and "news" in e['href'] and e['href'][-1] in "0123456789":
            result.append("https://iomtoday.co.im" + e['href'])
    result = map(mapper, result)
    return "</br>".join(result)
#------------------------
print("********************")
#-----------------gef-im
def crawl_gef(url, headers):
    req = requests.get(url, headers)
    soup = BeautifulSoup(html.unescape(req.text), "html.parser")
    result = []
    for e in soup.select("div.mvp-widget-feat2-right a"):
        result.append(e['href'])
    result = map(mapper, result)
    return "</br>".join(result)
#-----------------------
url = "https://www.manx.news/"
result = "<div>"+crawl_manx(url, headers)+"</div>"
url = "https://www.iomtoday.co.im/news"
result += "<div>"+crawl_iomtoday(url, headers)+"</div>"
url = "https://gef.im/"
result += "<div>"+crawl_gef(url, headers)+"</div>"
result = "<div>"+result+"</div>"

with open("../docs/index.html", "w", encoding="utf-8") as f:
    f.write("".join(result))

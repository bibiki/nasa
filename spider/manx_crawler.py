import html
import requests
from bs4 import BeautifulSoup

def mapper_manx(link):
    return "<a href=\""+link+"\">"+headline_manx(link)+"</a></br>"

def headline_manx(link):
    res = link[22:].split("-")
    res = map(lambda x: x.capitalize(), res)
    return " ".join(res).replace("/", "")

def crawl_manx(url, headers):
    req = requests.get(url, headers)
    soup = BeautifulSoup(html.unescape(req.text), "html.parser")
    result = []
    for e in soup.select("h3.entry-title a"):
        if "javascript" not in e['href']:
            result.append(e['href'])
    result = map(mapper_manx, result)
    return "</br>".join(result)

import html
import requests
from bs4 import BeautifulSoup

def mapper_gef(link):
    return "<div class=\"story\"><a href=\""+link+"\">"+headline_gef(link)+"</a>\n</div>"

def headline_gef(link):
    res = link[21:].split("-")
    res.pop()
    if "/" in res[0]:
        res[0] = res[0][res[0].index("/") + 1:]
    res = map(lambda x: x.capitalize(), res)
    return " ".join(res)

def crawl_gef(url, headers):
    req = requests.get(url, headers)
    soup = BeautifulSoup(html.unescape(req.text), "html.parser")
    result = []
    for e in soup.select("div.mvp-widget-feat2-right a"):
        result.append(e['href'])
    result = map(mapper_gef, result)
    #return "</br>".join(result)
    return "<div class=\"column-header\">GEF</div><div class=\"story-list\">\n" + "\n".join(result) + "</div>"

import html
import requests
from common import story_div
from bs4 import BeautifulSoup

def mapper_iomtoday(link):
    return story_div(link, headline_iomtoday)

def headline_iomtoday(link):
    res = link[28:].split("-")
    if "/" in res[0]:
        res[0] = res[0][res[0].index("/") + 1:]
    res.pop()
    res = map(lambda x: x.capitalize(), res)
    return " ".join(res)

def crawl_iomtoday(url, headers):
    req = requests.get(url, headers)
    soup = BeautifulSoup(html.unescape(req.text), "html.parser")
    result = []
    for e in soup.select("div div div div div.inner_wrapper div a"):
        if 'class' not in e and "news" in e['href'] and e['href'][-1] in "0123456789":
            result.append("https://iomtoday.co.im" + e['href'])
    result = map(mapper_iomtoday, result)
    #return "</br>".join(result)
    return "<div class=\"column-header\">IOM Today</div><div class=\"story-list\">\n" + "\n".join(result) + "</div>"

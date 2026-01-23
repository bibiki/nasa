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
#----------manx.news
def mapper_manx(link):
    return "<a href=\""+link+"\">"+headline_manx(link)+"</a></br>"

def headline_manx(link):
    res = link.split("-")
    res[0] = res[0][res[0].rindex("/")]
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
#------------------

#---------iomtotday.co.io
def mapper_iomtoday(link):
    return "<a href=\""+link+"\">"+headline_iomtoday(link)+"</a></br>"

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
    return "</br>".join(result)
#------------------------

#-----------------gef-im
def mapper_gef(link):
    return "<a href=\""+link+"\">"+headline_gef(link)+"</a></br>"

def headline_gef(link):
    res = link[20:].split("-")
    res.pop()
    if "/" in res[0]:
        res[0] = res[0][res[0].index("/"):]
    res = map(lambda x: x.capitalize(), res)
    return " ".join(res)

def crawl_gef(url, headers):
    req = requests.get(url, headers)
    soup = BeautifulSoup(html.unescape(req.text), "html.parser")
    result = []
    for e in soup.select("div.mvp-widget-feat2-right a"):
        result.append(e['href'])
    result = map(mapper_gef, result)
    return "</br>".join(result)
#-----------------------
url = "https://www.manx.news/"
result = "<div class=\"column\">"+crawl_manx(url, headers)+"</div>"
url = "https://www.iomtoday.co.im/news"
result += "<div class=\"column\">"+crawl_iomtoday(url, headers)+"</div>"
url = "https://gef.im/"
result += "<div class=\"column\">"+crawl_gef(url, headers)+"</div>"
result = "<div class=\"container\">"+result+"</div>"

result = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <style>
    .container {
      display: flex;
      gap: 16px;
      padding: 20px;
      max-width: 900px;
      margin: 20px auto;
    }
    .column {
      flex: 1;
      background: #e3f2fd;
      padding: 24px;
      border-radius: 8px;
      text-align: center;
      font-family: system-ui, sans-serif;
    }
  </style>
</head>
<body>
""" + result + "</body></html>"

with open("../docs/index.html", "w", encoding="utf-8") as f:
    f.write("".join(result))

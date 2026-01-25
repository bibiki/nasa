from manx_crawler import crawl_manx
from gef_crawler import crawl_gef
from iomtoday_crawler import crawl_iomtoday
from layout import head, footer
headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "3600",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
}

url = "https://www.manx.news/"
result = "<div class=\"column\">"+crawl_manx(url, headers)+"</div>"
url = "https://www.iomtoday.co.im/news"
result += "<div class=\"column\">"+crawl_iomtoday(url, headers)+"</div>"
url = "https://gef.im/"
result += "<div class=\"column\">"+crawl_gef(url, headers)+"</div>"

result = head + result + footer

with open("../docs/index.html", "w", encoding="utf-8") as f:
    f.write("".join(result))

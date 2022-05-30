import requests
from bs4 import  BeautifulSoup
url="https://www.cctv.com/"
res = requests.get(url)
res.encoding = "utf-8"
html = res.text
#print(html)

soup = BeautifulSoup(html, "html.parser")
news_list = soup.select(".bold")#找错了
print(len(news_list))
if len(news_list) >= 0:
    print("This is not asynchronous request")
else :
    print("asynchronous request.\nUse F12 to find the port")

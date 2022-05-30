import json
import requests
from bs4 import BeautifulSoup

url = "https://book.qidian.com/info/1028598839/#Catalog"
res = requests.get(url)
res.encoding = "utf-8"
html = res.text
# print(json_text)
soup = BeautifulSoup(html, "html.parser")
novel_list = soup.select(".book_name")
print(len(novel_list))
if len(novel_list) >= 0:
    print("不是异步请求")
else:
    print('这是异步请求，寻找接口')

# print(json_text)

# json_text = json_text.replace("data_callback(", "").replace("")
# json_object = json.loads(json_text)

# print(json_object)

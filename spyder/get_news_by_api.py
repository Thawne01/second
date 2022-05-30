import requests
import  json
from  bs4 import  BeautifulSoup
url = "https://news.163.com/special/cm_yaowen20200213/?callback=data_callback"
res = requests.get(url)
json_text = res.text
#print("成功进入")
#print(len(html))

json_text = json_text.replace("data_callback(", "").replace("])", "]")
#print(json_text)



#解析Json 数据
json_object = json.loads(json_text)
#print(json_object)

for json_raw in json_object:
    print(json_raw["title"])


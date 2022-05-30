import requests
from bs4 import BeautifulSoup



url = "https://book.qidian.com/info/1028598839/#Catalog"
res = requests.get(url)
res.encoding = "utf-8"
html = res.text


#print(html)

soup = BeautifulSoup(html, 'html.parser')
#print("Title = ", soup.title.text)
#print("a =", soup.h2)
datalist = soup.find_all("h2")
data_needed = len(datalist)
print("我需要的章节数目是:", data_needed)
#print("datalist = ", datalist)

#了解datalist有多长
#print(len(datalist))


print("Title : ", datalist[0].a.text)


times = 0
#i = 0
#dataurl = 1
for items in soup.find_all("h2", class_='book_name'):
    item = items.select('a')[0]
    dataurl = item.get('href')
    times += 1
    #print(dataurl)


#    i += 1
#    times += 1
#    #print(dataurl)

#print(dataurl)
#搞清楚到底有多少个url地址
print(times)

#章节数目校对
if data_needed == times:
    print("数目校对成功，即将进入下一步")
else :
    print("Error")







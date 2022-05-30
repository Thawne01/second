from bs4 import BeautifulSoup
import requests
import re


def cho_htm(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    html = res.text
    return html


html = cho_htm('https://read.qidian.com/chapter/vgA95QrUjZxxo3Pbs2jtrw2/i3ZdDxFzSYH6ItTi_ILQ7A2/')
# 生成BeautifulSoup对象,第一个参数是页面，第二个参数是解析库，python里的解析库是parser
soup = BeautifulSoup(html, "html.parser")
# text_list = soup.select("div", id='j_699443024')
text_list = soup.find_all("div", id='j_699443024')
print(text_list)
print(len(text_list))  # 只有一个
temp_text = text_list[0]
print(type(temp_text))  # <class 'bs4.element.Tag'>
# print(temp_text.text)  # 成功获取到页面内容
formula_text = temp_text.text
print(type(formula_text))
formula_text = formula_text.strip()  # 去掉两头多余的空行

with open('novel3.txt', mode='w', encoding='utf-8') as f:
    formula_text = formula_text.replace('\u3000', '')  # 去掉文本中间的空格
    f.write(formula_text)
    f.flush()

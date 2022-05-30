from bs4 import BeautifulSoup
import requests

source_page = 'https://book.qidian.com/info/1033058170/#Catalog'


def cho_htm(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    html = res.text
    return html


source_html = cho_htm(source_page)
soup_source = BeautifulSoup(source_html, 'html.parser')
ur = soup_source.find_all('h2')  # 拿到了h2列表
name_li = []  # 定义一个空列表来存放章节名
url_li = []
for ele in ur:
    # print(ele.a.text)
    name = ele.a.text
    name_li.append(name)  # 将一个个章节名添加到列表里
    # print(ele.a['href'])
    url_li.append(ele.a['href'])

for ele in url_li:
    ele = ele.replace('//', 'http://')
    html1 = cho_htm(ele)
    soup = BeautifulSoup(html1, 'html.parser')
    tex = soup.find_all('div')
    print(tex[0])
    break












    # print(text_list)
    # print(len(text_list))  # 只有一个
    # temp_text = text_list[0]
    # print(type(temp_text))  # <class 'bs4.element.Tag'>
    # # print(temp_text.text)  # 成功获取到页面内容
    # formula_text = temp_text.text
    # print(type(formula_text))
    # formula_text = formula_text.strip()  # 去掉两头多余的空行
    #
    # with open('novel3.txt', mode='w', encoding='utf-8') as f:
    #     formula_text = formula_text.replace('\u3000', '')  # 去掉文本中间的空格
    #     f.write(formula_text)
    #     f.flush()


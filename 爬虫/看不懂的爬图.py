import re
import requests
import os
from bs4 import BeautifulSoup

def getHtml(url):  #固定格式，获取html内容
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }  #模拟用户操作
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('网络状态错误')

def getUrlList(url):  # 获取图片链接
    url_list = []  #存储每张图片的url，用于后续内容爬取
    demo = getHtml(url)
    soup = BeautifulSoup(demo,'html.parser')
    sp = soup.find_all('div', class_="list") #class='list'在全文唯一，因此作为锚，获取唯一的div标签；注意，这里的网页源代码是class，但是python为了和class（类）做区分，在最后面添加了_
    nls = re.findall(r'a href="(.*?)" rel="external nofollow"  rel="external nofollow" ', str(sp)) #用正则表达式提取链接
    for i in nls:
        if 'https' in i: #因所有无效链接中均含有'https'字符串，因此直接剔除无效链接（对应第3条的分析）
            continue
        url_list.append('http://www.netbian.com' + i) #在获取的链接中添加前缀，形成完整的有效链接
    return url_list

def fillPic(url,page):
    pic_url = getUrlList(url) #调用函数，获取当前页的所有图片详情页链接
    path = './美女'  # 保存路径
    for p in range(len(pic_url)):
        pic = getHtml(pic_url[p])
        soup = BeautifulSoup(pic, 'html.parser')
        psoup = soup.find('div', class_="pic") #class_="pic"作为锚，获取唯一div标签；注意，这里的网页源代码是class，但是python为了和class（类）做区分，在最后面添加了_
        picUrl = re.findall(r'src="(.*?)"', str(psoup))[0] #利用正则表达式获取详情图片链接，因为这里返回的是列表形式，所以取第一个元素（只有一个元素，就不用遍历的方式了）
        pic = requests.get(picUrl).content #打开图片链接，并以二进制形式返回（图片，声音，视频等要以二进制形式打开）
        image_name ='美女' + '第{}页'.format(page) + str(p+1) + '.jpg' #给图片预定名字
        image_path = path + '/' + image_name #定义图片保存的地址
        with open(image_path, 'wb') as f: #保存图片
            f.write(pic)
            print(image_name, '下载完毕！！！')

def main():
    n = input('请输入要爬取的页数：')
    url = 'http://www.netbian.com/meinv/'  # 资源的首页，可根据自己的需求查看不同分类，自定义改变目录，爬取相应资源
    if not os.path.exists('./美女'):  # 如果不存在，创建文件目录
        os.mkdir('./美女/')
    page = 1
    fillPic(url, page)  # 爬取第一页，因为第1页和后续页的链接的区别，单独处理第一页的爬取
    if int(n) >= 2: #爬取第2页之后的资源
        ls = list(range(2, 1 + int(n)))
        url = 'http://www.netbian.com/meinv/'
        for i in ls: #用遍历的方法对输入的需求爬取的页面做分别爬取处理
            page = str(i)
            url_page = 'http://www.netbian.com/meinv/'
            url_page += 'index_' + page + '.htm' #获取第2页后的每页的详情链接
            fillPic(url_page, page) #调用fillPic()函数
import re
import requests
import os
from bs4 import BeautifulSoup

def getHtml(url):  #固定格式，获取html内容
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }  #模拟用户操作
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('网络状态错误')

def getUrlList(url):  # 获取图片链接
    url_list = []  #存储每张图片的url，用于后续内容爬取
    demo = getHtml(url)
    soup = BeautifulSoup(demo,'html.parser')
    sp = soup.find_all('div', class_="list") #class='list'在全文唯一，因此作为锚，获取唯一的div标签；注意，这里的网页源代码是class，但是python为了和class（类）做区分，在最后面添加了_
    nls = re.findall(r'a href="(.*?)" rel="external nofollow"  rel="external nofollow" ', str(sp)) #用正则表达式提取链接
    for i in nls:
        if 'https' in i: #因所有无效链接中均含有'https'字符串，因此直接剔除无效链接（对应第3条的分析）
            continue
        url_list.append('http://www.netbian.com' + i) #在获取的链接中添加前缀，形成完整的有效链接
    return url_list

def fillPic(url,page):
    pic_url = getUrlList(url) #调用函数，获取当前页的所有图片详情页链接
    path = './美女'  # 保存路径
    for p in range(len(pic_url)):
        pic = getHtml(pic_url[p])
        soup = BeautifulSoup(pic, 'html.parser')
        psoup = soup.find('div', class_="pic") #class_="pic"作为锚，获取唯一div标签；注意，这里的网页源代码是class，但是python为了和class（类）做区分，在最后面添加了_
        picUrl = re.findall(r'src="(.*?)"', str(psoup))[0] #利用正则表达式获取详情图片链接，因为这里返回的是列表形式，所以取第一个元素（只有一个元素，就不用遍历的方式了）
        pic = requests.get(picUrl).content #打开图片链接，并以二进制形式返回（图片，声音，视频等要以二进制形式打开）
        image_name ='美女' + '第{}页'.format(page) + str(p+1) + '.jpg' #给图片预定名字
        image_path = path + '/' + image_name #定义图片保存的地址
        with open(image_path, 'wb') as f: #保存图片
            f.write(pic)
            print(image_name, '下载完毕！！！')

def main():
    n = input('请输入要爬取的页数：')
    url = 'http://www.netbian.com/meinv/'  # 资源的首页，可根据自己的需求查看不同分类，自定义改变目录，爬取相应资源
    if not os.path.exists('./美女'):  # 如果不存在，创建文件目录
        os.mkdir('./美女/')
    page = 1
    fillPic(url, page)  # 爬取第一页，因为第1页和后续页的链接的区别，单独处理第一页的爬取
    if int(n) >= 2: #爬取第2页之后的资源
        ls = list(range(2, 1 + int(n)))
        url = 'http://www.netbian.com/meinv/'
        for i in ls: #用遍历的方法对输入的需求爬取的页面做分别爬取处理
            page = str(i)
            url_page = 'http://www.netbian.com/meinv/'
            url_page += 'index_' + page + '.htm' #获取第2页后的每页的详情链接
            fillPic(url_page, page) #调用fillPic()函数

main()


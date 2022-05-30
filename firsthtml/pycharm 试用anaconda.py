# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 10:40:45 2021

@author: MC
"""

from bs4 import BeautifulSoup
import requests
url = "http://localhost:63342/pythonProject5/firsthtml/firsthtml.html?_ijt=oeom0rs3575oui7us1r34mufi7"
res = requests.get(url)
res.encoding = "utf-8"
html = res.text


#将HTML变成beautifulsoup对象
soup = BeautifulSoup(html, "html.parser")
#print("title = ",soup.title.text)


#获取第一个DIV
#print("div =",soup.div)
#获取全部DIV
divList = soup.find_all("div")
print("divList = ", divList)
#print("font text = ", divList[0].font.text)
#print("font id = ", divList[1].font["id"])
#print("font color = ", divList[1].font["color"])

print("------------------------------------------------------------")

#通过class name 获取DIV
#divList = soup.find_all("div")
#print("divList = ",divList)
#print("font text = ",divList[1].font.text)
#print("font id = ",divList[1].font["id"])
#print("font color = ",divList[1].font["color"])


#通过ID获取DIV
div2 = soup.find_all("div", id="div2")
print("div2 = ", div2)

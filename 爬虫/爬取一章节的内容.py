import requests
from lxml import etree


def electric_machine(url):
    res = requests.get(url)
    res.encoding = "zh-cn"
    # print(res.text)
    return res.text


url = 'https://read.qidian.com/chapter/T3P_Qq0ZHA3ywypLIF-xfQ2/nacCFobP_1jM5j8_3RRvhw2/'
answer = electric_machine(url)
# print(answer)
# print(get_source)  函数在内存中的位置


html = etree.HTML(answer)

p_content = html.xpath('/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/p')
pur = len(p_content)
# for i in range(0, 2):
#     p_content = p_content[i]
#     p_con = p_content.xpath("//span[@class='content-wrap']")[i]
#     # print(etree.tostring(p_con, encoding='utf-8').decode())
#     print(p_con.text)

pds = []  # 定义列表存放各个有目标数据的标签
for ele in p_content:
    # print(ele)#获取一个个标签
    pd = ele.xpath("/span[@class='content-wrap']")[1]
    pds.append(pd)
    print(pd.text)
    # print(pds) #获取到蕴含文本的标签，存放在列表里

# per = len(pds)
# if per == pur:
#     print("目标数量核对成功")
#     # with open('./目标.txt', mode='wt', encoding='utf-8') as fs:
#     #     for ele in pds:
#     #         fs.write(ele)
#     #     print(fs.readlines())
#
# else:
#     print("这不对啊")


# with open('novel.txt', 'w', encoding='utf-8', newline='') as f:
#     writer = txt.DictWriter(f, fieldnames=['title', 'star', 'quote', 'url'])
#
#     writer.writeheader()  # 写入表头
#
#     for each in movieList:
#         writer.writerow(each)

# -*- codeing = utf-8 -*-
# @Time : 2021/9/20 21:49
# @Author :
# @File : testcompile.py
# @Software : PyCharm

import urllib
import re
from bs4 import BeautifulSoup
from urllib import request


findword = re.compile(r'<span (.*)">(.*)</span>')
findtitle = re.compile(r'<h1 class="content-title">(.*)</h1>')
findtime = re.compile(r'<p class="content-tip">(.*)?<script>',re.S)
findImg = re.compile(r'<img src="(.*?)"',re.S)

def askURL(url):
    head = {
        "User-Agent": " Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 70.0.3538.25 Safari / 537.36Core / 1.70.3877.400 QQBrowser / 10.8.4506.400"
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try :
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html



baseurl = "https://sise.uestc.edu.cn/info/1017/"
url = baseurl + str(1016) + ".htm"
html = askURL(url)
data = []
# 解析网页
soup = BeautifulSoup(html, "html.parser")
for item in soup.find_all('div', class_="v_news_content"):
    item = str(item)

    img = re.findall(findImg,item)
    print(len(img))
    print(img)

# for i in soup.find(class_="v_news_content").find_all("p"):
#     i = str(i)
#     img = re.findall(findImg,i)[0]
#     print(img)


















#     print(type(item))
    # item = str(item)
    # title = re.findall(findtitle, item)[0]
    # data.append(title)
    #print(data[0])


    # time = re.findall(findtime, item)[0]
    # time = re.findall('\d*',time)[1] +" " + re.findall('\d*',time)[3] + " " + re.findall('\d*',time)[5]
    # data.append(time)
    # print(data[1])
    #
    # for i in soup.find_all('div', class_="v_news_content"):
    #     i = str(i)
    #     word = re.findall(findword,i)










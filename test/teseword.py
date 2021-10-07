# -*- codeing = utf-8 -*-
# @Time : 2021/9/20 23:26
# @Author :
# @File : teseword.py
# @Software : PyCharm

import urllib
import re
from bs4 import BeautifulSoup
from urllib import request
import scrapy

#findword = re.compile(r'<span (.*)">([\u4e00-\u9fa5]*)</span>')
findword = re.compile(r'<span(.*)?">(<strong>)?(.*?)(</strong>)?(.*)</span>')
#findword = re.compile(r'<span\s[^>]*\slab="[^""]*"\s[^>]*>[^<>]*</span>')      #没用
find = re.compile(r'<p\s(.*?)>(.*)</p>')


# <span microsoft="" yahei";="" color:="" rgb(0,="" 0,="" 0);"="" style="font-family: 微软雅黑, ">
# <span style="color: rgb(0, 0, 0);"><strong>
# <span style="font-size:16px;line-height:150%;font-family:仿宋_GB2312">
# <span style="font-size: 16px; color: rgb(0, 0, 0); font-family: 微软雅黑;">


# def askURL(url):
#     head = {
#         "User-Agent": " Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 70.0.3538.25 Safari / 537.36Core / 1.70.3877.400 QQBrowser / 10.8.4506.400"
#     }
#     request = urllib.request.Request(url,headers=head)
#     html = ""
#     try :
#         response = urllib.request.urlopen(request)
#         html = response.read().decode("utf-8")
#     except urllib.error.URLError as e:
#         if hasattr(e,"code"):
#             print(e.code)
#         if hasattr(e,"reason"):
#             print(e.reason)
#
#     return html

baseurl = "https://sise.uestc.edu.cn/info/1021/"
url = baseurl + str(1308) + ".htm"
head = {
        "User-Agent": " Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 70.0.3538.25 Safari / 537.36Core / 1.70.3877.400 QQBrowser / 10.8.4506.400"
    }
request = urllib.request.Request(url,headers=head)
html = ""
response = urllib.request.urlopen(request)
html = response.read().decode("utf-8")



data = []
# 解析网页

soup = BeautifulSoup(html, "html.parser")
print(soup)
for item in soup.find_all('div', class_="v_news_content"):
     item = str(item)
     word = re.findall(find, item)[0]
     #word = re.sub()
     data.append(word)
     #print(data[0])

     #print(type(item))


    #print(item.span.string)
    #print(item.span.attrs)

# page = response.xpath('//div[@class="v_news_content"]')
# content_list = []
# for content in page:
#     content_list = content.xpath('//span[@style=" font-family "]').extract()
#     print(content_list)






# -*- codeing = utf-8 -*-
# @Time : 2021/10/6 20:05
# @Author :
# @File : test2.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import re
from urllib import request,parse,error
import sqlite3
import urllib
import json


fname = re.compile(r'"mid"="(\d*)","uname":"(.*?)","sex',re.S)
fword = re.compile(r'"content":{"message":"(.*)"')





url = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=17&oid=560233713032161611&sort=2"
head = {
        "User-Agent": " Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 70.0.3538.25 Safari / 537.36Core / 1.70.3877.400 QQBrowser / 10.8.4506.400"
    }
request = urllib.request.Request(url,headers=head)
html = ""
response = urllib.request.urlopen(request)
html = response.read().decode("utf-8")
#print(html)


#pg = re.findall(r'\"replies\":(.+?)\"hots\"',html)
pg2 = re.findall(r'"rpid"：(.+?)"reply_control"',html)
print(pg2)


for item in pg2:
    #print(item)
    i = 0
    data = []

    fname = re.compile(r'"uname":"(.+?)","sex', re.S)
    names = re.findall(fname,item)
    print(names)
    #data.append(names)

    fme = re.compile(r'"content":{"message":"(.+?)","plat')
    mes = re.findall(fme,item)
    #print(mes[i])
    #print(type(mes))
    #data.append(mes)






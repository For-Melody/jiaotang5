# -*- codeing = utf-8 -*-
# @Time : 2021/10/5 14:03
# @Author :
# @File : testitem.py
# @Software : PyCharm


from bs4 import BeautifulSoup
import re
from urllib import request,parse,error
import sqlite3
import urllib
import json
import time,datetime




url = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=17&oid=560233713032161611&sort=2"
head = {
        "User-Agent": " Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 70.0.3538.25 Safari / 537.36Core / 1.70.3877.400 QQBrowser / 10.8.4506.400"
    }
request = urllib.request.Request(url,headers=head)
html = ""
response = urllib.request.urlopen(request)
html = response.read().decode("utf-8")
#print(html)


pg = re.findall(r'\"replies\":(.+?)\"hots\"',html)
#print(pg)
datalist = []

# pg2 = re.findall(r'"rpid"：(.*)"reply_control',html)
# print(pg2)

for item in pg:
    #print(item)
    #item = str(item)

    fname = re.compile(r'"uname":"(.+?)","sex', re.S)
    nam = re.findall(fname,item)
    #print(nam)                                                       #把names当成参数使用导致出错
    #data.append(names)


    fme = re.compile(r'"content":{"message":"(.+?)","plat',re.S)
    mes = re.findall(fme,str(item))
    #print(type(mes))

    #print(mes)
    #print(type(mes))


    flike = re.compile(r'"like":(\d+?),"action')
    like = re.findall(flike,item)
    #print(like)


    ftime = re.compile(r'"ctime":(\d*?),"rpid_str"')
    time_ = re.findall(ftime,item)

    fimg = re.compile(r'"avatar":"(.+?)","rank"')
    img = re.findall(fimg, item)


    fmid = re.compile(r'"mid":"(\d*?)","uname"')
    mid = re.findall(fmid, item)
    #print(len(mid))

    #print(formatTime)


# print(len(mes))
#print(len(nam))
# print(len(like))
# print(len(time_))


for i in range(0,50):
    data = []
    data.append(nam[i])

    data.append(like[i])

    mes[i] = re.sub(r'\\n', " ", str(mes[i]))
    mes[i] = re.sub(r'\\u0026#34;', " ", str(mes[i]))
    data.append(mes[i])


    time1 = int(time_[i])
    timeStamp = time1
    timeArray = time.localtime(timeStamp)
    formatTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    data.append(formatTime)

    mid[i] = "https://space.bilibili.com/" + mid[i] + "?spm_id_from=444.42.0.0"
    data.append(mid[i])

    datalist.append(data)

#print(datalist)

# for i in datalist:
#     print(len(i))
#



















# bilibili = open('bilibili.html','r',encoding='utf-8')
# data = re.findall(r'\"replies\":(.+?)\"hots\"',str(html))[0]

#data = json.dumps(data)
# jsonbg = json.loads(data)
#
# # s=''
# # jsonbg = s.join(jsonbg)
# print(jsonbg)

# for item in jsonbg:
#
#     fname = re.compile(r'\"uname\":"(.+?)",\"sex',re.S)
#     names = re.findall(fname,item)
#     print(names[0])







# datalist = []
# soup = BeautifulSoup(html, "html.parser")
# #print(soup)
#
# for item in soup.find_all():
#     data = []
#     item = str(item)
#     #print(item)
#
# word = html.select('"content":{"message":"')
# print(word)


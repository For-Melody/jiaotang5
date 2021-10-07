# -*- codeing = utf-8 -*-
# @Time : 2021/10/5 12:39
# @Author :
# @File : demo1.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import re
from urllib import request,parse
import sqlite3
import urllib
import time



def main():
    baseurl1 = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=17&oid=560233713032161611&sort=2"
    datalist1 = getData(baseurl1)  #爬取网页
    baseurl2 =  "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=2&type=17&oid=560233713032161611&sort=2"
    datalist2 = getData(baseurl2)
    datalist = datalist1 + datalist2
    #print(datalist)

    dbpath = "嘉然.bd"
    saveData2DB(datalist,dbpath)    #保存数据到sql

    s = input()
    select_db(dbpath,s)


def getData(baseurl):
    datalist = []
    html = askURL(baseurl)
    pg = re.findall(r'\"replies\":(.+?)\"hots\"',html)

    for item in pg:
        fname = re.compile(r'"uname":"(.+?)","sex', re.S)  # 作者
        nam = re.findall(fname, item)


        fme = re.compile(r'"content":{"message":"(.+?)","plat')     #内容
        mes = re.findall(fme, item)



        flike = re.compile(r'"like":(\d+?),"action')            #点赞数
        like = re.findall(flike, item)


        ftime = re.compile(r'"ctime":(\d*?),"rpid_str"')        #时间
        time_ = re.findall(ftime, item)

        fimg = re.compile(r'"avatar":"(.+?)","rank"')
        img = re.findall(fimg,item)

        fmid = re.compile(r'"mid":"(\d*?)","uname"')
        mid = re.findall(fmid,item)


    for i in range(0, 50):
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

        data.append(img[i])
        mid[i] = "https://space.bilibili.com/" + mid[i] + "?spm_id_from=444.42.0.0"
        data.append(mid[i])


        datalist.append(data)
    #print(datalist)
    return datalist





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


#保存数据到数据库中
def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()


    for data in datalist:
        for i in range(len(data)):
            if i == 1:
                continue
            data[i] = '"'+ data[i] + '"'
        sql = '''
                insert into jiaran(
                cname,like,message,time,img,mid)
                values (%s)'''%",".join(data)
        #print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


#建立数据库
def init_db(dbpath):
    sql = '''
        create table jiaran
            (cname varchar  ,
            like numeric ,
            message text ,
            time text,
            img text,
            mid text)
    '''
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()


def select_db(dbpath,s):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    sql = "select message from jiaran "
    cur = c.execute(sql)
    for row in cur:
        #print(row[0])
        if row[0] == s:
            a = 1
            break
        else:
            a = 0
    if a == 1:
        print("存在此评论")
    else:
        print("没有此评论")


    conn.close()


if __name__ == "__main__":
    main()
    print("爬取完毕")


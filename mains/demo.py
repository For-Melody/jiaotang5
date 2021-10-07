# -*- codeing = utf-8 -*-
# @Time : 2021/9/20 20:13
# @Author :
# @File : demo.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import re
from urllib import request,parse
import xlwt
import urllib

def main():
    baseurl = "https://sise.uestc.edu.cn/info/1017/"
    datalist = getData(baseurl)         #爬取网页
    savepath = "信软.xls"
    dbpath = "movie.bd"
    saveData(datalist,savepath)        #保存数据到xls
    #saveData2DB(datalist,dbpath)        #保存数据到sql


findtitle = re.compile(r'<h1 class="content-title">(.*)</h1>')
findtime = re.compile(r'<p class="content-tip">(.*)?<script>',re.S)
findImg = re.compile(r'<img src="(.*?)"',re.S)

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,50):
        url = baseurl + str(i+1011)+".htm"
        html = askURL(url)

        #解析网页
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="list-content content-card"):
            data = []
            item = str(item)

            title = re.findall(findtitle, item)[0]          #提取标题
            data.append(title)

            time = re.findall(findtime, item)[0]            #提取日期
            time = re.findall('\d*', time)[1] + " " + re.findall('\d*', time)[3] + " " + re.findall('\d*', time)[5]
            data.append(time)

            for p in soup.find_all('div',class_="v_news_content"):      #提取内容
                i = p.text
                i = re.sub('\n',' ',i)
                data.append(i)

            imgs = re.findall(findImg,item)             #提取图片
            if(len(imgs)==0):
                data.append(' ')
            else:
                for j in range(0,len(imgs)):
                    img = re.findall(findImg,item)[j]
                    #print(img)
                    data.append(img)

            datalist.append(data)

    #print(datalist)
    return datalist








#得到指定一个url的网页内容
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






#保存数据到els中
def saveData (datalist,savepath):
    print("save")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)       #创建workbook对象
    sheet = book.add_sheet('信软新闻', cell_overwrite_ok=True)
    col = ("标题","日期","内容","图片")
    for i in range(0,4):
        sheet.write(0,i,col[i])
    for i in range(0,50):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0,len(data)):
            sheet.write(i + 1, j, data[j])

    book.save(savepath)






if __name__ == "__main__":
    main()
    print("爬取完毕")



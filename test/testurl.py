# -*- codeing = utf-8 -*-
# @Time : 2021/9/20 20:39
# @Author :
# @File : testurl.py
# @Software : PyCharm

import urllib
from urllib import request

#测试网页是否存在，信息能否爬取


baseurl = "https://sise.uestc.edu.cn/info/1017/"
datalist = []
for i in range(0,1):
    url = baseurl + str(i+1014)+".htm"
    print(url)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4506.400"
    }
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    print(response.read().decode("utf-8"))


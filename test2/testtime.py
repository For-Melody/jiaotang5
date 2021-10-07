# -*- codeing = utf-8 -*-
# @Time : 2021/10/6 20:48
# @Author :
# @File : testtime.py
# @Software : PyCharm

import datetime
import time

# timeStamp = 1624045464
# dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
# otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
# print(otherStyleTime)   # 2013--10--10 15:40:00

a = 1
timeStamp = a
timeArray = time.localtime(timeStamp)
formatTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print (formatTime)





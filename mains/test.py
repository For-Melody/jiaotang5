# -*- codeing = utf-8 -*-
# @Time : 2021/10/7 12:09
# @Author :
# @File : test.py
# @Software : PyCharm

import sqlite3


a = "哈哈哈哈"
b = "哈哈哈哈"
if a == b:
    print("存在此评论")
else:
    print("没有此评论")



# s = input()
# # print(s)
# # print(type(s))
# dbpath = "嘉然.bd"
# conn = sqlite3.connect(dbpath)
# c = conn.cursor()
# sql = "select message from jiaran "
# cur = c.execute(sql)
# print(cur)
#
# # if cur == NULL:
# #     print("没有此评论")
# # else :
# #     print("存在此评论")
# conn.close()

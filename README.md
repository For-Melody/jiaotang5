# 焦糖第五题

* 链接：[github](https://github.com/chynb/jiaotang5)
* 链接中mains文件夹里是完成的代码以及exl表和数据库，test和test文件夹是分别用来测试任务一和任务二代码的，可以忽略

## 1.任务一

> **源码放在mains/demo.py中，创建的exls是信软.xls**

1. 分析

   *在爬取网站中，一共分为三个步骤，分别为爬取网页，提取数据，保存数据。爬取包含获取网页信息与网页的跳转；提取包含提取需要的内容并对其进行整理，去除不必要的内容如\n；保存则是将数据保存在exls中*

2.  使用的库

*  bs4 

* re
* urllib
* xlwt

2. 创建主函数

   ```python
   if __name__ == "__main__":
       main()
       print("爬取完毕")
   ```

3. 创建main函数

   ```python
   def main():
       baseurl = "https://sise.uestc.edu.cn/info/1017/"
       datalist = getData(baseurl)         #爬取网页
       savepath = "信软.xls"
       saveData(datalist,savepath)        #保存数据到xls
   ```

   > 找的网站有差别。。。当时还没更新的时候就做了所以没改，我爬的学院新闻那一块，也询问过学姐可以哟

4. 爬取网页

   ```python
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
   ```

   * 简单的通过request进行伪装，然后做了错误处理，能及时看到出错的原因。本来是想有一个时间timesleep限制的，但是后面想想就算了，毕竟咱们院不可能把自己的学生ip给封了吧？？？（我不会告诉你因为尝试豆瓣把我ip封了23333）  

5. 解析网页

   ```python
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
   ```

   > 新闻之前只改变了网址的某一参数因此能以此规律爬下基本上最近的新闻，在这里我只爬了50条，如果要爬100条只需要把i的循环改为range(0,100)即可    

   我使用的正则提取将图片，内容等等提取出来并将每条新闻的数据保存在列表data中，最后将所有data数据保存在datalist中

   > **try**：期间我最先使用string方法提取span标签里的内容，但每次只能提取到一条文字内容因string提取完第一个标签中的内容便会停止，而网页中整段文字包含多个span标签或者p标签，后找到text方法提取标签内的全部内容才解决了问题

6. 保存数据

   ```python
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
   ```

   最后创建exls表将内容填入即可

   * **下面是结果图**

   > 我实在没想到往哪传图片所以放我个人贴吧里去了，有水印很正常。。。

   ![avatar](https://wx3.sinaimg.cn/mw690/006w6fGHly1gv706iz4t2j612u0ku10w02.jpg)

   **至此任务一就完成了**  

   > 任务一的所有测试代码我都放在test文件夹中，期间我测试了正则提取，reques请求等等，还有现在还没弄懂的scrapy，在爬取中我觉得用xpath可以快速定位到我所需要爬取的地方可惜我的代码写出来运行不了555๐·°(৹˃̵﹏˂̵৹)°·๐俗称写bug

***

## 2.任务一（探索）

在使用F12看了计院官网的内容（含有新闻内容），再对比爬下来的内容（不含新闻信息），应该是设置了动态页面，如果要爬取需要单独抓包爬取（我就一萌新说错了请谅解我(>v<)），最笨的办法就是手动F12把包的地址找到再进行爬取，也许可以用selenium模拟人为操作爬取？没使用过但道理上说应该可行吧hhhh

***

## 3.任务二

> **源码放在mains/demo1中，数据库为嘉然.bd**

1. 分析

   *过程与任务一大致相同，只是不能找原网页的url，而是找js渲染过的url，同样分三步：爬取网页，提取数据，保存数据，只不过后面多出了一个查找有无评论的函数*

2. 使用的库
   * re
   * urllib
   * sqlite3
   * time  

3. 建立主函数

   ```
   if __name__ == "__main__":
       main()
       print("爬取完毕")
   ```

4. 创建main函数

   ```
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
   ```

   > 因一页的评论不足100条所以我爬取了两页，懒得写在爬取网页里面了，干脆就爬取两个网页的内容然后将数据合并，所以看着有些繁琐，但基本思路和任务一区别不大

5. 爬取网页

   ```
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
   ```

6. 解析网页

   ```python
   def getData(baseurl):
       datalist = []
       html = askURL(baseurl)
       pg = re.findall(r'\"replies\":(.+?)\"hots\"',html)
   
       for item in pg:
           fname = re.compile(r'"uname":"(.+?)","sex', re.S)  		#作者
           nam = re.findall(fname, item)
   
   
           fme = re.compile(r'"content":{"message":"(.+?)","plat')     #内容
           mes = re.findall(fme, item)
   
   
   
           flike = re.compile(r'"like":(\d+?),"action')            #点赞数
           like = re.findall(flike, item)
   
   
           ftime = re.compile(r'"ctime":(\d*?),"rpid_str"')        #时间
           time_ = re.findall(ftime, item)
   
           fimg = re.compile(r'"avatar":"(.+?)","rank"')			#头像
           img = re.findall(fimg,item)
   
           fmid = re.compile(r'"mid":"(\d*?)","uname"')			#空间链接
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
   ```

   * 这里不同于任务一的是re.find_all在item中找的是所有的符合正则表达式的数据，其实item就是pg（网页数据），所以跟任务一可以用循环不同，这里要单独用一个for循环将re.find_all生成的列表中的每个元素提取出来。

   * **时间戳**：时间戳被提取后还需要另外解析才能得到时间，一开始找的是mtime所以一直不对，直到找到ctime才发现自己找错了，时间戳是用秒来反应时间，时间是从1970-01-01T00:00:00开始（因为解析timeStamp=0出来的结果就是这个时间），同时需要注意时间戳要用整形参数所以需要强制类型转换

   > **bug**：在这个函数中我忘记提取网页信息也就是没有使用askUrl函数导致运行时系统报错：local variable "name" referenced before assignment,然后我查了一下发现基本上报这个错误都是全局变量局部引用导致的，要解决需要加上global，而我在这里的变量并不是全局变量，在之前的所有代码中也没有出现关键字“name”，但却报了这个错，具体原因我现在还是不太了解

7. 保存数据

   1. 建立数据库

      ```python
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
      ```

      * 我使用sql创建的数据库，其中包含作者，点赞数，内容，时间，头像，空间链接。

        > **bug**：最开始我将cname设置成关键词并不能为空，即：
        >
        > cname varchar primary key not null
        >
        > 但运行后报错找不到cname，将后缀删掉后就恢复正常，我想应该是在爬取的数据中可能存在空的情况从而与not null冲突而报错

   2. 将数据存储到数据库中

      ```python
      def saveData2DB(datalist,dbpath):
          init_db(dbpath)
          conn = sqlite3.connect(dbpath)
          cur = conn.cursor()
      
      
          for data in datalist:
              for i in range(len(data)):
                  if i == 1:				#like为numeric，不需要加双引号
                      continue
                  data[i] = '"'+ data[i] + '"'			
              sql = '''
                          insert into jiaran(
                          name,like,message,time)
                          values (%s)'''%",".join(data)
              #print(sql)
              cur.execute(sql)
              conn.commit()
          cur.close()
          conn.close()
      ```

      > **bug**：开始时在数据库中定义数据类型时cname为varchar，message、time等为text，但在数据存储过程中并未加上“（双引号）导致报错：
      >
      > sqlite3.OperationalError: near "@嘉然今天吃什么": syntax error
      >
      > 加上后程序正常。
      >
      > 学到了在数据库出错时可以将sql单独打印查看问题或将一条sql直接插入数据库查看问题，先不进行数据的上传，从而快速找到出错的地方

8. 查找数据

   ```python
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
   ```

   * 在数据的查找中我用的笨办法直接将所有评论提取出来再挨个比对

     > **try**：我使用过LIKE对数据进行查找：
     >
     > select message from jiaran LIKE 's%'
     >
     > 但运行时间溢出且无任何结果，不知道错在哪里（虽然LIKE可以模糊查询，但是我认为如果要查找的内容是确定的，用LIKE就相当于全匹配，应该算是一种特殊情况吧）
     >
     > 后我又使用WHERE进行查找：
     >
     > select message from jiaran WHERE message == 's'
     >
     > 出现与LIKE一样的问题，不知道错误在哪，所以只好使用笨一点的方法

**至此任务二就完成了**

* **下面是结果图**

![avatar](https://wx4.sinaimg.cn/mw690/006w6fGHly1gv706i8gmkj61hc0smu0x02.jpg)



**希望我这个弱渣也能加入焦糖这个大佬云集的地方啦！ヽ(✿ﾟ▽ﾟ)ノ**

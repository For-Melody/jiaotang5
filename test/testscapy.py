# -*- codeing = utf-8 -*-
# @Time : 2021/9/21 13:30
# @Author :
# @File : testscapy.py
# @Software : PyCharm

# -*- coding: utf-8 -*-
import scrapy


class TbspiderSpider(scrapy.Spider):
    name = 'tbSpider'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/p/5702862812?pn=1']

    def parse(self, response):
        # 找到包含每一页的完整内容的标签
        page = response.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')
        # 遍历找到的标签
        for content in page:
            # 找到每一楼的文本内容,最后放在一个列表中
            content_list = content.xpath('.//div[@class="d_post_content j_d_post_content "]').extract()
            print('/**********---------++++++++++++++*******/-------------')
            print(content_list)


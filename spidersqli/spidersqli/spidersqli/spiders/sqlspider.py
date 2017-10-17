# -*- coding: utf-8 -*-
import scrapy
from spidersqli.items import SpidersqliItem
from bs4 import BeautifulSoup
import re
from tld import get_tld


class SqlspiderSpider(scrapy.Spider):
    targets = []
    with open("domain.txt") as f:
        tmps = f.readlines()
    name = "sqlspider"
    for tmp in tmps:
        tmp = re.sub('\s?', '', tmp)
        targets.append(tmp)
        # allower_domains = [re.sub('http://|https://', "", url)]

    # allowed_domains = ["njszb.com", "ruijiesoft.com"]
    # start_urls = [re.sub('\\n', '', url) for url in urls]
    print targets
    start_urls = ['%s' % target for target in targets]

    # def parse(self, response):
    #     item = SpidersqliItem()
    #     """parse"""
    #     if not hasattr(response, 'xpath'):
    #         return
    #     for url in response.xpath('//*[@href]/@href').extract():
    #         url = response.urljoin(url)  # 转化成绝对路径
    #         yield scrapy.Request(url)
    #         if '=' in url and 'mailto:' not in url and '.css' not in url and '.png' not in url and '.jpg' not in url \
    #                 and 'javascript:' not in url and "tree.TreeTempUrl" not in url and '?' in url:
    #             item['url'] = url
    #             yield item

    def parse(self, response):
        print "[$$$]  " + response.url
        domain = response.url
        # print '-' * 50
        # print 'response:  ' + domain
        # print "-" * 50
        urls = []
        item = SpidersqliItem()
        item['host'] = domain
        soup = BeautifulSoup(response.body, 'lxml')
        links = soup.findAll('a')
        for link in links:
            # 获得了目标的url但还需要处理
            _url = link.get('href')
            # print "-" * 50
            # print type(_url)
            # print _url
            # print "-" * 50
            # 接着对其进行判断处理
            # 先判断它是否是无意义字符开头以及是否为None值
            # 判断URL后缀,不是列表的不抓取
            if _url is None or re.match('^(javascript|:;|#)', _url) or re.match('.(jpg|png|bmp|mp3|wma|wmv|gz|zip|rar|iso|pdf|txt|db)$', _url):
                continue
            # 然后判断它是不是http|https开头,对于这些开头的都要判断是否是本站点， 不做超出站点的爬虫
            if '=' in _url and '?' in _url:
                if re.match('^(http|https)', _url):
                    if get_tld(_url) in domain:
                        urls.append(_url)
                else:
                    urls.append(domain + '/' + _url)
        # for url_ in urls:
        #     yield scrapy.Request(url_)
        # yield scrapy.Request(url_ for url_ in urls)
        item['url'] = urls
        # print "=" * 50
        # print item
        # print "=" * 50
        yield item

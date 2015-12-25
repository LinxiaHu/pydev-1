# coding:utf-8
'''
Created on 2015 12月

@author: Chunyun
'''

import math
import numpy as np
import urllib as u1
import urllib2 as u2
import re


# print '中国'

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def speak(self, word):
        print 'Hello:%s' % word
        
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
    
# 百度贴吧爬虫类
class BDTB:
    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
 
    # 传入页码，获取该页帖子的代码
    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = u2.Request(url)
            response = u2.urlopen(request)
            print response.read()
            return response
        except u2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败,错误原因", e.reason
                return None
 

# 图片抓取类（taobao)
class SpiderTaobao:
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
 
    def getPage(self, pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print url
        request = u2.Request(url)
        response = u2.urlopen(request)
        return response.read().decode('gbk')
 
    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, page)
        for item in items:
            print item[0], item[1], item[2], item[3], item[4]



if __name__ == '__main__':
#     dalt = math.pi / 3
#     cos1 = math.cos(dalt)
#     print cos1
#     
#     array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#     print array
#     
#     p1 = Person('tengfei', 3)
#     p2 = Person('zhangsan', 9)
#     a = []
#     a.append('a')
#     a.append('b')
#     a.append('c')
#     a.append(p1)
#     a.append(p2)
#     print a
#     p1.speak('xiaowang')
#     p2.speak('word')
#     p1.speak('jfiejf')
#     p1age = p1.getAge()
#     p2age = p2.getAge()
#     print 'p1的年龄是：%s' % p1age
#     print 'p2的年龄是：%s' % p2age
    
    # urllib的使用测试
#     values = {}
#     values['username'] = "1016903103@qq.com"
#     values['password'] = "XXXX"
#     data = u1.urlencode(values) 
#     url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
#     request = u2.Request(url, data)  # post方式请求
#     response = u2.urlopen(request)
#     print response.read()
    
    # 贴吧测试
#     baseURL = 'http://tieba.baidu.com/p/3138733512'
#     bdtb = BDTB(baseURL, 1)
#     bdtb.getPage(1)

    # 异常测试
#     req = u2.Request('http://blog.csdn.net/cqcre')
#     try:
#         u2.urlopen(req)
#     except u2.HTTPError, e:
#         print e.code
#         print e.reason
        
        
    # 加入判断   
#     req = u2.Request('http://blog.csdn.net/cqcre')
#     try:
#         u2.urlopen(req)
#     except u2.URLError, e:
#         if hasattr(e, "code"):
#             print e.code
#         if hasattr(e, "reason"):
#             print e.reason
#     else:
#         print "OK"
        
    
    # 淘宝图片抓取测试
    spider = SpiderTaobao()
    spider.getContents(1)








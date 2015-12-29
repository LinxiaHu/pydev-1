#coding:utf-8
'''
Created on 2015年12月25日

@author: Chunyun
'''

import re

a1 = '<tr id="k"></tr>'
partter1 = re.compile(r'<tr.*', re.S)
ma1 = partter1.match(a1)
print ma1.group() #匹配的字串
print ma1.span() #匹配的范围
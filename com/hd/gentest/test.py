#coding:utf-8
'''
Created on 2015 12月

@author: Chunyun
'''

import math
import numpy as np



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

if __name__ == '__main__':
    dalt = math.pi / 3
    cos1 = math.cos(dalt)
    print cos1
    
    array = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print array
    
    p1 = Person('tengfei', 3)
    p2 = Person('zhangsan', 9)
    a = []
    a.append('a')
    a.append('b')
    a.append('c')
    a.append(p1)
    a.append(p2)
    print a
    p1.speak('xiaowang')
    p2.speak('word')
    p1.speak('jfiejf')
    p1age = p1.getAge()
    p2age = p2.getAge()
    print 'p1的年龄是：%s' % p1age
    print 'p2的年龄是：%s' % p2age


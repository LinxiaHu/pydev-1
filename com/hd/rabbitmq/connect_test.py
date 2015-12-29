#coding:utf-8
'''
Created on 2015.12.29

@author: Chunyun
'''
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.206.129'))
print connection


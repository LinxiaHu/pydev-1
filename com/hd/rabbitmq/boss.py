# coding:utf-8
'''
Created on 2015.12.29

@author: Chunyun
'''
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.206.129'))
# print connection

channel = connection.channel()
# 创建名字为test的queue,然后可以在server上sudo rabbitmqctl list_queues来查看这个queue
channel.queue_declare(queue='queue-1')

message = ' '.join(sys.argv[1:]) or "Hello World!"  
channel.basic_publish(exchange='',  
                      routing_key='queue-1',  
                      body=message,  
                      properties=pika.BasicProperties(  
                         delivery_mode = 2, # make message persistent  
                      ))  
print " [queue-1] Sent %r" % message 
connection.close()
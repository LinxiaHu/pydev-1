#coding:utf-8
'''
Created on 2015.12.29
@author: Chunyun
'''
import pika
import time


connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.206.129'))
channel = connection.channel()
# 创建名字为test的queue,然后可以在server上sudo rabbitmqctl list_queues来查看这个queue
channel.queue_declare(queue='queue-1', durable=True)  
print ' [*] Waiting for messages. To exit press CTRL+C'  
  
def callback(ch, method, properties, body):  
    print " [test] Received %r" % (body,)  
    time.sleep( body.count('.') )  
    print " [test] Done"  
    ch.basic_ack(delivery_tag = method.delivery_tag)  
# 通过 basic.qos 方法设置prefetch_count=1 ,这样RabbitMQ就会使
# 得每个Consumer在同一个时间点最多处理一个Message,
# 换句话说，在接收到该Consumer的ack前，他它不会将新的Message分发给它  
# 注意，这种方法可能会导致queue满。当然，这种情况下你可能需要添加更多
# 的Consumer，或者创建更多的virtualHost来细化设计
channel.basic_qos(prefetch_count=1)  
channel.basic_consume(callback,  
                      queue='queue-1')  
  
channel.start_consuming()
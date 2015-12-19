# coding:utf-8
import MySQLdb as db

# print "hello,中国"
# 数据库连接
conn = db.Connect(host='127.0.0.1',
                  port=3306,
                  user='root',
                  passwd='125885',
                  db='goods',
                  charset='utf8'
                   )

curser = conn.cursor()

print curser
print conn

curser.close()
conn.close()

# coding:utf-8
import MySQLdb as db
  
print "hello,中国"
# 数据库连接
conn = db.Connect(host='127.0.0.1',
                port=3306,
                user='root',
                passwd='123456',
                db='goods',
                charset='utf8'
                )
 
curser = conn.cursor()
 
sql = "select uid, loginname from t_user"
curser.execute(sql)
print curser.rowcount
rs = curser.fetchone()
print rs
  
rs = curser.fetchall()
print rs
for row in rs:
    print "userid = %s, loginname = %s" % row
 
 
print curser
print conn
 
curser.close()
conn.close()

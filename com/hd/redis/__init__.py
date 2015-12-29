import redis
import psutil


connection = redis.StrictRedis(host='192.168.206.129', port=6379, db=0)
print connection
# connection.sadd("set1", "apple");
print connection.smembers("set1")
# connection.bgsave()
print psutil.cpu_times();
# importing library
import redis

# creating an Redis instance
r = redis.Redis(host='localhost', port=6379, db=0)

# simple list
r.lpush('L001', 'a','b','c')

print("List contents: ", r.lrange('L001',0,-1))
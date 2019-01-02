# importing library
import redis

# creating an Redis instance
r = redis.Redis(host='localhost', port=6379, db=0)

# clearing the keys before creating them
r.delete('L001','L002','L003')

# simple list
r.lpush('L001', 'a','b','c')

print("List contents: ", r.lrange('L001',0,-1))

r.rpush('L001', 'd')
print("Inserted from right: ", r.lrange('L001',0,-1))
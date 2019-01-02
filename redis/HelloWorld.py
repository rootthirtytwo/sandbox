# importing library
import redis

# creating an Redis instance
r = redis.Redis(host='localhost', port=6379, db=0)

# creating an key value pair
r.set('hello','world')

# print the value of the key
print(r.get('hello'))

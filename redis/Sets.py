# importing library
import redis

# creating an Redis instance
r = redis.Redis(host='localhost', port=6379, db=0)

# creating a simple set
r.sadd('SET001','a','b', 'c')

# print the length of the set
print("Length of the string: ",r.scard('SET001'))

print("Set members: ", r.smembers('SET001'))
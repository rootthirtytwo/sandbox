# importing library
import redis

# creating an Redis instance
r = redis.Redis(host='localhost', port=6379, db=0)

# creating a simple set
r.sadd('ST001','a','b', 'c')

# print the length of the set
print("Length of the stri/ng: ",r.scard('ST001'))

# members of the set
print("Members of ST001 ", r.smembers('ST001'))

# creating second set
r.sadd('ST002', 'b','c', 'd')
print("Members of ST002 ", r.smembers('ST001'))

# intersect explained
print("Set intersect between ST001 and ST002 ", r.sinter('ST001', 'ST002'))

# union explained
print("Set union between ST001 and ST002 ", r.sunion('ST001', 'ST002'))

# diff explained
print("Set difference between ST001 and ST002 ", r.sdiff('ST001', 'ST002'))

# ismember explained, if it a member it returns True or else False
print("'a' is member of ST001  ", r.sismember("ST001", 'a'))
print("'a' is member of ST002  ", r.sismember("ST002", 'a'))

# moving member from one set to another
print("Move 'a' from ST001 to ST002..")
r.smove("ST001", 'ST002', 'a')
print(r.smembers('ST001'))
print(r.smembers('ST002'))

# pop one item from set
r.spop('ST001')
print("After pop one item from set ST001", r.smembers('ST001'))

# removing specific member from set

r.srem('ST002', 'a')
print("remove 'a' from set ST002", r.smembers("ST002"))

#Usage of scan
print(r.sscan("ST002",0,'b', 1))

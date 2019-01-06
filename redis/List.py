# importing library
import redis

# creating an Redis instance
r = redis.Redis(host='localhost', port=6379, db=0)

r.delete('L001')

# simple list
r.lpush('L001', 'a','b','c', 'l1','l2')
print("List contents: ", r.lrange('L001',0,-1))

r.rpush('L001', 'd')
print("Inserted from right: ", r.lrange('L001',0,-1))

# remove single right most entry
r.rpop('L001')
print("After RPOP: ", r.lrange('L001',0,-1))

# remove single left most entry
r.lpop('L001')
print("After LPOP: ", r.lrange('L001',0,-1))

# length of the list
print("Length of L001 ", r.llen('L001'))

# LINDEX explained
print("2nd position of the list L001 ", r.lindex('L001', 1))

print("List: ", r.lrange('L001',0,-1))

print("POPS right most element and returns the item deleted ", r.brpop('L001'))
print("POPS left most element and returns the item deleted ", r.blpop('L001'))

# Pops right most item and pushes that to left side of the list
r.brpoplpush('L001','L001')
print("List: ", r.lrange('L001',0,-1))


# inserting after / before an item
r.linsert('L001', "After",  "c", "Ac")
print("List: ", r.lrange('L001',0,-1))

r.linsert('L001', "Before",  "b", "Bb")
print("List: ", r.lrange('L001',0,-1))

r.lset('L001',2,'Indexed Item')
print("List: ", r.lrange('L001',0,-1))

# removes an item from list and we can pass the count to remove that many occurrences
r.lpush('L001', 'b')
print("List: ", r.lrange('L001',0,-1))
r.lrem('L001', 2, 'b' )
print("List: ", r.lrange('L001',0,-1))

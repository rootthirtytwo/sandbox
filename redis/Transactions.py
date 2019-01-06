# importing library
import redis

# creating an Redis instance
r = redis.Redis(host='localhost', port=6379, db=0)

# initiate the transaction which is equivalent to "MULTI"
p = r.pipeline()

p.set('SET001', 'test 004')

# execute the queue, which is equivalent to EXEC
p.execute()


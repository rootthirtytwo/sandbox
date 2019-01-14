import redis

r = redis.Redis(host="localhost", port=6379, db=0)

r.flushall()

#ZADD & ZRANGE explained
r.zadd("ss01",{"a":1, "b":2,"c":1, "d":4})
r.zadd("ss02",{"a":100, "b":200,"c":150, "d":400})
print("Contents in ss01 ",r.zrange("ss01",0,-1, withscores=True))
print("Contents in ss02 ",r.zrange("ss02",0,-1, withscores=True))

#ZCARD explained
print("\nLength of ss01 ", r.zcard("ss01"))

#ZINCRBY explained
r.zincrby("ss02", 10, "b")
print("\nContents in ss02 ",r.zrange("ss02",0,-1, withscores=True))


import redis

r = redis.Redis(host="localhost", port=6379)

r.flushall()

#HSET & HGET explained
data = {"name": "kevin"}
r.hset("hashkey001", "name", "kevin")
print("HSET Result ", r.hget("hashkey001", "name"))

#HMSET & HGETALL explained
data = {"name": "John", "age":34, "salary":95000.99, "IsMale":"Ture", "place":"Chicago", "married":"Yes"}
r.hmset('hashkey002', data)
print("HMSET Result ", r.hgetall("hashkey002"))

# HINCRBY explained
print("\nAge before ", r.hget("hashkey002", "age"))
r.hincrby("hashkey002","age", 2)
print("Age after increase by 2 ", r.hget("hashkey002", "age"))

# HINCRBYFLOAT explained
print("\nSalary before ", r.hget("hashkey002", "salary"))
r.hincrbyfloat("hashkey002","salary", 10000)
print("Salary after increase by 10000  ", r.hget("hashkey002", "salary"))

# HEXISTS explained
print("\nname is available in hashkey001", r.hexists("hashkey001", "name"))
print("age is available in hashkey001", r.hexists("hashkey001", "age"))

#HKEYS & HVALS explained
print("\nList all the keys of hashkey002 ", r.hkeys("hashkey002"))
print("List all the values of hashkey002 keys('name', 'age', 'salary','IsMale') ", r.hvals("hashkey002"))

#HDEL explained
r.hdel("hashkey002","married", "place")
print("\nValues after removing 'married' and 'place' keys", r.hgetall("hashkey002") )

#HLEN explained
print("\nLength of hashkey002 ", r.hlen("hashkey002"))

#HSETNX explained ( Set the value is the key not exists )
r.hsetnx("hashkey001", "age", 26)
print("Added key age to hashkey001 ", r.hgetall("hashkey001"))

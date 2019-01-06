# importing library
import redis
import time

# creating an Redis instance
r = redis.Redis(host='localhost', port=6379, db=0)

# clearing the keys before creating them
r.delete('S001','S002','S003', 'S004')

# creating an key value pair
r.set('S001','1')

# print the value of the given key
print("Initial value: ",r.get('S001')) #returns 1

# increment value
r.incr('S001', 10)
print("After increasing by 10 : ",r.get('S001')) #returns 1


# decrease value
r.decr('S001', 5)
print("After decreasing by 5 : ",r.get('S001')) #returns 1

# setting an expiration time
print("\n************** SETTING EXPIRATION **************", sep='\n')
r.set('S001','hi S001', ex=5) # ex = in sec, ps = in milli-sec
print("Print value of S001: ",r.get('S001'))
print("sleep for 5sec.....")
time.sleep(5)
print("Check value now: ",r.get('S001'))

# experimenting with EXISTS(XX) and NOT-EXISTS(NX)
print("\n************** EXISTS / NON-EXISTS **************", sep='\n')
r.set('S001','Hi again',nx=True) # if not exists then create, so it prints 6
r.set('S002',"Hello I'm new",nx=True)
print("S001(nx=True) value is ",r.get('S001'))
print("S002(nx=True) value is ",r.get('S002'))

r.set('S001','Hi Again',nx=False) # if exists then update, so it prints Hi Again
print("S001(nx=False) value is ",r.get('S001'))

r.set('S001','Hello',xx=False) # if exists then update, so it prints Hi Again
print("S001(xx=False) value is ",r.get('S001'))

r.set('S001','Hellooo',xx=True) # if exists then update, so it prints Hi Again
print("S001(xx=True) value is ",r.get('S001'))

r.set('S003','hi',xx=True) # if exists then update, so it prints Hi Again
print("S003(xx=True) value is ",r.get('S003'))

r.set('S003','hi',xx=False) # if exists then update, so it prints Hi Again
print("S003(xx=False) value is ",r.get('S003'))

# Append explained
r.set('S004', 'Hi')
print("Before Append S004 ", r.get('S004'))
r.append('S004', ' Redis')
print("Append 'Redis' to S004 ",r.get('S004'))


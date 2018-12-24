import numpy as np
from itertools import chain, repeat, cycle
# simple iteration
for i in range(5):
    print(i)

# dict
d = {'a':1, 'b':2, 'c':3}
for k in d:
    print(k)

for k,v in d.items():
    print("{0}->{1}".format(k,v))


# file
# with open("filename.txt", 'r') as f:
#     for ln in f:
#         print(repr(ln))

#list
l = ['a','b']
for n,v in enumerate(l):
    print("{0}->{1}".format(n,v))

# zip
name = ['USA', 'India', 'Australia']
code = [1, 91, 61]

for n, c in zip(name, code):
    print("Area code for {0} is +{1}".format(n,c))

# customization
nums = [88,73,92,72,40,38,35,20,90,72]


#generator
def hello_world():
    yield "hello"
    yield "world"

for x in hello_world():
    print(x)

#print evens
def evenes(num):
    for n in num:
        if n % 2 ==0:
            yield n

for n in evenes(nums):
    print(n)

#sorting
place = ['USA', 'INDIA', 'CANADA','QATAR']

print(sorted(place,key=len))


# dict construction
colors = ['red','green','red','blue','green','red']

d ={}

for color in colors:
    d[color] = d.get(color, 0)+1

print(d)






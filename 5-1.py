import random
import math

arr=[]
n=int(input("Input size of arr  "))
for i in range(n):
    arr.append(random.randint(-10,10))

print arr

s=0
for i in range(n):
    s=s+arr[i]

print 'Sum ',s

m=0
m=float(m)
for i in range(n):
    m=m*float(arr[i])

print 'Mult ',m
sq=0
sq = float(sq)
s=0
s = float(s)

for i in range(n):
    s=float(arr[i])

    sq=sq+math.sqrt(float(s))


print 'Sum of square ',sq

import random

arr=[]
n=int(input("Input size of arr  "))
for i in range(n):
    arr.append(random.randint(-10,10))

print arr

minn=999
mn=0
for i in range(n):
    if arr[i]<minn:
        minn=arr[i]
        mn=i

print 'Min ',minn,mn

maxx=-999
mx=0
for i in range(n):
    if arr[i]>maxx:
        maxx=arr[i]
        mx=i
        
print 'Max ',maxx,mx
s=0
if mx > mn:
    for i in range(mn,mx+1):
        s=s+arr[i]

if mn > mx:
    for i in range(mx,mn+1):
        s=s+arr[i]


print s

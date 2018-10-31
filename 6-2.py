import random

arr=[]
rr=[]
xx=[]


n=int(input("Input size of arr  "))

a=0
b=0
for i in range(n):
    arr.append(random.randint(-10,10))
print arr

for i in range(n):
    if arr[i]>0:
        rr.append(arr[i])
        a=a+1
    else:
        xx.append(arr[i])
        b=b+1


print rr
print xx



for i in range(a):
    xx.append(rr[i])
    
print rr
print xx

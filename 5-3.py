import random
import math

arr=[]

rr=[]
n=int(input("Input size of arr  "))
for i in range(n):
    arr.append(random.randint(10,99))

print arr


k=int(input("Input k "))


for i in range(n):
    if arr[i]%10==k:
        rr.append(arr[i])

print rr

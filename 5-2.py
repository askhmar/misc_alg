import random
import math

arr=[]
n=int(input("Input size of arr  "))
for i in range(n):
    arr.append(random.randint(-10,10))

print arr



s=0
for i in range(n-1):
    if arr[i+1]<arr[i]:
        print arr[i+1],i
        break


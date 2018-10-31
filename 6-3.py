import random

arr=[]

#n=int(input("Input size of arr  "))

n=10


for i in range(n):
    arr.append(random.randint(-10,10))

print arr


for j in range(n):
    for i in range(n-1):
        if (arr[i+1]<0):
            if arr[i]>=0:
                a=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=a

        
 
print arr        
        

import random

arr=[]
n=int(input("Input size of arr  "))
for i in range(n):
    arr.append(random.randint(1,10))

print arr


a=0

for i in range(n-1):
    if (arr[i]%2==0)and(arr[i+1]%2==0):
        print 'Even numbers ',arr[i],arr[i+1]
        for i in range(a,i):
            print arr[i]
            a=i+3

if a==0:
    print 'No even numbers '

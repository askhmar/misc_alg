import random

arr=[]
n=int(input("Input size of arr  "))
for i in range(n):
    arr.append(random.randint(1,10))

print arr

for i in range(n):
    arr[i]=arr[i]-20

print 'Arr minus 20 '
print arr

a=arr[n-1]
for i in range(n):
    arr[i]=arr[i]*n

print 'Arr multiply 20 '
print arr
    


b=int(input("Input B "))

for i in range(n):
    arr[i]=arr[i]+b

print 'Arr add B '
print arr

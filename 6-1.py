import random

arr=[]

while 1>0:
    n=int(input("Input size of arr bigger 6 "))
    if n>6:
        break
    else:
        print('Error of input ')

for i in range(n):
    arr.append(random.randint(1,10))
print arr

while 1>0:
    k1=int(input("Input k1 "))
    k2=int(input("Input k2 "))
    if (k1<k2)and(k2<=n)and(k1>0):
        break
    else:
        print('Error of input ')

a=0
for i in range(k1,k2+1):
    a=a+arr[i]
print 'Sum of between k1 k2 ',a

a=0
for i in range(n):
    a=a+arr[i]

print 'Sum of arr ',a
a=a/(n+1)

print 'Middle of arr ',a


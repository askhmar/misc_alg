a=int(input("Input number "))
n=0
while a>0:
        d= a % 10
        a=a-d
        a= a // 10
        n=n*10+d
     
print "reverse ", n

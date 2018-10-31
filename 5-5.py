a=int(input("Input number "))
n=0
s=0
d=0
while a!=1:
        if (a%2)==0:
                a=a/2
                d=d+1
        else:
                a=a*3+1
                a=a/2
                n=n+1
                
        s=s+1
     
print "All Steps ", s
print "Divide ", d
print "not Divide ", n

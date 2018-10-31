a = input("a: ")
a = int(a)



d1= a % 10

d11= a // 10

d111= a // 100

d11=d11-d111*10

d1=d1*100

d11=d11*10

d111=d1+d11+d111

print "reverse ", d111

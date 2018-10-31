a = input("a: ")
a = int(a)


b = input("b: ")
b = int(b)


d1= a % 10

d11= a // 10

d111= a // 100

d11=d11-d111*10



print d1
print d11
print d111

dd1= b % 10

dd11= b // 10

dd111= b // 100

dd11=dd11-dd111*10


d2 = d1+d11+d111+dd1+dd11+dd111

d3 = (d1+d11+d111)-(dd1+dd11+dd111)

d4= d1*d11*d111*dd1*dd11*dd111

d5= (d1+d11+d111)/(dd1+dd11+dd111)

print "sum: ",d2
print "dec: ",d3
print "mult: ",d4
print "div: ",d5

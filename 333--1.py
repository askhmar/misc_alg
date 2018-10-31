a = input("a: ")
a = int(a)

b = input("b: ")
b = int(b)



d1= a % 10

d2= a // 10

d3= a // 100

d2=d2-d3*10



dd1= b % 10

dd2= b // 10

dd3= b // 100

dd2=dd2-dd3*10


print "reverse a: ", d1*100+d2*10+d3
print "reverse b: ", dd1*100+dd2*10+dd3

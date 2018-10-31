a = input("a: ")
a = int(a)



d1= a % 10

d2= a // 10

d3= a // 100

d2=d2-d3*10





print "1: ", d1*100+d2*10+d3
print "2: ", d2*100+d3*10+d1
print "3: ", d2*100+d1*10+d3
print "4: ", d1*100+d3*10+d2
print "5: ", d3*100+d1*10+d2
print "6: ", a
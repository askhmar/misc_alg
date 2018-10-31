import math
x1 = input("x1: ")
x1 = float(x1)

y1 = input("y1: ")
y1 = float(y1)

x2 = input("x2: ")
x2 = float(x2)

y2 = input("y2: ")
y2 = float(y2)

x3 = input("x3: ")
x3 = float(x3)

y3 = input("y3: ")
y3 = float(y3)


ab=math.sqrt((math.pow((x2-x1),2)+math.pow((y2-y1),2)))

bc=math.sqrt((math.pow((x3-x2),2)+math.pow((y3-y2),2)))

ac=math.sqrt((math.pow((x1-x3),2)+math.pow((y1-y3),2)))

p=ab+bc+ac

print "perimetr: ",p

p=p/2

p=math.sqrt((p*(p-ab)*(p-bc)*(p-ac)))

print "square: ",p

import math
a = input("inp a  : ")
a=float(a)
b = input("inp b  : ")
b=float(b)
c = input("inp c  : ")
c=float(c)

p=1
p=(a+b+c)
p=float(p)
p=p/2

p=p*(p-a)*(p-b)*(p-c)

s = math.sqrt(p)

ha=1
hb=1
hc=1
ha=float(ha)
hb=float(hb)
hc=float(hc)

ha=(2*s)/a
hb=(2*s)/b
hc=(2*s)/c

print "h a=",ha
print "h b=",hb
print "h c=",hc

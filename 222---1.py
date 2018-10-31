import math


print  "1)"
#-------A

x=input("x ")
y=input("y ")
z=input("z ")

print "a=",(math.sqrt(math.fabs(x-1)) -  math.pow(math.fabs(y),-3))/(1+(math.pow(x,2))/2+(math.pow(y,2))/4)

print "b= ",x*(math.atan(z)+math.exp(-(x+3)))


print  "2)"
#-------B

x=input("x ")
y=input("y ")

print "a= ",(3+math.exp(y-1))/(1+math.pow(x,2)*math.fabs(y-math.tan(z)))

print  "b= ",1+math.fabs(y-x)+(math.pow(y-x,2))/2+(math.pow(math.fabs(y-x),3)/3)

print  "3)"
#-------V


x=input("x ")
y=input("y ")


print "a= ",(1+y)*(((x+y)/(math.pow(x,2)+4))/((math.exp(-x-2)+1)/(math.pow(x,2)+4)))

print "b= ",(1+math.cos(y-2))/(math.pow(x,4)/2+math.pow(math.sin(z),2))


print  "4)"
#-------V


x=input("x ")
y=input("y ")
z=input("z ")


print "a= ",y+x/(math.pow(y,2)+math.fabs(math.pow(x,2)/(y+math.pow(x,3)/3)))

a=1+math.pow(math.tan(z/2),2)
print "b= ",a


print  "5)"
#-------D

x=input("x ")
y=input("y ")
a=2*math.cos(x-((math.pi)/6))

b=1/2+math.pow((math.sin(y)),2)
   
a=a/b
print "a= ",a

print "b= ",1+math.pow(z,2)/(3+math.pow(z,2)/5)


print  "6)"
#-------E

x=input("x ")
y=input("y ")


print "a= ",(1+math.pow(math.sin(x+y),2))/(2+math.fabs(x-2*x/(1+math.pow(x,2)*math.pow(y,2))))+x

print "b= ",math.pow(math.cos(math.atan(1/z)),2)


print  "7)"
#----------Z

x=input("x ")
y=input("y ")
z=input("z ")

a=y-math.sqrt(math.fabs(x))
b=x-(y/(z+math.pow(x,2)/4))

a=math.log(math.fabs(a*b))

print "a= ",a

print "b= ",x-math.pow(x,2)/math.factorial(3)+math.pow(x,5)/math.factorial(5)

import math
n=int(input("Input number "))
i=1

s=int(math.ceil(math.sqrt(n)))

for i in range(s):
        for j in range(s):
                if ((i+1)*(j+1))<=n:
                        print i+1," * ",j+1," = ", (i+1)*(j+1)


import math
s=0
y=int(input('Entre com um expoente inteiro: '))
for x in range(0,100):
    s+= ((y**x)/math.factorial(x))
print(s)

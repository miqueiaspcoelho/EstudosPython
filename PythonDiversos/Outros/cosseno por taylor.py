import math
b=0
i=0
d=40
for x in range (0,200):
    b=b+((-1)**x)*((d**(2*x))/math.factorial(2*x))
    c=((-1)**x)*((d**(2*x))/math.factorial(2*x))
    i+=1
    print('b',b)
    if abs(c) < (10**-9):
        break
print('erro=',c)
print('cosseno=',b)
print('iterações=',i)
    
    

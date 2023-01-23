import math
a=0.5
b=1
aa=a
bb=b

fa=a**2 + math.log(a)
fb=b**2 + math.log(b)
fx=1

if (fa*fb<0):
    while (abs(fx)>0.05):
        
        x=(a+b)/2
        fx=x**2 + math.log(x)
        if (abs(fx) > 0.05 and fx>0):
            b=x
        if (abs(fx) > 0.05 and fx<0):
            a=x
    print(x,'é a raiz que fica dentro do intervalo','[',aa,';',bb,']')

else:
    print('não existe uma raiz da função')

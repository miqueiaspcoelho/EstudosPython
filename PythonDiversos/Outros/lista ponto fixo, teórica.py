#ponto fixo, lista que o professor passou
'''#questão 1
m=1.72
L=7
f1=((20*m**3)-(120*m**2)-120)/-217
f2=((120-217*m+(120*m**2))/20)**(1/3)
f3=((120/m**2)-(217/m)+120)/20

f1=round(f1,9)
f2=round(f2,9)
f3=round(f3,9)
#funciona só para o segundo ponto fixo
f4=(((217*m)+(20*m**3)-120)/120)**0.5
f4=round(f4,9)
#PRIMEIRO e TERCEIRO PONTOS FIXOS
#função iteração 1
e1=1
i=0
while abs(e1)>10**-L:
    i=i+1
    f1=((20*f1**3)-(120*f1**2)-120)/-217
    f1=round(f1,9)
    e1=(20/3*f1**3)-(40*f1**2)+(217/3*f1)-40
print(f1,i,abs(e1))   
#função iteração 2
p=0
e2=1
while abs(e2)>10**-L:
    p=p+1 
    f2=((120-217*f2+(120*f2**2))/20)**(1/3)
    f2=round(f2,9)
    e2=(20/3*f2**3)-(40*f2**2)+(217/3*f2)-40
print(f2,p,abs(e2))   
#função de iteraçao 3
q=0
e3=1
while abs(e3)>10**-L:
    q=q+1 
    f3=((120/f3**2)-(217/f3)+120)/20
    f3=round(f3,9)
    e3=(20/3*f3**3)-(40*f3**2)+(217/3*f3)-40
print(f3,q,abs(e3))
#SEGUNDO PONTO FIXO
j=0
e4=1
while abs(e4)>10**-L:
    j=j+1 
    f4=(((217*f4)+(20*f4**3)-120)/120)**0.5
    f4=round(f4,9)
    e4=(20/3*f4**3)-(40*f4**2)+(217/3*f4)-40
print(f4,j,abs(e4))
'''
'''#questão 2 não precisa iterar, mas deu certo e valeu o esforço
y=0.618
e5=1
L1=8
f5=(1-y)**0.5
#f5=round(f5,9)
i2=0
while abs(e5)>10**-L1:
    i2=i2+1
    f5=(1-f5)**0.5
    #f5=round(f5,9)
    e5=(1-f5)**0.5-f5
    
print(f5,i2,abs(e5))
'''
#questão 3 
y2=0.31
e6=1
L2=8
i3=0
f6=(1/(y2+(4/y2)-3))**0.5
while abs(e6)>10**-L2:
    i3=i3+1
    f6=(1/(f6+(4/f6)-3))**0.5
    e6=(1-f6)**3-f6
print(f6,i3,abs(e6))

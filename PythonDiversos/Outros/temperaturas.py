#Código genérico rodando.
x=int(input('Qual a quantidade de dias?'))

contador1=0
contador2=0
contador3=0
temp=0
for a in range(0,x):
    
    e=float(input('Qual a temperatura?'))
    temp=temp+e

    if e==1:
        contador1=contador1+1
    if e>=2 and e>=4:
        contador2=contador2+1
    if e>4:
        contador3=contador3+1

media_das_temperaturas=temp/x
print('media das temperaturas',media_das_temperaturas)

#percentual das temperaturas.

a=(contador1*100)/x
print('percentual das temperaturas iguais a 1',a)
b=(contador2*100)/x
print('percentual das temperaturas entre 2 e 4',b)
c=(contador3*100)/x
print('temperaturas maiores que 4',c)

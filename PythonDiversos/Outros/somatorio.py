print('Calculando Pí por meio do somatório de parcelas.')
n=int(input('Número de parcelas: '))
x=1
s=0
i=1
for a in range (0,n):
    s=s+(1/(x**3))*i
    x=x+2
    i=i*-1
print('O somatório das',n,'parcelas é:',s)
pi=((s*32)**(1/3))
print('Valor de Pí calculado: ',pi)
import math
print('Pí ''exato:''',math.pi)

from matplotlib import pyplot as plt
import numpy as np

x=[0,  0,  0,  0,  1, 0, 0, 0, 0]
t=[-4, -3, -2, -1, 0, 1, 2, 3, 4]
t_escala=[]
a=0
tipo_escala=''
if a > 1:
    for valor in t:
        t_escala.append(valor/a)
        tipo_escala='Compressão'
if a>0 and a<1:
    for valor in t:
        t_escala.append(valor/a)
        tipo_escala='Expansão'
if a==1:
    t_escala=t
    tipo_escala='Igual a entrada'
if a==0:
    t_escala=len(x)*[0]
    tipo_escala='Zerado'


print(t_escala)
plt.plot(t,x,color='black', label='Entrada')
plt.plot(t_escala,x,'b--',label=tipo_escala)
plt.xlabel('t')

plt.ylabel('x(t)=entrada e y(t)=saida')
plt.title('Deslocamento no tempo')

plt.grid()
plt.legend(loc='best')

plt.show()

    

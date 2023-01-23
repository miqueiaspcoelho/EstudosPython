from matplotlib import pyplot as plt
import numpy as np
'''DESLOCAMENTO NO TEMPO '''

#x=[0,  0,  0,  0,  1, 0, 0, 0, 0] # sinal de entrada (valores do eixo Y)
#tempo=[-4, -3, -2, -1, 0, 1, 2, 3, 4] #vetor de tempo (valores do eixo X)
#tempo_deslocado=[] #vetor com o deslocamento

#sinal x(t)

t1=1 #valor do deslocamento (atraso de t1=1)
t2=-1 #valor do deslocamento (adiantado de t2=1)

tempo_deslocado1=[] #tempo deslocado (atraso)
tempo_deslocado2=[] #tempo deslocado (avanço)

t=np.linspace(0,5) #tempo
x=np.exp(-2*t) #função

for elemento in t:
    tempo_deslocado1.append(elemento+t1)
    tempo_deslocado2.append(elemento+t2)

plt.plot(t,x,color='black', label='Entrada')
plt.plot(tempo_deslocado1,x,color='blue', label='Entrada atrasada em '+str(t1))
plt.plot(tempo_deslocado2,x,color='green', label='Entrada adiantada em '+str(t2))
plt.xlabel('t')

plt.ylabel('y(t)=x(t-t0)')
plt.title('Deslocamento no tempo')

plt.grid()
plt.legend()

plt.show()

    

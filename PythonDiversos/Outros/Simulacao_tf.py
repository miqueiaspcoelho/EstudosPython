'''
Exemplo de simulação de sistema usando função de transferência em Python
Disciplina: Análise de Sistemas Lineares - UFMA
Prof. Dr. Paulo Rogério de Almeida Ribeiro
'''

import matplotlib.pyplot as plt
import numpy as np
import control.matlab
import math

#Constantes da EDO
a=1# m
b=0.125 # b
c=1 #k

#Condições iniciais
y0=[[0], [2]] # ordem no código é: y'[0] e depois y[0] /  nesse exemplo  y'[0]=0 e y[0]=2

#Definições de tempo de simulação
Tfinal=60; #Segundos
DeltaT=0.01 #Passo
Tfinal=Tfinal/DeltaT;
tempo=list(range(0,int(Tfinal), 1))

#Entrada, neste exemplo, x(t) = 3cos(0.3t)
x=[]
N=len(tempo)
i=0
freq_sinal=0.3
Amp_sinal=3
while (i<N):
   tempo[i] = tempo[i]*DeltaT
   #x.append(0) #Caso a entrada fosse zero - equação homogênea
   x.append(Amp_sinal*math.cos(freq_sinal*tempo[i]))
   i=i+1
tempo = np.array(tempo)

#Função de transferência, neste exemplo (massa-mola amortecedor): 1/(ms²+bs+k)
num_ft=[1]
den_ft=[a, b, c]
func_trans=control.matlab.tf(1, [a, b, c])

#Simulação usando a função lsim
yout, t, xout = control.matlab.lsim(func_trans, x, tempo, y0)
plt.plot(tempo, yout, 'b--')
plt.show()

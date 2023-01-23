import math as mt
#valores de lambda (estão disposto na tabela do pdf.)
Y=[4.7,7.8,10.9,14.1,17.2]
#comprimento da viga
L=3.4
#modulo de elasticidade
E=5
#momento de inercia
I=7
#massa por unidade de comprimento
m=10000
const= 2*(mt.pi)*(L**2)
F=[]
for i in range (0,len(Y)):
    f= ((Y[i])**2/const)*(E*I/m)**0.5
    F.append(f)
    print(f,'Hz')

import matplotlib.pyplot as plt
import numpy as np

#TEMPOS DE QUEDA MEDIDOS

TEMPOS=[0.2403023,0.240498,0.249923,0.261691,0.253290,
0.251643,0.250353,0.252837,0.256167,0.258629,
0.250560,0.252290,0.257753,0.248144,0.257472,
0.245576,0.246297,0.236246,0.245847,0.242838,
0.256556,0.244604,0.246757,0.248669,0.250156,
0.247049,0.254929,0.247209,0.246877,0.255456,
0.250780,0.248494,0.250109,0.252073,0.256587,
0.254553,0.245461,0.258727,0.253130,0.258727,
0.252877,0.253747,0.252876,0.245191,0.249878,
0.252479,0.255992,0.241566,0.247615,0.246322,
0.250203,0.253212,0.252213,0.250022,0.245678,
0.264213,0.253214,0.252116,0.241316,0.242281,
0.249921,0.243122,0.244312,0.252210,0.254013,
0.231220,0.241540,0.241082,0.244113,0.256781,
0.251012,0.253104,0.240231,0.242720,0.262343,
0.251214,0.253122,0.250241,0.243240,0.247115,
0.248231,0.254320,0.251320,0.252245,0.243021,
0.234234,0.241781,0.240422,0.243103,0.243504,
0.251311,0.232834,0.242541,0.252831,0.242040,
0.252412,0.251819,0.240208,0.250033,0.251091]

G=[]
X=[]

#CALCULANDO OS VALORES DA GRAVIDADE USANDO g=2*h/t²

tam=len(TEMPOS)
for x in range(0,tam):
    X.append(x+1)
    g=0.8/(TEMPOS[x]**2)
    G.append(g)

#APLICANDO A IDEIA DOS MINIMOS QUADRADOS
Sxy=0
Sx=0
Sy=0
Sqx=0

Sxy1=0
Sx1=0
Sy1=0
Sqx1=0

for x in range (0,tam):
    Sxy=Sxy+(x+1)*G[x]
    Sx=Sx+(x+1)
    Sy=Sy+G[x]
    Sqx=Sqx + (x+1)**2

for x in range (0,tam):
    Sxy1=Sxy1+(TEMPOS[x])*G[x]
    Sx1=Sx1+(TEMPOS[x])
    Sy1=Sy1+G[x]
    Sqx1=Sqx1 + (TEMPOS[x])**2

#COEFICIENTES
 

m=(tam*Sxy - Sx*Sy)/(tam*Sqx - Sx**2)
b=(Sqx*Sy-Sxy*Sx)/(tam*Sqx - Sx**2)
print('y=',m,'x +',b)

m1=(tam*Sxy1 - Sx1*Sy1)/(tam*Sqx1 - Sx1**2)
b1=(Sqx1*Sy1-Sxy1*Sx1)/(tam*Sqx1 - Sx1**2)
print('y1=',m1,'x +',b1)

#ERRO

for x in range (0,tam):
    e=(G[x]- (m*x+b))**2
print('Erro=',e)


for x in range (0,tam):
    e=(G[x]- (m1*TEMPOS[x]+b1))**2
print('Erro1=',e)

#PLOTANDO OS GRAFICOS

x=np.linspace(min(X)-10,max(X)+10,num=1000)
y=x
plt.grid(True)
plt.plot(x,(y*m1+b1),'b-')
plt.xlim(min(TEMPOS)-0.0005,max(TEMPOS)+0.0005)
plt.ylim(min(G)-0.5,max(G)+0.5)
plt.xlabel('TEMPOS DOS LANÇAMENTOS (s)')
plt.ylabel('GRAVIDADE CALCULADA  (m/s²)')
plt.scatter(TEMPOS,G, marker="o", color='red')
plt.show()


x1=np.linspace(min(X)-10,max(X)+10,num=1000)
y1=x1
plt.grid(True)
plt.plot(x1,(y1*m+b),'b-')
plt.xlim(min(X)-5,max(X)+5)
plt.ylim(min(G)-1,max(G)+1)
plt.xlabel('Nº DO LANÇAMENTO')
plt.ylabel('GRAVIDADE CALCULADA  (m/s²)')
plt.scatter(X,G, marker="o", color='red')
plt.show()

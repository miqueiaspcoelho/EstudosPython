Pontos=[(-1,15),(0,8),(3,-1)]
tam=len(Pontos)
m=1
b=1
PL=[]
PL1=[]
PL2=[]
m=1
a=1
for x in range (0,tam):
    i=0
    a=1
    b=1
    for j in range (0,tam):
        if j!=x:
            a=a*(Pontos[x][0] - Pontos[j][0])
            i=i+1
        if i==(tam-1):
            PL.append(a)
for y in range (0,tam):
    b=1
    for z in range(y+1,tam):
        b=b*((-Pontos[y][0]) + (-Pontos[z][0]))
        c=(-Pontos[y][0]) * (-Pontos[z][0])
        print('-',Pontos[y][0],'*','-',Pontos[z][0],'=',c)
        PL1.append(b)
        PL2.append(c)
PLaux=[]
PL1aux=[]
PL2aux=[]
for x in range(0,tam):
    PLaux.append(PL[x])
i=len(PL1)-1
for x in range(0,len(PL1)):
    if i>=0:
        PL1aux.append(PL1[i])
        PL2aux.append(PL2[i])        
        i=i-1
L2=[]
j=0
k=0
for x in range (0,tam):
    u=Pontos[x][1]/PLaux[x]
    print(Pontos[x][1],'/',PLaux[x],'=',u)
    j=j+PL1aux[x]*u
    k=k+PL2aux[x]*u
    L2.append(u)
a=sum(L2)
print('a=',PL)
print('j=',PL1)
print('k=',PL2)

'''
import matplotlib.pyplot as plt
import numpy as np
X=[]
Y=[]
for x in range (0,len(Pontos)):
    X.append(Pontos[x][0])
    Y.append(Pontos[x][1])
xmax=max(X+Y)
x = np.linspace(min(X)-2,max(X)+2,num=100)
y = x
plt.xlim(min(X)-2,max(X)+2)
plt.ylim(min(Y)-2,max(Y)+2)
plt.xlabel('x')
plt.ylabel('P (x)')
plt.grid(True)
plt.title('INTERPOLAÇÃO DE LAGRANGE, 3 PONTOS')
plt.plot(x,(y**2*a + y*j + k),'r--', drawstyle='default') 
plt.scatter(X, Y, marker="o", color='red')
plt.show()
'''



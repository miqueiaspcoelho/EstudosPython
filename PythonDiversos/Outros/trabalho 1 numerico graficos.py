import matplotlib.pyplot as plt
import numpy as np
Pontos=[(-1,2),(-2,4),(5,0),(-4,11)]
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
plt.xlabel('DIA')
plt.ylabel('VALOR DO DOLAR')
plt.grid(True)
plt.title('VALORES DO DOLAR (OUTUBRO DE 2019)')
plt.plot(x,((y*MB[u][0])+MB[u][1]),'r--', drawstyle='default') 
plt.scatter(X, Y, marker="o", color='red')
plt.show()

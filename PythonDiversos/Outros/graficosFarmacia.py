import math
import matplotlib.pyplot as plt
import numpy as np

tpsa=[40.46,20.23,29.46,53.35,42.35,33.37,33.37,40.46,22.13,
      53.35,29.46,40.46,20.23,29.46,38.70,22.13,33.12,
      53.35,42.35,65.48,40.46]
logp=[3.67,4.83,4.21,3.32,3.60,3.90,3.64,3.35,4.83,3.10,3.96,3.88,4.81,3.95,
      3.38,4.96,4.96,3.50,3.49,2.78,3.68]
gpcr=[0.37,0.34,0.29,0.44,0.36,0.32,0.31,0.22,0.30,0.28,0.45,0.23,0.35,0.29,0.36,0.27,0.36,0.29,0.40,0.24,0.34]

listau=[]
listaw=[]
listaz=[]

for x in range(0,21):
    u=math.log(tpsa[x],10)
    listau.append(u)

    w=math.log(logp[x],10)
    listaw.append(w)

    z=math.log(gpcr[x],10)
    listaz.append(z)
'''
#verde (atividade biologica gpcr)
plt.plot(gpcr)
#laranja (log de tpsa)
plt.plot(listau)
#azul (log de p)
plt.plot(listaw)
'''
plt.plot(

listap=[]
listalog=[]
listagpcr=[]
a=0
b=0
c=0

somatpsa=sum(tpsa)
somalogp=sum(logp)

for x in range (0,21):
    a= a + (tpsa[x]*logp[x])
    b= b +(tpsa[x])**2
    c= c + (logp[x])**2

    listap.append(a)
    listalog.append(b)
    listagpcr.append(c)

p=a - ((somatpsa*somalogp)/21)/ ((b-((somatpsa)**2/21))*(c - ((somalogp**2)/21)))**0.5
print(p)    
    

'''
plt.xlabel('LogP')
plt.ylabel('GPCR')
'''
plt.show()

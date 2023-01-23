import matplotlib.pyplot as plt
import numpy as np

lea=[]
ler=[]
lel=[]
i=0.05*(10**(-9))
t=i
li=[]

while t<10**(-9):
    ea=-1.436/t
    er=(5.86*10**(-6))/(t)**9
    el=ea+er

    lea.append(ea)
    ler.append(er)
    lel.append(el)
    t=t+i
    li.append(t)
    
plt.plot(li,lel)
plt.xlabel('Raio Interatômico (m)')
plt.ylabel('Energia de de Ligação (eV)')

plt.plot(li,ler)
plt.xlabel('Raio Interatômico (m)')
plt.ylabel('Energia de Repulsão (eV)')

plt.plot(li,lea)
plt.xlabel('Raio Interatômico (m)')
plt.ylabel('Energia de de Atração (eV)')


plt.show()
    
    

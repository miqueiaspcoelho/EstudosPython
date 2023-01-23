from matplotlib import pyplot as plt
import numpy as np
'''
def y_retangular(t,a,b):
    lista=[]
    for n in t:
        if n <a:
            lista.append(0)
        if n>=a and n<=b:
            lista.append(1)
        if n>b:
            lista.append(0)
        
    return lista

n_pontos=500
l_inferior=-2
l_superior=2


#t=np.linspace(l_inferior,l_superior,n_pontos)
o=y_retangular(t,-0.5,0.5)
#plt.plot(t,o)
#plt.show()
'''
#x=[0,0,1,0,0]
#t=[-2,-1,0,1,2]
#x=[0,0,1,1,0,0,0]
#t=[-2,-1,-0.5,0,0.5,1,2]
x=[1,2,4,16]
t=[-2,-1,0,1]
y=[]
i=1
for n in range(0,len(x)):
    if i<len(x):
       fx=(x[i]-x[n])/(t[i]-t[n])
       y.append(fx)
       if len(y)==1:
           y.append(fx)
    i+=1

plt.plot(t,y,color='red',label='Sinal de Saida')
plt.plot(t,x,'b--',label='Sinal de Entrada')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('y(t)=dx(t)/dt')
plt.axis([min(t)-1,max(t)+1,min(y)-1,1.5*max(y)])
plt.grid()
plt.show()



#método das diferenças finitas para derivar a função


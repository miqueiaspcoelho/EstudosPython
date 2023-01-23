import math
'''
a=[4.153979239,4.099591837,3.602629657,4.407713499]
d=0
for tudo in range(0,4):
    t=(a[tudo] - 4.065978558)**2
    print(round(t,10))
    d+=t

print(d)
'''
'''
al=[0.2401,0.2511,0.2466,0.2405]

m=0.244575
d=0.004563551
e=2.72
pi=3.14

print('Desvio padrão',round(desvp,9))
print('média'm)

'''
t=[0.34,0.35,0.37,0.33]
m=0.3475
d=0.029580398
e=2.72
pi=3.14


for tudo in range(0,4):
    fdg=(1/(d*((2*pi)**0.5))) * (e**(-((t[tudo] - m )**2)/(2*(d**2))))
    j=(e**(-((t[tudo] - m )**2)/(2*(d**2))))
    z=(1/(d*((2*pi)**0.5)))
    print(j)
    



'''

m=sum(al)/4
s=0
for tudo in range(0,4):
    t=(al[tudo]-m)
    t=t**2
    s+=t
d=(s/4)**0.5
print('Desvio padrão das posições iniciais=',d)

gaus=[]
for tudo in range(0,4):
    z=(1/(d*(2*math.pi)**0.5)*(math.e**(-(al[tudo]-m)**2/(2*(d**2)))))
    z=round(z,3)

    gaus.append(z)
print('Para as posições iniciais nós temos o seguinte conjunto gaussiano=',gaus,'\n')

'''

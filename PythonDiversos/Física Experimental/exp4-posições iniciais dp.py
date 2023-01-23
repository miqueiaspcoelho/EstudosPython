import math
print(math.e)
a=[0.1456,0.2197,0.1831,0.2746,0.293,0.3113]
m=sum(a)/6
s=0
for tudo in range(0,6):
    t=(a[tudo]-m)
    t=t**2
    s+=t
d=(s/6)**0.5
print('Desvio padrão das posições iniciais=',d)

gaus=[]
for tudo in range(0,6):
    z=(1/(d*(2*math.pi)**0.5)*math.e**(-(a[tudo]-m)**2/(2*(d**2))))
    z=round(z,3)
    gaus.append(z)
print('Para as posições iniciais nós temos o seguinte conjunto gaussiano=',gaus,'\n')
hmax=[0.145, 0.218, 0.184, 0.272, 0.293, 0.312]
r=sum(hmax)/6
ss=0
for tudo in range(0,6):
    p=(hmax[tudo]-r)
    p=p**2
    ss+=p
d1=(ss/6)**0.5
gaush=[]
for tudo in range(0,6):
    y=(1/(d1*(2*math.pi)**0.5)*math.e**(-(hmax[tudo]-m)**2/(2*(d**2))))
    y=round(y,3)
    gaush.append(y)
print('Para as alturas máximas nós temos o seguinte conjunto gaussiano=',gaush,'\n')

l1=[0.142,0.145,0.144]
l2=[0.215,0.216,0.218]
l3=[0.182,0.184,0.182]
l4=[0.268,0.272,0.272]
l5=[0.293,0.293,0.293]
l6=[0.312,0.310,0.311]
print('--------------------------------------------------------------\n')
print('DESVIOS DOS LANÇAMENTOS EM RELAÇÃO À MÉDIA DAS ALTURAS MÁXIMAS.\n')
for tudo in range(0,3):
    D1=(l1[tudo]-m)
    D2=(l2[tudo]-m)
    D3=(l3[tudo]-m)
    D4=(l4[tudo]-m)
    D5=(l5[tudo]-m)
    D6=(l6[tudo]-m)

    print('Desvio (s1)==',l1[tudo],'-',m,'=',D1,'\n'
          'Desvio (s2)==',l2[tudo],'-',m,'=',D2,'\n'
          'Desvio (s3)==',l3[tudo],'-',m,'=',D3,'\n'
          'Desvio (s4)==',l4[tudo],'-',m,'=',D4,'\n'
          'Desvio (s5)==',l5[tudo],'-',m,'=',D5,'\n'
          'Desvio (s6)==',l6[tudo],'-',m,'=',D6,'\n')

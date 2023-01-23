#w=2pi/T
#tq= tempo de queda
#p= período
#h= altura
#d= diâmetro
import math
pi=math.pi

m=0.1

tq=[1.809401,1.79151,1.472639]
p=[0.490843,0.635906,0.449469]
h=[0.15,0.133,0.128]
d=[0.0189,0.01865,0.0191]

print('ITEM 1 FREQUÊNCIA ANGULAR E PROPAGAÇÃO DE ERROS\n')
W=[]
errop=[]
z=2*pi
for tudo in range(0,3):
    a=z/p[tudo]
    W.append(a)
    deltap=(((z/p[tudo]**2)**2)*(0.000001**2))**0.5
    errop.append(deltap)
    print('Frequência angular=',a,'\n'
          'Propagação de erro=',deltap,'\n')

print('---------------------------------------------------------------------------------------------------')
print('ITEM 2 MÉDIA E DESVIO PADRÃO DA FREQUÊNCIA\n')
mw=sum(W)/3
s=0
for tudo in range(0,3):
   b=(W[tudo] - mw)**2
   s+=b
desvp=(s/3)**0.5
print('Média da frequência angular=',mw,'\n'
      'Desvio padrão da frequência angular=',desvp,'\n')

print('---------------------------------------------------------------------------------------------------')
print('ITEM 3 MOMENTO DE INÉRCIA E PROPAGAÇÃO DE ERRO\n')
inercia=[]
erroI=[]
for tudo in range(0,3):
    
    I=((d[tudo])*m*(h[tudo])*(p[tudo]))/(z*tq[tudo])
    deltai1=(((m*h[tudo]*p[tudo])/(z*tq[tudo]))**2)*(0.000005**2)
    deltai2=(((d[tudo]*h[tudo]*p[tudo])/z*tq[tudo])**2)*(0.0001**2)
    deltai3=(((d[tudo]*m*p[tudo])/z*tq[tudo])**2)*(0.005)**2
    deltai4=(((d[tudo]*m*h[tudo])/z*tq[tudo])**2)*(0.000001**2)
    deltai5=(((d[tudo]*m*h[tudo]*p[tudo])/z*(tq[tudo]**2))**2)*(0.000001**2)
    DELTAI=(deltai1 + deltai2 + deltai3 + deltai4 + deltai5)**0.5

    inercia.append(I)
    erroI.append(DELTAI)
    print('Momento de inércia=',I,'\n'
          'Propagação de erro=',DELTAI,'\n')
    
print('---------------------------------------------------------------------------------------------------')
print('ITEM 4 MÉDIA E DESVIO PADRÃO DO MOMENTO DE INÉRCIA\n')
mi=sum(inercia)/3
s1=0
for tudo in range(0,3):
    c=(inercia[tudo] - mi)**2
    s1+=c
desvi=(s1/3)**0.5
print('Média do momento de inércia=',mi,'\n'
      'Desvio padrão do momento de inércia=',desvi,'\n')

print('---------------------------------------------------------------------------------------------------')
print('ITEM 5 MOMENTO ANGULAR E PROPAGAÇÃO DE ERRO\n')
momento=[]
erroL=[]
for tudo in range(0,3):
    L=inercia[tudo]*W[tudo]
    L1=d[tudo]*m*h[tudo]/tq[tudo]
    deltaL1=(((m*h[tudo])/(tq[tudo]))**2)*(0.000005**2)
    deltaL2=(((d[tudo]*m)/(tq[tudo]))**2)*(0.0001**2)
    deltaL3=(((d[tudo]*m)/(tq[tudo]))**2)*(0.005**2)
    deltaL4=(((d[tudo]*m*h[tudo])/(tq[tudo]))**2)*(0.000001**2)
    DELTAL=(deltaL1 + deltaL2+ deltaL3 + deltaL4)**0.5
    momento.append(L)
    erroL.append(DELTAL)
    print('Momento de inércia=',L,'\n'
          'Propagação de erro=',DELTAL,'\n')

print('---------------------------------------------------------------------------------------------------')
print('ITEM 6 MÉDIA E DESVIO PADRÃO DO MOMENTO ANGULAR\n')
ml=sum(momento)/3
s2=0
for tudo in range(0,3):
    d=(momento[tudo] - ml)**2
    s2+=d
desvl=(s2/3)**0.5
print('Média do momento de inércia=',ml,'\n'
      'Desvio padrão do momento de inércia=',desvl,'\n')

print('---------------------------------------------------------------------------------------------------')
print('ITEM 7 ERRO TOTAL PARA A FREQUÊNCIA ANGULAR\n')
errototalfrequencia=[]
for tudo in range(0,3):
    wt=((desvp**2)+(errop[tudo]**2))**0.5
    errototalfrequencia.append(wt)
    print('Erro total da frequência:',W[tudo],'=',wt)


print('---------------------------------------------------------------------------------------------------')
print('\nITEM 8 ERRO TOTAL PARA O MOMENTO DE INERCIA\n')
errototalmomentoinercia=[]
for tudo in range(0,3):
    It=((desvi**2)+ (erroI[tudo]**2))**0.5
    errototalmomentoinercia.append(It)
    print('Erro total do momento de inércia:',inercia[tudo],'=',It)

print('---------------------------------------------------------------------------------------------------')
print('\nITEM 9 ERRO TOTAL PARA O MOMENTO ANGULAR\n')
errototalangular=[]
for tudo in range(0,3):
    Lt=((desvl**2)+ (erroL[tudo]**2))**0.5
    errototalangular.append(Lt)
    print('Erro total do momento de angular:',momento[tudo],'= ',Lt)

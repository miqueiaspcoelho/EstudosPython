import math

#Ângulos de reflexão#
a15alpha=[15.0, 15.0, 15.5, 15.5, 15.5,
15.5, 15.5, 15.5, 15.5, 15.5,
15.0, 14.5, 15.5, 14.5, 15.5,
15.5, 14.5, 15.5, 14.5, 15.5,
15.4, 15.0, 15.4, 15.0, 15.2]

a30alpha=[30.5, 30.9, 30.0, 30.9, 29.5,
30.2, 30.4, 30.0, 30.3, 30.0,
30.0, 30.3, 30.3, 30.0, 30.3,
30.0, 31.1, 30.0, 30.2, 30.1,
30.0, 30.1, 30.0, 30.1, 30.2]


a45alpha=[44.0, 45.9, 44.9, 46.0, 44.9,
44.5, 46.0, 44.5, 46.0, 44.5,
44.8, 45.5, 44.6, 45.5, 44.8,
45.5, 44.5, 44.5, 44.7, 45.0,
45.9, 45.5, 45.5, 46.0, 45.1]

a60alpha=[59.9, 61.0, 59.9, 61.0, 59.9,
60.5, 61.0, 60.5, 61.0, 60.5,
59.7, 61.0, 60.0, 60.8, 60.0,
59.9, 60.5, 61.0, 59.9, 59.8,
60.0, 61.0, 60.5, 61.0, 60.5]
#---------------------------------------------------------#
#Ângulos de refração#

a15ref=[10.0, 10.0, 10.0, 10.0, 9.9,
9.9, 9.9, 9.9, 9.9, 9.9,
9.9, 9.9, 9.9, 9.9, 9.9,
10.0, 9.9, 9.9, 9.9, 9.9,
9.9, 10.2, 9.9, 10.1, 9.9]

a30ref=[20.0, 19.2, 20.0, 19.4, 20.0,
19.9, 19.9, 20.0, 19.1, 19.9,
19.4, 20.0, 19.4, 20.0, 19.4,
20.0, 19.1, 20.0, 19.1, 20.0,
19.1, 20.0, 19.0, 20.1, 19.3]

a45ref=[28.5, 28.0, 29.0, 28.2, 29.0,
28.9, 28.0, 28.9, 28.0, 28.9,
28.8, 28.0, 28.9, 28.0, 28.9,
28.0, 28.7, 28.8, 28.3, 29.0,
29.1, 28.0, 29.0, 28.0, 29.0]

a60ref=[36.0, 35.5, 36.0, 35.4, 36.0,
36.0, 35.5, 36.0, 36.5, 36.0,
36.0, 35.2, 35.2, 35.2, 36.8,
36.0, 35.4, 36.5, 35.5, 36.0,
36.0, 35.5, 36.0, 35.5, 36.0]
#------------------------------------------------------------------#
#ângulos limites
alimites=[42.5,42.3,42.5,42.4,42.5,
          43.0,43.0,43.9,43.1,42.9,
          43.0,42.5,42.8,44.0,43.0,
          43.5,42.5,43.0,43.8,43.0,
          42.5,42.3,42.4,42.5,42.1]
#-----------------------------------------------------------------#

#1- médias
#angulos de reflexão.
ma15alpha=sum(a15alpha)/25
ma30alpha=sum(a30alpha)/25
ma45alpha=sum(a45alpha)/25
ma60alpha=sum(a60alpha)/25
print('MÉDIA DOS ÂNGULOS DE REFLEXÃO\n'
      'I=15º=',round(ma15alpha,1),'º\n'
      'I=30º=',round(ma30alpha,1),'º\n'
      'I=45º=',round(ma45alpha,1),'º\n'
      'I=60º=',round(ma60alpha,1),'º\n')

#angulos de refração
ma15ref=sum(a15ref)/25
ma30ref=sum(a30ref)/25
ma45ref=sum(a45ref)/25
ma60ref=sum(a60ref)/25
print('MÉDIA DOS ÂNGULOS DE REFRAÇÃO\n'
      'I=15º=',round(ma15ref,1),'º\n'
      'I=30º=',round(ma30ref,1),'º\n'
      'I=45º=',round(ma45ref,1),'º\n'
      'I=60º=',round(ma60ref,1),'º\n')

#2- desvio padrão
#angulos de reflexão
salpha15=0
salpha30=0
salpha45=0
salpha60=0
for tudo in range(0,25):
    da15alpha=(ma15alpha - a15alpha[tudo])**2
    da30alpha=(ma30alpha - a30alpha[tudo])**2
    da45alpha=(ma45alpha - a45alpha[tudo])**2
    da60alpha=(ma60alpha - a60alpha[tudo])**2

    salpha15+=da15alpha
    salpha30+=da30alpha
    salpha45+=da45alpha
    salpha60+=da60alpha

DALPHA15=(salpha15/24)**0.5
DALPHA30=(salpha30/24)**0.5
DALPHA45=(salpha45/24)**0.5
DALPHA60=(salpha60/24)**0.5

print('DESVIO PADRÕES- ÂNGULOS DE REFLEXÃO\n'
      'I=15º=',round(DALPHA15,2),'º\n'
      'I=30º=',round(DALPHA30,2),'º\n'
      'I=45º=',round(DALPHA45,2),'º\n'
      'I=60º=',round(DALPHA60,2),'º\n')

#ângulos de refração
sref15=0
sref30=0
sref45=0
sref60=0
for tudo in range(0,25):
    da15ref=(ma15ref - a15ref[tudo])**2
    da30ref=(ma30ref - a30ref[tudo])**2
    da45ref=(ma45ref - a45ref[tudo])**2
    da60ref=(ma60ref - a60ref[tudo])**2

    sref15+=da15ref
    sref30+=da30ref
    sref45+=da45ref
    sref60+=da60ref

DREF15=(sref15/24)**0.5
DREF30=(sref30/24)**0.5
DREF45=(sref45/24)**0.5
DREF60=(sref60/24)**0.5

print('DESVIO PADRÕES- ÂNGULOS DE REFRAÇÃO\n'
      'I=15º=',round(DREF15,2),'º\n'
      'I=30º=',round(DREF30,2),'º\n'
      'I=45º=',round(DREF45,2),'º\n'
      'I=60º=',round(DREF60,2),'º\n')

#item 3 - indices de refração
sen15=math.sin(math.radians(15))
cos15=math.cos(math.radians(15))

sen30=0.5
cos30=math.cos(math.radians(30))

sen45=(2**0.5)/2
cos45=math.cos(math.radians(45))

sen60=(3**0.5)/2
cos60=math.cos(math.radians(60))

indices15=[]
indices30=[]
indices45=[]
indices60=[]
for tudo in range(0,25):
    nref15=sen15/(math.sin(math.radians(a15ref[tudo])))
    nref30=sen30/(math.sin(math.radians(a30ref[tudo])))
    nref45=sen45/(math.sin(math.radians(a45ref[tudo])))
    nref60=sen60/(math.sin(math.radians(a60ref[tudo])))

    indices15.append(round(nref15,2))
    indices30.append(round(nref30,2))
    indices45.append(round(nref45,2))
    indices60.append(round(nref60,2))
print(indices15,'\n',
      indices30,'\n',
      indices45,'\n',
      indices60,'\n')


#item 4 - questão 1
delta15=0
delta30=0
delta45=0
delta60=0
for tudo in range(0,25):
    d15=(15 - a15alpha[tudo])
    d30=(30 - a30alpha[tudo])
    d45=(45 - a45alpha[tudo])
    d60=(60 - a60alpha[tudo])

    delta15+=d15
    delta30+=d30
    delta45+=d45
    delta60+=d60

D15=(delta15/25)
D30=(delta30/25)
D45=(delta45/25)
D60=(delta60/25)

print('QUESTÃO 1\n'
      'I=15º=',round(D15,2),'º +-',round(DALPHA15,2),'\n'
      'I=30º=',round(D30,2),'º +-',round(DALPHA30,2),'\n'
      'I=45º=',round(D45,2),'º +-',round(DALPHA45,2),'\n'
      'I=60º=',round(D60,2),'º +-',round(DALPHA60,2),'\n')
#item 5 - questão 4
mi15=sum(indices15)/25
mi30=sum(indices30)/25
mi45=sum(indices45)/25
mi60=sum(indices60)/25

si15=0
si30=0
si45=0
si60=0
for tudo in range(0,25):
    a=(mi15 - indices15[tudo])**2
    b=(mi30 - indices30[tudo])**2
    c=(mi45 - indices45[tudo])**2
    d=(mi60 - indices60[tudo])**2

    si15+=a
    si30+=b
    si45+=c
    si60+=d

dsi15=(si15/24)**0.5
dsi30=(si30/24)**0.5
dsi45=(si45/24)**0.5
dsi60=(si60/24)**0.5

print('INDICE DE REFRAÇÃO DO MATERIAL PARA CADA ÂNGULO\n'
      'I=15º=',round(mi15,2),'+-',round(dsi15,2),'\n'
      'I=30º=',round(mi30,2),'+-',round(dsi30,2),'\n'
      'I=45º=',round(mi45,2),'+-',round(dsi45,2),'\n'
      'I=60º=',round(mi60,2),'+-',round(dsi60,2),'\n')

#item 6 - questão 5
dx15=dsi15/(25**0.5)
dx30=dsi30/(25**0.5)
dx45=dsi45/(25**0.5)
dx60=dsi60/(25**0.5)
print('ERRO PADRÃO\n'
      'I=15º=',round(dx15,4),'\n'
      'I=30º=',round(dx30,4),'\n'
      'I=45º=',round(dx45,4),'\n'
      'I=60º=',round(dx60,4),'\n')

er15= ((1.49 - mi15)/1.49)*100
er30= ((1.49 - mi30)/1.49)*100
er45= ((1.49 - mi45)/1.49)*100
er60= ((1.49 - mi60)/1.49)*100
print('ERRO RELATIVO\n'
      'I=15º=',round(er15,2),'%\n'
      'I=30º=',round(er30,2),'%\n'
      'I=45º=',round(er45,2),'%\n'
      'I=60º=',round(er60,2),'%\n')

#item 7 -questão 6
#angulo limite
limite15=[]
limite30=[]
limite45=[]
limite60=[]
for tudo in range(0,25):
    x=math.asin(1/indices15[tudo])
    y=math.asin(1/indices30[tudo])
    z=math.asin(1/indices45[tudo])
    w=math.asin(1/indices60[tudo])

    x=round((math.degrees(x)),3)
    y=round((math.degrees(y)),3)
    z=round((math.degrees(z)),3)
    w=round((math.degrees(w)),3)
    
    limite15.append(x)
    limite30.append(y)
    limite45.append(z)
    limite60.append(w)
print(limite15,'\n\n',limite30,'\n\n',limite45,'\n\n',limite60,'\n')

mli15=sum(limite15)/25
mli30=sum(limite30)/25
mli45=sum(limite45)/25
mli60=sum(limite60)/25

print('MÉDIA DOS ANGULOS LIMITES\n'
      'I=15º=',round(mli15,2),'º\n'
      'I=30º=',round(mli30,2),'º\n'
      'I=45º=',round(mli45,2),'º\n'
      'I=60º=',round(mli60,2),'º\n')

#propagação de erro
#primeiro do indice de refração do acrilico
sal15=0
sal30=0
sal45=0
sal60=0
for tudo in range(0,25):
    D1=(mli15 - limite15[tudo])**2
    D2=(mli30 - limite30[tudo])**2
    D3=(mli45 - limite45[tudo])**2
    D4=(mli60 - limite60[tudo])**2

    sal15+=D1
    sal30+=D2
    sal45+=D3
    sal60+=D4

d1=(sal15/24)**0.5
d2=(sal30/24)**0.5
d3=(sal45/24)**0.5
d4=(sal60/24)**0.5

print('DESVIO PADRÃO PARA OS ÂNGULOS LIMITES\n'
      'I=15º=',round(d1,2),'º\n'
      'I=30º=',round(d2,2),'º\n'
      'I=45º=',round(d3,2),'º\n'
      'I=60º=',round(d4,2),'º\n')

erl15=d1/(25**0.5)
erl30=d2/(25**0.5)
erl45=d3/(25**0.5)
erl60=d4/(25**0.5)

print(round(erl15,2),round(erl30,2),round(erl45,2),round(erl60,2))

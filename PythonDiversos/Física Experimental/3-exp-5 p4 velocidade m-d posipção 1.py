xi=0.15
cos=(3**0.5)/2

lv=[1.28,1.15,1.15]
tv=[0.110028,0.388501,0.364801]

v0=[]
for tudo in range(0,3):

    vo=((lv[tudo])+xi)/(cos*(tv[tudo]))
    v0.append(vo)
    
vo=0
lb=[1.28,1.28,1.28]
tb=[0.137908,0.26301,0.408107]
v1=[]
for tudo in range(0,3):

    vo=((lb[tudo])+xi)/(cos*(tb[tudo]))
    v1.append(vo)

mv=sum(v0)/3
mb=sum(v1)/3

dv=0
db=0
for tudo in range(0,3):
    a=(v0[tudo]-mv)**2
    dv+=a
    b=(v1[tudo]-mb)**2
    db+=b
d1=(dv/3)**0.5
d2=(db/3)**0.5


print('Posição 1\n'
      'Bola verde\n\n'
      'Média das velocidades iniciais=',mv,'m/s\n'
      'Desvio padrão das velocidades iniciais=',d1,'m/s\n\n'
      'Bola branca\n'
      'Média das velocidades iniciais=',mb,'m/s\n'
      'Desvio padrão das velocidades iniciais=',d2,'m/s\n')
      


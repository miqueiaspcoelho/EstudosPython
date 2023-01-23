#periodos  v1=8 volts  v2=9 volts   v3=10volts
v1qua=[0.668259,0.671863,0.672713]
v1sen=[0.656098,0.668087,0.667857]
v1tri=[0.672565,0.669608,0.667687]


v2qua=[1.002232,1.319934,0.660513]
v2sen=[0.656098,0.668087,0.667857]
v2tri=[0.668257,0.667071,0.673586]

v3qua=[0.668317,0.663868,0.664398]
v3sen=[0.661309,0.658202,0.659353]
v3tri=[0.661365,0.655104,0.662501]

print('ITEM 1 MÉDIAS DOS PERÍODOS E DESVIOS PADRÕES\n')
m1q=sum(v1qua)/3
m1s=sum(v1sen)/3
m1t=sum(v1tri)/3

m2q=sum(v2qua)/3
m2s=sum(v2sen)/3
m2t=sum(v2tri)/3

m3q=sum(v3qua)/3
m3s=sum(v3sen)/3
m3t=sum(v3tri)/3


s1qua=0
s1sen=0
s1tri=0

s2qua=0
s2sen=0
s2tri=0

s3qua=0
s3sen=0
s3tri=0
for tudo in range(0,3):
    #desvios para 8volts
    d1qua=(v1qua[tudo] - m1q)**2
    d1sen=(v1sen[tudo] - m1s)**2
    d1tri=(v1tri[tudo] - m1t)**2

    s1qua+=d1qua
    s1sen+=d1sen
    s1tri+=d1tri

    #desvios para 9volts
    d2qua=(v2qua[tudo] - m2q)**2
    d2sen=(v2sen[tudo] - m2s)**2
    d2tri=(v2tri[tudo] - m2t)**2

    s2qua+=d2qua
    s2sen+=d2sen
    s2tri+=d2tri
    
    #desvios para 10volts
    d3qua=(v3qua[tudo] - m3q)**2
    d3sen=(v3sen[tudo] - m3s)**2
    d3tri=(v3tri[tudo] - m3t)**2

    s3qua+=d3qua
    s3sen+=d3sen
    s3tri+=d3tri

D1QUA=(s1qua/3)**0.5
D1SEN=(s1sen/3)**0.5
D1TRI=(s1tri/3)**0.5

D2QUA=(s2qua/3)**0.5
D2SEN=(s2sen/3)**0.5
D2TRI=(s2tri/3)**0.5
    
D3QUA=(s3qua/3)**0.5
D3SEN=(s3sen/3)**0.5
D3TRI=(s3tri/3)**0.5

print('------Médias-----------\n'
      'ONDAS QUADRADAS\n'
      '8 volts=',m1q,'\n'
      '9 volts=',m2q,'\n'
      '10 volts=',m3q,'\n\n'
      'ONDAS SENOIDAIS\n'
      '8 volts=',m1s,'\n'
      '9 volts=',m2s,'\n'
      '10 volts=',m3s,'\n\n'
      'ONDAS TRIANGULARES\n'
      '8 volts=',m1t,'\n'
      '9 volts=',m2t,'\n'
      '10 volts=',m3t,'\n\n'
      '------Desvio padrão------\n'
      'ONDAS QUADRADAS\n'
      '8 volts=',D1QUA,'\n'
      '9 volts=',D2QUA,'\n'
      '10 volts=',D3QUA,'\n\n'
      'ONDAS SENOIDAIS\n'
      '8 volts=',D1SEN,'\n'
      '9 volts=',D2SEN,'\n'
      '10 volts=',D3SEN,'\n\n'
      'ONDAS TRIANGULARES\n'
      '8 volts=',D1TRI,'\n'
      '9 volts=',D2TRI,'\n'
      '10 volts=',D3TRI,'\n\n')
print('-----------------------------------------------------------------\n')
print('ITEM 2\n'
      'Produtos entre média de cada tipo de onda de cada voltagem e frequência usada\n'
      'e a respectiva propagação de erro\n\n')
f1=2.99
f2=2.988
f3=3.027

#8 volts
p1q=m1q*f1
delta1q=(((f1**2)*(0.000001**2))+((m1q**2)*(0.001**2)))**0.5

p1s=m1s*f1
delta1s=(((f1**2)*(0.000001**2))+((m1s**2)*(0.001**2)))**0.5

p1t=m1t*f1
delta1t=(((f1**2)*(0.000001**2))+((m1t**2)*(0.001**2)))**0.5

#9 volts    
p2q=m2q*f2
delta2q=(((f2**2)*(0.000001**2))+((m2q**2)*(0.001**2)))**0.5

p2s=m2s*f2
delta2s=(((f2**2)*(0.000001**2))+((m2s**2)*(0.001**2)))**0.5

p2t=m2t*f2
delta2t=(((f2**2)*(0.000001**2))+((m2t**2)*(0.001**2)))**0.5

#10 volts
p3q=m3q*f3
delta3q=(((f3**2)*(0.000001**2))+((m3q**2)*(0.001**2)))**0.5

p3s=m3s*f3
delta3s=(((f3**2)*(0.000001**2))+((m3s**2)*(0.001**2)))**0.5

p3t=m3t*f3
delta3t=(((f3**2)*(0.000001**2))+((m3t**2)*(0.001**2)))**0.5


print('ONDAS QUADRADAS\n'
      '(8 volts frequência = 2,99Hz)\n'
      'produto=',p1q,'propagação de erro=',delta1q,'\n'
      '(9 volts frequência = 2,988Hz )\n'
      'produto=',p2q,'propagação de erro=',delta2q,'\n'
      '(10 volts frequência = 3,027Hz)\n'
      'produto=',p3q,'propagação de erro=',delta3q,'\n\n'

      'ONDAS SENOIDAIS\n'
      '(8 volts frequência = 2,99Hz)\n'
      'produto=',p1s,'propagação de erro=',delta1s,'\n'
      '(9 volts frequência = 2,988Hz )\n'
      'produto=',p2s,'propagação de erro=',delta2s,'\n'
      '(10 volts frequência = 3,027Hz)\n'
      'produto=',p3s,'propagação de erro=',delta3s,'\n\n'

      'ONDAS TRIANGULARES\n'
      '(8 volts frequência = 2,99Hz)\n'
      'produto=',p1t,'propagação de erro=',delta1t,'\n'
      '(9 volts frequência = 2,988Hz )\n'
      'produto=',p2t,'propagação de erro=',delta2t,'\n'
      '(10 volts frequência = 3,027Hz)\n'
      'produto=',p3t,'propagação de erro=',delta3t,'\n\n')

print('-----------------------------------------------------------------\n')
print('ITEM 3 INVERSO DA MÉDIA\n')
inm1q= 1/m1q
inm1s= 1/m1s
inm1t= 1/m1t

inm2q= 1/m2q
inm2s= 1/m2s
inm2t= 1/m2t

inm3q= 1/m3q
inm3s= 1/m3s
inm3t= 1/m3t
print('ONDAS QUADRADAS\n'
      '8 volts=',inm1q,'\n'
      '9 volts=',inm2q,'\n'
      '10 volts=',inm3q,'\n\n'

      'ONDAS SENOIDAIS\n'
      '8 volts=',inm1s,'\n'
      '9 volts=',inm2s,'\n'
      '10 volts=',inm3s,'\n\n'

      'ONDAS TRIANGULARES\n'
      '8 volts=',inm1t,'\n'
      '9 volts=',inm2t,'\n'
      '10 volts=',inm3t,'\n\n')

print('-----------------------------------------------------------------\n')
print('ITEM 10 MÉDIA DOS PRODUTOS PARA CADA VOLTAGEM\n')
quadrada=[]
senoidal=[]
triangular=[]

quadrada.append(p1q)
quadrada.append(p2q)
quadrada.append(p3q)

senoidal.append(p1s)
senoidal.append(p2s)
senoidal.append(p3s)

triangular.append(p1t)
triangular.append(p2t)
triangular.append(p3t)

MQUA=sum(quadrada)/3
MSEN=sum(senoidal)/3
MTRI=sum(triangular)/3

print('ONDA QUADRADA =',MQUA,'\n'
      'ONDA SENOIDAL =',MSEN,'\n'
      'ONDA TRIANGULAR =',MTRI,'\n')

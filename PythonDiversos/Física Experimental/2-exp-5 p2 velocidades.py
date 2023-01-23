xi=0.15
yi=0.12
cos=(3**0.5)/2
sen=0.5
g=10

lv=[2.26,2.26,2.26]
tv=[1.427087,0.954714,0.932392]
velx=[]
vely=[]
v_y=[]
acel=[]

v0=[]
print('Bola verde\n')
for tudo in range(0,3):

    vo=(lv[tudo]+xi)/(cos*(tv[tudo]))

    vx=(vo*cos)
    vy=(vo*sen)
    a=(yi+(vo*sen*(tv[tudo])))/(((tv[tudo])**2)/2)
    vyy=vy - a*(tv[tudo])
    
    v_y.append(vyy)
    velx.append(vx)
    vely.append(vy)
    v0.append(vo)
    acel.append(a)
    print('Velocidades iniciais=',vo,'m/s\n'
          'Velocidades na componenete x=',vx,'m/s\n'
          'Velocidade inicial na componente y=',vy,'m/s\n'
          'Velocidade em y=',vyy,'m/s\n'
          'Aceleração=',a,'m/s^2\n\n' )
mvi=sum(v0)/3
mvx=sum(velx)/3
mviy=sum(vely)/3
ma=sum(acel)/3
mvyy=sum(v_y)/3

dvi=0
dvx=0
dviy=0
dv=0
da=0
dyy=0
for tudo in range(0,3):
    D1=(v0[tudo]-mvi)**2
    dvi+=D1
    D2=(velx[tudo] - mvx)**2
    dvx+=D2
    D3=(vely[tudo] - mviy)**2
    dviy+=D3
    D4=(acel[tudo]-ma)**2
    da+=D4
    D5=(v_y[tudo] - mvyy)**2
    dyy+=D5
d1=(dvi/3)**0.5
d2=(dvx/3)**0.5
d3=(dviy/3)**0.5
d4=(da/3)**0.5
d5=(dyy/3)**0.5
print('Média das velocidades inicias=',mvi,'m/s\n'
      'Média das velocidades em x=',mvx,'m/s\n'
      'Média das velocidades iniciais em y=',mviy,'m/s\n'
      'Média das acelerações=',ma,'m/s^2\n\n'
      'Desvio padrão das velocidades iniciais=',d1,'m/s\n'
      'Desvio padrão das velocidades em x=',d2,'m/s\n'
      'Desvio padrão das velocidades iniciais em y=',d3,'m/s\n'
      'Desvio padrão das velocidades em y=',d5,'m/s\n'
      'Desvio padrão das acelerações=',d4,'m/s^2\n')







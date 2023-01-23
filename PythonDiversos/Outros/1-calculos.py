a=[1.619086,3.364158,5.142604]
b=[1.636219,1.524609,1.439472]
c=[0.765842,0.187397,0.188228]
d=[0.240043,0.386661,0.122564]

ac1=[]
ac2=[]
ac3=[]
ac4=[]
pe1=[]
pe2=[]
pe3=[]
pe4=[]
print('ITEM 1, ACELERAÇÕES E PROPAGAÇÃO DE ERRO\n')

for tudo in range(0,3):
    a1=2*1/((a[tudo])**2)
    a2=2*1/((b[tudo])**2)
    a3=2*1/((c[tudo])**2)
    a4=2*1/((d[tudo])**2)

    da1=((2/(a[tudo]**2))**2)*((0.0005)**2)  +  ((4*1/(a[tudo]**3))**2)*((0.000001)**2)
    da2=((2/(b[tudo]**2))**2)*((0.0005)**2)  +  ((4*1/(b[tudo]**3))**2)*((0.000001)**2)
    da3=((2/(c[tudo]**2))**2)*((0.0005)**2)  +  ((4*1/(c[tudo]**3))**2)*((0.000001)**2)
    da4=((2/(d[tudo]**2))**2)*((0.0005)**2)  +  ((4*1/(d[tudo]**3))**2)*((0.000001)**2)

    da1=(da1)**0.5
    da2=(da2)**0.5
    da3=(da3)**0.5
    da4=(da4)**0.5

    pe1.append(da1)
    pe2.append(da2)
    pe3.append(da3)
    pe4.append(da4)
    
    ac1.append(a1)
    ac2.append(a2)
    ac3.append(a3)
    ac4.append(a4)
    print('Aceleração para o sistema (2,5 volts)=',a1,' m/s^2\n'
          'Propagação de erro=',da1,' m/s^2\n\n'
          'Aceleração para o sistema (5 volts)=',a2,' m/s^2\n'
          'Propagação de erro=',da2,' m/s^2\n\n'
          'Aceleração para o sistema (7,5 volts)=',a3,' m/s^2\n'
          'Propagação de erro=',da3,' m/s^2\n\n'
          'Aceleração para o sistema (10 volts)=',a4,' m/s^2\n'
          'Propagação de erro=',da4,' m/s^2\n')

print('---------------------------------------------------------------\n')
print('ITEM 2 - VELOCIDADES E PROPAGAÇÃO DE ERROS.\n')
va=[]
vb=[]
vc=[]
vd=[]

deltava=[]
deltavb=[]
deltavc=[]
deltavd=[]
for tudo in range(0,3):
    v1=1/(a[tudo])
    v2=1/(b[tudo])
    v3=1/(c[tudo])
    v4=1/(d[tudo])

    va.append(v1)
    vb.append(v2)
    vc.append(v3)
    vd.append(v4)


    dva=(((1/(a[tudo]**2))**2)*((0.000001)**2) + ((1/a[tudo])**2)*((0.0005)**2))**0.5
    dvb=(((1/(b[tudo]**2))**2)*((0.000001)**2) + ((1/b[tudo])**2)*((0.0005)**2))**0.5
    dvc=(((1/(c[tudo]**2))**2)*((0.000001)**2) + ((1/c[tudo])**2)*((0.0005)**2))**0.5
    dvd=(((1/(d[tudo]**2))**2)*((0.000001)**2) + ((1/d[tudo])**2)*((0.0005)**2))**0.5

    deltava.append(dva)
    deltavb.append(dvb)
    deltavc.append(dvc)
    deltavd.append(dvd)


    print('Velocidade (2,5 volts)=',v1,'m/s\n'
          'Propagação de erro=',dva,'m/s\n\n'
          
          'Velocidade (5 volts)=',v2,'m/s\n'
          'Propagação de erro=',dvb,'m/s\n\n'
          
          'Velocidade(7,5 volts)=',v3,'m/s\n'
          'Propagação de erro=',dvc,'m/s\n\n'

          'Velocidade(10 volts)=',v4,'m/s\n'
          'Propagação de erro=',dvd,'m/s\n')


print('---------------------------------------------------------------\n')
print('ITEM 3 - MÉDIA E DESVIO PADRÃO DAS ACELERAÇÕES\n')
m1=sum(ac1)/3
m2=sum(ac2)/3
m3=sum(ac3)/3
m4=sum(ac4)/3

des1=0
des2=0
des3=0
des4=0
for tudo in range(0,3):
    d1=(ac1[tudo]-m1)**2
    d2=(ac2[tudo]-m2)**2
    d3=(ac3[tudo]-m3)**2
    d4=(ac4[tudo]-m4)**2

    des1+=d1
    des2+=d2
    des3+=d3
    des4+=d4
    
D1=(des1/3)**0.5
D2=(des2/3)**0.5
D3=(des3/3)**0.5
D4=(des4/3)**0.5

print('Desvio padrão (2,5 volts)=',D1,'\n'
      'Média=',m1,'\n\n'
      'Desvio padrão (5 volts)=',D2,'\n'
      'Média=',m2,'\n\n'
      'Desvio padrão (7,5 volts)=',D3,'\n'
      'Média=',m3,'\n\n'
      'Desvio padrão (10 volts)=',D4,'\n'
      'Média=',m4,'\n\n')

print('---------------------------------------------------------------\n')
print('ITEM 4 - MÉDIA E DESVIO PADRÃO DAS VELOCIDADES.\n')
mv1=sum(va)/3
mv2=sum(vb)/3
mv3=sum(vc)/3
mv4=sum(vd)/3

desm1=0
desm2=0
desm3=0
desm4=0
for tudo in range(0,3):
    dm1=(va[tudo]-mv1)**2
    dm2=(vb[tudo]-mv2)**2
    dm3=(vc[tudo]-mv3)**2
    
    dm4=(vd[tudo]-mv4)**2

    desm1+=dm1
    desm2+=dm2
    desm3+=dm3
    desm4+=dm4
DVA=(desm1/3)**0.5
DVB=(desm2/3)**0.5
DVC=(desm3/3)**0.5
DVD=(desm4/3)**0.5

print('Desvio padrão (2,5 volts)=',DVA,'m/s\n'
      'Média=',mv1,'m/s\n\n'

      'Desvio padrão (5 volts)=',DVB,'m/s\n'
      'Média=',mv2,'m/s\n\n'

      'Desvio padrão (7,5 volts)=',DVC,'m/s\n'
      'Média=',mv3,'m/s\n'

      'Desvio padrão (10 volts)=',DVD,'m/s\n'
      'Média=',mv4,'m/s\n')

print('---------------------------------------------------------------\n')
print('ITEM 5 - FORÇA E PROPAGAÇÃO DE ERRO.\n')
f1=[]
f2=[]
f3=[]
f4=[]

pfa=[]
pfb=[]
pfc=[]
pfd=[]

for tudo in range(0,3):
    fa=0.01*ac1[tudo]
    fb=0.01*ac2[tudo]
    fc=0.01*ac3[tudo]
    fd=0.01*ac4[tudo]

    f1.append(fa)
    f2.append(fb)
    f3.append(fc)
    f4.append(fd)

    deltafa=((((ac1[tudo])**2)*((0.00001)**2)) + (((0.01)**2)*((pe1[tudo])**2)))**0.5
    deltafb=((((ac2[tudo])**2)*((0.00001)**2)) + (((0.01)**2)*((pe2[tudo])**2)))**0.5
    deltafc=((((ac3[tudo])**2)*((0.00001)**2)) + (((0.01)**2)*((pe3[tudo])**2)))**0.5
    deltafd=((((ac4[tudo])**2)*((0.00001)**2)) + (((0.01)**2)*((pe4[tudo])**2)))**0.5

    pfa.append(deltafa)
    pfb.append(deltafb)
    pfc.append(deltafc)
    pfd.append(deltafd)

    print('Força resultante (2,5 volts)=',fa,'N\n'
          'Propagação de erro=',deltafa,'N\n'

          'Força resultante (5 volts)=',fb,'N\n'
          'Propagação de erro=',deltafb,'N\n'

          'Força resultante (7,5 volts)=',fc,'N\n'
          'Propagação de erro=',deltafc,'N\n'

          'Força resultante (10 volts)=',fd,'\n'
          'Propagação de erro=',deltafd,'N\n')


print('---------------------------------------------------------------\n')
print('ITEM 6 - MÉDIA DAS FORÇAS.\n')
mf1=sum(f1)/3
mf2=sum(f2)/3
mf3=sum(f3)/3
mf4=sum(f4)/3


df1=0
df2=0
df3=0
df4=0
for tudo in range(0,3):
    desf1=(f1[tudo] - mf1)**2
    desf2=(f2[tudo] - mf2)**2
    desf3=(f3[tudo] - mf3)**2
    desf4=(f4[tudo] - mf4)**2

    df1+=desf1
    df2+=desf2
    df3+=desf3
    df4+=desf4

DF1=(df1/3)**0.5
DF2=(df2/3)**0.5
DF3=(df3/3)**0.5
DF4=(df4/3)**0.5

print('Média (2,5 volts)=',mf1,'N\n'
      'Desvio padrão=',DF1,'N\n'

      'Média (5 volts)=',mf2,'N\n'
      'Desvio padrão=',DF2,'N\n'

      'Média (7,5 volts)=',mf3,'N\n'
      'Desvio padrão=',DF3,'N\n'

      'Média (10 volts)=',mf4,'N\n'
      'Desvio padrão=',DF4,'N\n')

print('---------------------------------------------------------------\n')
print('ITEM 10 - COVARIÂNCIA MÉDIA DAS FORÇAS E VOLTAGEM APLICADA.\n')

forcas=[mf1,mf2,mf3,mf4]
volt=[2.5,5,7.5,10]
media1=sum(forcas)/4
media2=sum(volt)/4

s=0
for tudo in range(0,4):
    x=((forcas[tudo] - media1) * (volt[tudo] - media2))
    s+=x
cov=s/4

print('A covariância entre a média das forças e a voltagem aplicada é:'
      ,cov)

print('---------------------------------------------------------------\n')
print('ITEM 1, ACELERAÇÕES E PROPAGAÇÃO DE ERRO, MÉDIA E DESVIO PADRÃO\n')


VEL1=[]
VEL2=[]
VEL3=[]
VEL4=[]

for tudo in range(0,3):
    vel1=ac1[tudo] * a[tudo]
    vel2=ac2[tudo] * b[tudo]
    vel3=ac3[tudo] * c[tudo]
    vel4=ac4[tudo] * d[tudo]

    VEL1.append(vel1)
    VEL2.append(vel2)
    VEL3.append(vel3)
    VEL4.append(vel4)

    dvel1=(((a[tudo]**2)*(pe1[tudo]**2)) + ((ac1[tudo]**2)*(0.000001**2)))**0.5
    dvel2=(((b[tudo]**2)*(pe2[tudo]**2)) + ((ac2[tudo]**2)*(0.000001**2)))**0.5
    dvel3=(((c[tudo]**2)*(pe3[tudo]**2)) + ((ac3[tudo]**2)*(0.000001**2)))**0.5
    dvel4=(((d[tudo]**2)*(pe4[tudo]**2)) + ((ac4[tudo]**2)*(0.000001**2)))**0.5
    
    print('Velocidade (2,5 volts)=',vel1,'m/s\n'
          'Propagação de erro=',dvel1,'m/s\n\n'

          'Velocidade (5 volts)=',vel2,'m/s\n'
          'Propagação de erro=',dvel2,'m/s\n\n'

          'Velocidade (7,5 volts)=',vel3,'m/s\n'
          'Propagação de erro=',dvel3,'m/s\n\n'

          'Velocidade (10 volts)=',vel4,'m/s\n'
          'Propagação de erro=',dvel4,'m/s\n\n')

mediav1=sum(VEL1)/3
mediav2=sum(VEL2)/3
mediav3=sum(VEL3)/3
mediav4=sum(VEL4)/3

print('Média (2,5 volts)=',mediav1,'m/s\n\n'
      'Média (5 volts)=',mediav2,'m/s\n\n'
      'Média (7,5 volts)=',mediav3,'m/s\n\n'
      'Média (10 volts)=',mediav4,'m/s\n\n')
dpv1=0
dpv2=0
dpv3=0
dpv4=0

for tudo in range(0,3):
    dp1=(VEL1[tudo] - mediav1)**2
    dp2=(VEL2[tudo] - mediav2)**2
    dp3=(VEL3[tudo] - mediav3)**2
    dp4=(VEL4[tudo] - mediav4)**2

    dpv1+=dp1
    dpv2+=dp2
    dpv3+=dp3
    dpv4+=dp4
DPV1=(dpv1/3)**0.5
DPV2=(dpv2/3)**0.5
DPV3=(dpv3/3)**0.5
DPV4=(dpv4/3)**0.5

print('Desvio padrão (2,5 volts)=',DPV1,'m/s\n\n'
      'Desvio padrão (5 volts)=',DPV2,'m/s\n\n'
      'Desvio padrão (7,5 volts)=',DPV3,'m/s\n\n'
      'Desvio padrão (10 volts)=',DPV4,'m/s\n\n')


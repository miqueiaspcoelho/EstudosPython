#i=10g e 20g/  #/j=10g e 50g/    #k=50g e 100g
print('ITEM 1 - ACELERAÇÕES E PROPAGAÇÃO DE ERRO.\n')
pi=[0.216527,0.097743,0.261593]
pj=[0.207956,0.0895265,0.115422]
pk=[0.14602,0.152179,0.105441]

a=0.01
b=0.02
c=0.05
d=0.1003
g=9.8

ac1=[]
ac2=[]
ac3=[]
pe1=[]
pe2=[]
pe3=[]

for tudo in range(0,3):
    a1=2*0.07/((pi[tudo])**2)
    a2=2*0.07/((pj[tudo])**2)
    a3=2*0.07/((pk[tudo])**2)

    da1=((2/(pi[tudo]**2))**2)*((0.0005)**2)  +  ((4*0.07/(pi[tudo]**3))**2)*((0.000001)**2)
    da2=((2/(pj[tudo]**2))**2)*((0.0005)**2)  +  ((4*0.07/(pj[tudo]**3))**2)*((0.000001)**2)
    da3=((2/(pk[tudo]**2))**2)*((0.0005)**2)  +  ((4*0.07/(pk[tudo]**3))**2)*((0.000001)**2)

    da1=(da1)**0.5
    da2=(da2)**0.5
    da3=(da3)**0.5

    pe1.append(da1)
    pe2.append(da2)
    pe3.append(da3)
    
    ac1.append(a1)
    ac2.append(a2)
    ac3.append(a3)
    print('Aceleração para o sistema (10g-20g)=',a1,' m/s^2\n'
          'Propagação de erro=',da1,' m/s^2\n\n'
          'Aceleração para o sistema (10g-50g)=',a2,' m/s^2\n'
          'Propagação de erro=',da2,' m/s^2\n\n'
          'Aceleração para o sistema (50g-100g)=',a3,' m/s^2\n'
          'Propagação de erro=',da3,' m/s^2\n')

print('---------------------------------------------------------------\n')
print('ITEM 2 - FORÇA RESULTANTE SOBRE OS BLOCOS\n')
fi=[]
fj=[]
fk=[]
deltafi=[]
deltafj=[]
deltafk=[]
for tudo in range(0,3):
    f1=0.03 * (ac1[tudo])
    f2=0.06 * (ac2[tudo])
    f3=0.1503 * (ac3[tudo])

    fi.append(f1)
    fj.append(f2)
    fk.append(f3)

    df1=((2*((ac1[tudo])**2))*(pe1[tudo])**2 + ((0.03)**2)*(0.00001)**2)**0.5
    df2=((2*((ac2[tudo])**2))*(pe2[tudo])**2 + ((0.06)**2)*(0.00001)**2)**0.5
    df3=((2*((ac3[tudo])**2))*(pe3[tudo])**2 + ((0.1503)**2)*(0.00001)**2)**0.5

    deltafi.append(df1)
    deltafj.append(df2)
    deltafk.append(df3)

    print('Força resultante (10g-20g)=',f1,'N\n'
          'Propagação de erro=',df1,'N\n\n'
          
          'Força reultante (10g-50g)=',f2,'N\n'
          'Propagação de erro=',df2,'N\n\n'
          
          'Força resultante (50g-100g)=',f3,'N\n'
          'Propagação de erro=',df3,'N\n')

print('---------------------------------------------------------------\n')
print('ITEM 3 - MÉDIA E DESVIO PADRÃO DAS ACELERAÇÕES\n')
m1=sum(ac1)/3
m2=sum(ac2)/3
m3=sum(ac3)/3

des1=0
des2=0
des3=0
for tudo in range(0,3):
    d1=(ac1[tudo]-m1)**2
    d2=(ac2[tudo]-m2)**2
    d3=(ac3[tudo]-m3)**2

    des1+=d1
    des2+=d2
    des3+=d3
    
D1=(des1/3)**0.5
D2=(des2/3)**0.5
D3=(des3/3)**0.5

print('Desvio padrão (10g-20g)=',D1,'\n'
      'Média=',m1,'\n\n'
      'Desvio padrão (10g-50g)=',D2,'\n'
      'Média=',m2,'\n\n'
      'Desvio padrão (50g-100g)=',D3,'\n'
      'Média=',m3,'\n\n')
print('---------------------------------------------------------------\n')
print('ITEM 4 - VELOCIDADES E PROPAGAÇÃO DE ERROS.\n')
vi=[]
vj=[]
vk=[]

deltavi=[]
deltavj=[]
deltavk=[]
for tudo in range(0,3):
    v1=0.07/(pi[tudo])
    v2=0.07/(pj[tudo])
    v3=0.07/(pk[tudo])

    vi.append(v1)
    vj.append(v2)
    vk.append(v3)

    dvi=(((0.07/(pi[tudo]**2))**2)*((0.000001)**2) + ((1/pi[tudo])**2)*((0.0005)**2))**0.5
    dvj=(((0.07/(pj[tudo]**2))**2)*((0.000001)**2) + ((1/pj[tudo])**2)*((0.0005)**2))**0.5
    dvk=(((0.07/(pk[tudo]**2))**2)*((0.000001)**2) + ((1/pk[tudo])**2)*((0.0005)**2))**0.5

    deltavi.append(dvi)
    deltavj.append(dvj)
    deltavk.append(dvk)

    print('Velocidade (10g-20g)=',v1,'m/s\n'
          'Propagação de erro=',dvi,'m/s\n\n'
          
          'Velocidade (10g-50g)=',v2,'m/s\n'
          'Propagação de erro=',dvj,'m/s\n\n'
          
          'Velocidade(50g-100g)=',v3,'m/s\n'
          'Propagação de erro=',dvk,'m/s\n')

print('---------------------------------------------------------------\n')
print('ITEM 5 - MÉDIA E DESVIO PADRÃO DAS VELOCIDADES.\n')
mv1=sum(vi)/3
mv2=sum(vj)/3
mv3=sum(vk)/3

desm1=0
desm2=0
desm3=0
for tudo in range(0,3):
    dm1=(vi[tudo]-mv1)**2
    dm2=(vj[tudo]-mv2)**2
    dm3=(vk[tudo]-mv3)**2

    desm1+=dm1
    desm2+=dm2
    desm3+=dm3
DVI=(desm1/3)**0.5
DVJ=(desm2/3)**0.5
DVK=(desm3/3)**0.5

print('Desvio padrão (10g-20g)=',DVI,'m/s\n'
      'Média=',mv1,'m/s\n\n'

      'Desvio padrão (10g-50g)=',DVJ,'m/s\n'
      'Média=',mv2,'m/s\n\n'

      'Desvio padrão (50g-100g)=',DVK,'m/s\n'
      'Média=',mv3,'m/s\n')
print('---------------------------------------------------------------\n')
print('ITEM 6 - GRAVIDADE E PROPAGAÇÃO DE ERROS.\n')
gi=[]
gj=[]
gk=[]

deltagi=[]
deltagj=[]
deltagk=[]
for tudo in range(0,3):
    g1=(ac1[tudo]*(0.03))/0.01
    g2=(ac2[tudo]*(0.06))/0.04
    g3=(ac3[tudo]*(0.1503))/0.0503

    gi.append(g1)
    gj.append(g2)
    gk.append(g3)

    dg1=(((0.03/0.01)**2)*(pe1[tudo])**2 + (((2*ac1[tudo]*0.02)/(0.01**2))**2)*(0.00001)**2 + (((2*ac1[tudo]*0.01)/(0.01**2))**2)*(0.00001)**2)**0.5
    dg2=(((0.06/0.04)**2)*(pe2[tudo])**2 + (((2*ac2[tudo]*0.05)/(0.04**2))**2)*(0.00001)**2 + (((2*ac2[tudo]*0.01)/(0.04**2))**2)*(0.00001)**2)**0.5
    dg3=(((0.1503/0.0503)**2)*(pe3[tudo])**2 + (((2*ac3[tudo]*0.1003)/(0.0503**2))**2)*(0.00001)**2 + (((2*ac3[tudo]*0.05)/(0.0503**2))**2)*(0.00001)**2)**0.5

    deltagi.append(dg1)
    deltagj.append(dg2)
    deltagk.append(dg3)
    print('Gravidade (10g-20g)=',g1,'m/s^2\n'
          'Propagação de erro=',dg1,'m/s^2\n\n'

          'Gravidade (10g-50g)=',g2,'m/s^2\n'
          'Propagação de erro=',dg2,'m/s^2\n\n'

          'Gravidade (50g-100g)=',g3,'m/s^2\n'
          'Propagação de erro=',dg3,'m/s^2\n')
print('---------------------------------------------------------------\n')
print('ITEM 7 - MÉDIA E DESVIO PADRÃO DA GRAVIDADE.\n')
mgi=sum(gi)/3
mgj=sum(gj)/3
mgk=sum(gk)/3

desg1=0
desg2=0
desg3=0
for tudo in range(0,3):
    dgi=(gi[tudo]-mgi)**2
    dgj=(gj[tudo]-mgj)**2
    dgk=(gk[tudo]-mgk)**2

    desg1+=dgi
    desg2+=dgj
    desg3+=dgk
DGI=(desg1/3)**0.5
DGJ=(desg2/3)**0.5
DGK=(desg3/3)**0.5

print('Desvio padrão (10g-20g)=',DGI,'\n'
      'Média=',mgi,'\n\n'

      'Desvio padrão (10g-50g)=',DGJ,'\n'
      'Média=',mgj,'\n\n'

      'Desvio padrão (50g-100g)=',DGK,'\n'
      'Média=',mgk,'\n')

print('---------------------------------------------------------------\n')
print('ITEM 9 - RAZÕES (DESVIO/MÉDIA) E (DESVIO/DESVIO PADRÃO).\n')
for tudo in range(0,3):
    rdma1=(ac1[tudo]-m1)/m1
    rdma2=(ac2[tudo]-m2)/m2
    rdma3=(ac3[tudo]-m3)/m3

    rddpa1=(ac1[tudo]-m1)/D1
    rddpa2=(ac2[tudo]-m2)/D2
    rddpa3=(ac3[tudo]-m3)/D3

    rdmv1=(vi[tudo]-mv1)/mv1
    rdmv2=(vj[tudo]-mv2)/mv2
    rdmv3=(vk[tudo]-mv3)/mv3

    rddpv1=(vi[tudo]-mv1)/DVI
    rddpv2=(vj[tudo]-mv2)/DVJ
    rddpv3=(vk[tudo]-mv3)/DVK

    rdmg1=(gi[tudo]-mgi)/mgi
    rdmg2=(gj[tudo]-mgj)/mgj
    rdmg3=(gk[tudo]-mgk)/mgk

    rddpg1=(gi[tudo]-mgi)/DGI
    rddpg2=(gi[tudo]-mgi)/DGJ
    rddpg3=(gi[tudo]-mgi)/DGK

    print('Sistema 1 (10g-20g)\n'
          'Razão entre desvio e média da aceleração=',rdma1,'\n'
          'Razão entre desvio e desvio padrão da aceleração=',rddpa1,'\n'
          'Razão entre desvio e média da velocidade=',rdmv1,'\n'
          'Razão entre desvio e desvio padrão da velocidade=',rddpv1,'\n'
          'Razão entre desvio e média da gravidade=',rdmg1,'\n'
          'Razão entre desvio e desvio padrão da gravidade=',rddpg1,'\n\n'

          'Sistema 2 (10g-50g)\n'
          'Razão entre desvio e média da aceleração=',rdma2,'\n'
          'Razão entre desvio e desvio padrão da aceleração=',rddpa2,'\n'
          'Razão entre desvio e média da velocidade=',rdmv2,'\n'
          'Razão entre desvio e desvio padrão da velocidade=',rddpv2,'\n'
          'Razão entre desvio e média da gravidade=',rdmg2,'\n'
          'Razão entre desvio e desvio padrão da gravidade=',rddpg2,'\n\n'

          'Sistema 3 (50g-100g)\n'
          'Razão entre desvio e média da aceleração=',rdma3,'\n'
          'Razão entre desvio e desvio padrão da aceleração=',rddpa3,'\n'
          'Razão entre desvio e média da velocidade=',rdmv3,'\n'
          'Razão entre desvio e desvio padrão da velocidade=',rddpv3,'\n'
          'Razão entre desvio e média da gravidade=',rdmg3,'\n'
          'Razão entre desvio e desvio padrão da gravidade=',rddpg3,'\n\n')





'''
print('---------------------------------------------------------------\n'
      'Aceleração com base na análise de um sistema de tensão e polia.\n')
import math
acel1=((b-a)*g)/(b+a)
print('Aceleração do sistema 10g e 20g(a aceleração é igual para os dois blocos)=',round(acel1,5),'m/s^2')
acel2=((c-a)*g)/(c+a)
print('Aceleração do sistema 10g e 50g(a aceleração é igual para os dois blocos)=',round(acel2,5),'m/s^2')
acel3=((d-c)*g)/(d+c)
print('Aceleração do sistema 50g e 100g(a aceleração é igual para os dois blocos)=',round(acel3,5),'m/s^2\n')
print('Aceleração com base em tempo de queda e equações relacionando seno e cosseno em radianos\n')




def g_p_r(x):
    r=(x*math.pi)/180
    return r
y=g_p_r(math.pi/2)
o=round(math.cos(y),5)
o_=round(math.sin(y),5)

vel1=[]
vel2=[]
vel3=[]

ace1=[]
ace2=[]
ace3=[]

for tudo in range(0,3):
    v1=(0.07)/(o*pi[tudo])
    v2=(0.07)/(o*pj[tudo])
    v3=(0.07)/(o*pk[tudo])
    
    print('Velocidade para o sistema (10g-20g)=',v1,'\n'
          'Velocidade para o sistema (10g-50g)=',v2,'\n'
          'Velocidade para o sistema (50g e 100g)=',v3,'\n\n')
    vel1.append(v1)
    vel2.append(v2)
    vel3.append(v3)

    A1=(v1*o_*pi[tudo])/((pi[tudo]**2)/2)
    A2=(v2*o_*pj[tudo])/((pj[tudo]**2)/2)
    A3=(v3*o_*pk[tudo])/((pk[tudo]**2)/2)

    print('Aceleração para o sistema (10g-20g)=',A1,'\n'
          'Aceleração para o sistema (10g-50g)=',A2,'\n'
          'Aceleração para o sistema (50g-100g)=',A3,'\n\n')
    ace1.append(A1)
    ace2.append(A2)
    ace3.append(A3)

'''

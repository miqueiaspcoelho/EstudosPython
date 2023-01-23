import math
#angulo formado de cada lançamento
print('ÂNGULOS FORMADOS FORAM CALCULADOS COM A FÓRMULA: (amplitude x 360)/(2 x(pí)x L)\n')
al1=(3*360)/((2*math.pi)*32.5)
al2=(4*360)/((2*math.pi)*32.5)
al3=(5*360)/((2*math.pi)*32.5)
al4=(6*360)/((2*math.pi)*32.5)
print('3cm--Ângulo formado=',al1,'º\n'
      '4cm--Ângulo formado=',al2,'º\n'
      '5cm--Ângulo formado=',al3,'º\n'
      '6cm--Ângulo formado=',al4,'º\n')
print('---------------------------------------------------------\n')
#campo gravitacional para cada período
haste=0.325
g1=[]
g2=[]
g3=[]
g4=[]
lista1=[1.161546,1.160941,1.1626315]
lista2=[1.162244,1.162066,1.162700]
lista3=[1.162539,1.162510,1.162844]
lista4=[1.163151,1.163609,1.163372]
LISTA=lista1+lista2+lista3+lista4
print('PERÍODO E SUA RESPECTIVA GRAVIDADE DADA PELA FÓRMULA:'
      'G=4x(pí)²xL/T²----- aproximação usada pra Pí:',math.pi,'\n')
for todos in range (0,3):
    gravidade1=(4*(math.pi**2)*haste)/(lista1[todos]**2)
    gravidade2=(4*(math.pi**2)*haste)/(lista2[todos]**2)
    gravidade3=(4*(math.pi**2)*haste)/(lista3[todos]**2)
    gravidade4=(4*(math.pi**2)*haste)/(lista4[todos]**2)


    print('3cm --PERÍODO=',lista1[todos],'GRAVIDADE=',gravidade1,'\n'
    '4cm --PERÍODO=',lista2[todos],'GRAVIDADE=',gravidade2,'\n'
    '5cm --PERÍODO=',lista3[todos],'GRAVIDADE=',gravidade3,'\n'
    '6cm --PERIODO=',lista4[todos],'GRAVIDADE=',gravidade4,'\n')

    g1.append(gravidade1)
    g2.append(gravidade2)
    g3.append(gravidade3)
    g4.append(gravidade4)
G=g1+g2+g3+g4
print('-------------------------------------------------------------\n')


#média do período de oscilação
print('MÉDIA DOS PERÍODOS E DA GRAVIDADE, DIVIDIDOS POR LANÇAMENTO\n')
s1=0
s2=0
s3=0
s4=0
for todos in range (0,3):
    s1+=lista1[todos]
    s2+=lista2[todos]
    s3+=lista3[todos]
    s4+=lista4[todos]
m1=s1/3
m2=s2/3
m3=s3/3
m4=s4/3
print('3cm--MÉDIA dos PERÍODOS=',m1,'\n'
'4cm--MÉDIA dos PERÍODOS=',m2,'\n'
'5cm--MÉDIA dos PERÍODOS=',m3,'\n'
'6cm--MÉDIA dos PERÍODOS=',m4,'\n'
'MÉDIA ENTRE TODOS OS PERÍODOS=',(m1+m2+m3+m4)/4,'\n')
#média do campo gravitacional
sg1=0
sg2=0
sg3=0
sg4=0
for todos in range(0,3):
    sg1+=g1[todos]
    sg2+=g2[todos]
    sg3+=g3[todos]
    sg4+=g4[todos]
mg1=sg1/3
mg2=sg2/3
mg3=sg3/3
mg4=sg4/3
print('3cm--MÉDIA DA GRAVIDADE=',mg1,'\n'
      '4cm--MÉDIA DA GRAVIDADE=',mg2,'\n'
      '5cm--MÉDIA DA GRAVIDADE=',mg3,'\n'
      '6cm--MÉDIA DA GRAVIDADE=',mg4,'\n'
      'MÉDIA ENTRE TODAS AS GRAVIDADES=',(mg1+mg2+mg3+mg4)/4,'\n')
print('---------------------------------------------------------')
print('AMPLITUDES DIVIDAS POR LANÇAMENTO\n')
#amplitude dos períodos
am1=(max(lista1) - min(lista1))
am2=(max(lista2) - min(lista2))
am3=(max(lista3) - min(lista3))
am4=(max(lista4) - min(lista4))
AM=(max(LISTA) - min(LISTA))
#amplitude das gravidades
amg1=(max(g1) - min(g1))
amg2=(max(g2) - min(g2))
amg3=(max(g3) - min(g3))
amg4=(max(g4) - min(g4))
AMG=(max(G) - min(G))
print('3cm--AMPLITUDE dos PERÍODOS',am1,'\n'
      '4cm--AMPLITUDE dos PERÍODOS',am2,'\n'
      '5cm--AMPLITUDE dos PERÍODOS',am3,'\n'
      '6cm--AMPLITUDE dos PERÍODOS',am4,'\n'
      'AMPLITUDE ENTRE TODOS OS PERÍODOS JUNTOS',AM,'\n\n'
      '3cm--AMPLITUDE das GRAVIDADES',amg1,'\n'
      '4cm--AMPLITUDE das GRAVIDADES',amg2,'\n'
      '5cm--AMPLITUDE das GRAVIDADES',amg3,'\n'
      '6cm--AMPLITUDE das GRAVIDADES',amg4,'\n'
      'AMPLITUDE ENTRE TODAS AS GRAVIDADES JUNTAS',AMG,'\n')
print('---------------------------------------------------------')
#desvios e seus módulos
print('DESVIOS E MÓDULOS DE DESVIO DE CADA PERÍODO\n')
ds1=0
ds2=0
ds3=0
ds4=0
dsq1=0
dsq2=0
dsq3=0
dsq4=0

for todos in range(0,3):
    d1=(lista1[todos]- m1)
    dq1=d1**2
    dsq1+=dq1
    
    d2=(lista2[todos]- m2)
    dq2=d2**2
    dsq2+=dq2
    
    d3=(lista3[todos]- m3)
    dq3=d3**2
    dsq3+=dq3

    d4=(lista4[todos]- m4)
    dq4=d4**2
    dsq4+=dq4
    print('3cm--DESVIOS DE CADA UM DOS PERÍODOS=',d1,'MÓDULO DE CADA DESVIO=',abs(d1),'\n'
          '4cm--DESVIOS DE CADA UM DOS PERÍODOS=',d2,'MÓDULO DE CADA DESVIO=',abs(d2),'\n'
          '5cm--DESVIOS DE CADA UM DOS PERÍODOS=',d3,'MÓDULO DE CADA DESVIO=',abs(d3),'\n'
          '6cm--DESVIOS DE CADA UM DOS PERÍODOS=',d4,'MÓDULO DE CADA DESVIO=',abs(d4),'\n')
    ds1+=abs(d1)
    ds2+=abs(d2)
    ds3+=abs(d3)
    ds4+=abs(d4)
print('---------------------------------------------------------\n')
print('DESVIO MÉDIO E PADRÃO(QUADRÁTICO) DOS PERÍODOS\n')
#desvio médio dos períodos
D1=ds1/3
D2=ds2/3
D3=ds3/3
D4=ds4/3
print('3cm--DESVIO MÉDIO DOS PERÍODOS=',D1,'\n'
      '4cm--DESVIO MÉDIO DOS PERÍODOS=',D2,'\n'
      '5cm--DESVIO MÉDIO DOS PERÍODOS=',D3,'\n'
      '6cm--DESVIO MÉDIO DOS PERÍODOS=',D4,'\n')
#desvio padrão dos períodos
DP1=(dsq1/3)**0.5
DP2=(dsq2/3)**0.5
DP3=(dsq3/3)**0.5
DP4=(dsq4/3)**0.5
print('3cm--DESVIO PADRÃO(QUADRÁTICO) DOS PERÍODOS=',DP1,'\n'
      '4cm--DESVIO PADRÃO(QUADRÁTICO) DOS PERÍODOS=',DP2,'\n'
      '5cm--DESVIO PADRÃO(QUADRÁTICO) DOS PERÍODOS=',DP3,'\n'
      '6cm--DESVIO PADRÃO(QUADRÁTICO) DOS PERÍODOS=',DP4,'\n')
print('---------------------------------------------------------\n')
print('DESVIOS E MÓDULOS DE DESVIO DE CADA GRAVIDADE\n')
dsg1=0
dsg2=0
dsg3=0
dsg4=0
dsqg1=0
dsqg2=0
dsqg3=0
dsqg4=0

    
for todos in range(0,3):
    
    dg1=(g1[todos] - mg1)
    dqg1=dg1**2
    dsqg1+=dqg1
    
    dg2=(g2[todos] - mg2)
    dqg2=dg2**2
    dsqg2+=dqg2
    
    dg3=(g3[todos] - mg3)
    dqg3=dg3**2
    dsqg3+=dqg3
    
    dg4=(g4[todos] - mg4)
    dqg4=dg4**2
    dsqg4+=dqg4
    
    print('3cm--DESVIOS DE CADA UMA DAS GRAVIDADES=',dg1,'MÓDULO DE CADA DESVIO=',abs(dg1),'\n'
          '4cm--DESVIOS DE CADA UMA DAS GRAVIDADES=',dg2,'MÓDULO DE CADA DESVIO=',abs(dg2),'\n'
          '5cm--DESVIOS DE CADA UMA DAS GRAVIDADES=',dg3,'MÓDULO DE CADA DESVIO=',abs(dg3),'\n'
          '6cm--DESVIOS DE CADA UMA DAS GRAVIDADES=',dg4,'MÓDULO DE CADA DESVIO=',abs(dg4),'\n')
    dsg1+=abs(dg1)
    dsg2+=abs(dg2)
    dsg3+=abs(dg3)
    dsg4+=abs(dg4)
print('---------------------------------------------------------\n')
print('DESVIO MÉDIO E PADRÃO(QUADRÁTICO) DAS GRAVIDADES\n')
#desvio médio da gravidade
DG1=dsg1/3
DG2=dsg2/3
DG3=dsg3/3
DG4=dsg4/3
print('3cm--DESVIO MÉDIO DAS GRAVIDADES=',DG1,'\n'
      '4cm--DESVIO MÉDIO DAS GRAVIDADES=',DG2,'\n'
      '5cm--DESVIO MÉDIO DAS GRAVIDADES=',DG3,'\n'
      '6cm--DESVIO MÉDIO DAS GRAVIDADES=',DG4,'\n')

#desvio quadrático (padrão) da gravidade
DPG1=(dsqg1/3)**0.5
DPG2=(dsqg2/3)**0.5
DPG3=(dsqg3/3)**0.5
DPG4=(dsqg4/3)**0.5
print('3cm--DESVIO PADRÃO(QUADRÁTICO) DAS GRAVIDADES=',DPG1,'\n'
      '4cm--DESVIO PADRÃO(QUADRÁTICO) DAS GRAVIDADES=',DPG2,'\n'
      '5cm--DESVIO PADRÃO(QUADRÁTICO) DAS GRAVIDADES=',DPG3,'\n'
      '6cm--DESVIO PADRÃO(QUADRÁTICO) DAS GRAVIDADES=',DPG4,'\n')
print('---------------------------------------------------------\n')
print('VARIÂNCIAS DOS PERÍODOS E GRAVIDADES\n')
#variâncias

vp1=(DP1**2)
vp2=(DP2**2)
vp3=(DP3**2)
vp4=(DP4**2)

print('3cm--VARIÂNCIA DOS PERÍODOS=',vp1,'\n'
      '4cm--VARIÂNCIA DOS PERÍODOS=',vp2,'\n'
      '5cm--VARIÂNCIA DOS PERÍODOS=',vp3,'\n'
      '6cm--VARIÂNCIA DOS PERÍODOS=',vp4,'\n')


vg1=(DPG1**2)
vg2=(DPG2**2)
vg3=(DPG3**2)
vg4=(DPG4**2)
print('3cm--VARIÂNCIA DAS GRAVIDADES=',vg1,'\n'
      '4cm--VARIÂNCIA DAS GRAVIDADES=',vg2,'\n'
      '5cm--VARIÂNCIA DAS GRAVIDADES=',vg3,'\n'
      '6cm--VARIÂNCIA DAS GRAVIDADES=',vg4,'\n')

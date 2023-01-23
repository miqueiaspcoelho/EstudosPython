
import math
pi=math.pi
#valores de período do aprelho 2,5 volts.

pa=[1.3316,1.136091,1.0716]
#valores de período do motor 2,5 volts.
pm=[0.77654,0.809424,0.71322]



print('--------------------------PARA 2,5 VOLTS-------------------------------------------\n')
print('ITEM 1 FREQUÊNCIA ANGULAR E PROPAGAÇÃO DE ERROS (aparelho e motor)\n')
faparelho=[]
eaparelho=[]
fmotor=[]
emotor=[]
z=2*pi
for tudo in range(0,3):
    ap=z/pa[tudo]
    faparelho.append(ap)
    mo=z/pm[tudo]
    fmotor.append(mo)
    
    deltaA=(((z/pa[tudo]**2)**2)*(0.000001**2))**0.5
    deltaM=(((z/pm[tudo]**2)**2)*(0.000001**2))**0.5
    eaparelho.append(deltaA)
    emotor.append(deltaM)
    
    print('Frequência angular do aparelho=',ap,'\n'
          'Propagação de erro do aparelho=',deltaA,'\n'
          'Frequência do motor=',mo,'\n'
          'Propagação de erro do motor=',deltaM,'\n')
    
print('---------------------------------------------------------------------------------------------------')
print('ITEM 2 MÉDIA E DESVIO PADRÃO DA FREQUÊNCIA\n')
mediaA=sum(faparelho)/3
mediaM=sum(fmotor)/3
sa=0
sm=0
for tudo in range(0,3):
   desA=(faparelho[tudo] - mediaA)**2
   desM=(fmotor[tudo] - mediaM)**2
   
   sa+=desA
   sm+=desM
DA=(sa/3)**0.5
DM=(sm/3)**0.5
print('Média da frequência angular do aparelho=',mediaA,'\n'
      'Desvio padrão da frequência angular do aparelho=',DA,'\n'
      'Média da frequência angular do motor=',mediaM,'\n'
      'Desvio padrão da frequência angular do motor=',DM)

print('---------------------------------------------------------------------------------------------------')
print('ITEM 3 RAZÃO ENTRE FREQUÊNCIA ANGULAR DO APARELHO E DO MOTOR\n')
razaoa_m=[]
for tudo in range(0,3):
    razao=faparelho[tudo]/fmotor[tudo]
    razaoa_m.append(razao)
    print('Razão entre:',faparelho[tudo],'/',fmotor[tudo],'=',razao)

print('---------------------------------------------------------------------------------------------------')
print('ITEM 4 MÉDIA E DESVIO PADRÃO DA RAZÃO F.APARELHO/F.MOTOR\n')
m_razao=sum(razaoa_m)/3
sr=0
for tudo in range(0,3):
    desva_m=(razaoa_m[tudo] - m_razao)**2
    sr+=desva_m
DA_M=(sr/3)**0.5
print('Média da razão é=',m_razao,'\n'
      'Desvio padrão da razão=',DA_M)

print('------------------------------------PARA 5 VOLTS------------------------------------------------------\n')
print('ITEM 5 FREQUÊNCIA ANGULAR E PROPAGAÇÃO DE ERROS (aparelho e motor)\n')
#valores de período do aparelho 5 volts.
pa1=[0.720052,0.733429,0.705933]

#valores de período do motor 5 volts.
pm1=[0.381145,0.318327,0.377364]


faparelho1=[]
fmotor1=[]
eaparelho1=[]
emotor1=[]

for tudo in range(0,3):
    ap1=z/pa1[tudo]
    faparelho1.append(ap1)
    mo1=z/pm1[tudo]
    fmotor1.append(mo1)
    
    deltaA1=(((z/pa1[tudo]**2)**2)*(0.000001**2))**0.5
    deltaM1=(((z/pm1[tudo]**2)**2)*(0.000001**2))**0.5
    eaparelho1.append(deltaA1)
    emotor1.append(deltaM1)
    
    print('Frequência angular do aparelho=',ap1,'\n'
          'Propagação de erro do aparelho=',deltaA1,'\n'
          'Frequência do motor=',mo1,'\n'
          'Propagação de erro do motor=',deltaM1,'\n')


print('---------------------------------------------------------------------------------------------------')
print('ITEM 6 MÉDIA E DESVIO PADRÃO DA FREQUÊNCIA\n')
mediaA1=sum(faparelho1)/3
mediaM1=sum(fmotor1)/3
sa1=0
sm1=0
for tudo in range(0,3):
   desA1=(faparelho1[tudo] - mediaA1)**2
   desM1=(fmotor1[tudo] - mediaM1)**2
   
   sa1+=desA1
   sm1+=desM1
DA1=(sa1/3)**0.5
DM1=(sm1/3)**0.5
print('Média da frequência angular do parelho=',mediaA1,'\n'
      'Desvio padrão da frequência angular do aparelho=',DA1,'\n'
      'Média da frequência angular do motor=',mediaM1,'\n'
      'Desvio padrão da frequência angular do motor=',DM1)

print('---------------------------------------------------------------------------------------------------')
print('ITEM 7 RAZÃO ENTRE FREQUÊNCIA ANGULAR DO APARELHO E DO MOTOR\n')
razao1a_m=[]
for tudo in range(0,3):
    razao1=faparelho1[tudo]/fmotor1[tudo]
    razao1a_m.append(razao1)
    print('Razão entre:',faparelho1[tudo],'/',fmotor1[tudo],'=',razao1)

print('---------------------------------------------------------------------------------------------------')
print('ITEM 8 MÉDIA E DESVIO PADRÃO DA RAZÃO F.APARELHO/F.MOTOR\n')
m_razao1=sum(razao1a_m)/3
sr1=0
for tudo in range(0,3):
    desv1a_m=(razao1a_m[tudo] - m_razao1)**2
    sr1+=desv1a_m
D1A_M=(sr1/3)**0.5
print('Média da razão é=',m_razao1,'\n'
      'Desvio padrão da razão=',D1A_M)

print('---------------------------------------------------------------------------------------------------')
print('ITEM 9 COVARIÂNCIA F.APARELHO/F.MOTOR\n')
cov2=0
cov5=0
for tudo in range(0,3):
    c2=(faparelho[tudo] - mediaA)*(fmotor[tudo] - mediaM)
    c5=(faparelho1[tudo] - mediaA1)*(fmotor1[tudo] - mediaM1)
    cov2+=c2
    cov5+=c5
COV2=cov2/3
COV5=cov5/3
print('Coraviância para 2,5 volts=',COV2,'\n'
      'Covariância para 5 volts=',COV5)

print('---------------------------------------------------------------------------------------------------')
print('ERRO TOTAL FREQUÊNCIA ANGULAR\n')
errototal2_5aparelho=[]
errototal2_5motor=[]

errototal5aparelho=[]
errototal5motor=[]
for tudo in range(0,3):
    et2_5aparelho=((DA**2)+(eaparelho[tudo]**2))**0.5
    et2_5motor=((DM**2)+(emotor[tudo]**2))**0.5

    errototal2_5aparelho.append(et2_5aparelho)
    errototal2_5motor.append(et2_5motor)

    et5aparelho=((DA1**2)+(eaparelho1[tudo]**2))**0.5
    et5motor=((DM1**2)+(emotor1[tudo]**2))**0.5

    errototal5aparelho.append(et5aparelho)
    errototal5motor.append(et5motor)
print('Erro total para a frequência de 2,5 volts\n')
print('Erro relacionado ao aparelho (haste)\n')
for tudo in range(0,3):
    print(errototal2_5aparelho[tudo])

print('\nErro relacionado ao motor\n')
for tudo in range(0,3):
    print(errototal2_5motor[tudo])

print('--------------------------------------------------------------------\n')
print('Erro total para a frequência de 5 volts\n')
print('Erro relacionado ao aparelho (haste)\n')
for tudo in range(0,3):
    print(errototal5aparelho[tudo])

print('\nErro relacionado ao motor\n')
for tudo in range(0,3):
    print(errototal5motor[tudo])










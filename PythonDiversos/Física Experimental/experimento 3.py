m1=[0.534007,0.568506,0.701483,0.678405,0.437344]
m1meia=[0.496625,0.464638,0.415051,0.451326,0.421002]
m2=[0.626161,0.607598,0.525210,0.587240,0.599603]
m2meia=[0.403546,0.426037,0.361667,0.383450,0.428052]
h=0.602
h1=0.301
#1 Calcular as acelerações de queda no plano inclinado para cada massa em cada um dos lançamentos.
a1=[]
a1m=[]
a2=[]
a2m=[]
acelerasen=9.8*0.64278760968
print('Aceleração no plano inclinado em fução do seno (a=gxsen(40))='
      ,acelerasen,'\n')
print('----------------------------------------------------------------------\n')
print('ACELERAÇÕES.\n')

 #para 10 gramas
for tudo in range(0,5):
    u1=m1[tudo]
    acelu1=(2*h)/(u1**2)
    a1.append(acelu1)
    print('Aceleração ''10g'' (t)-',u1,'=','(a)=',acelu1)
print('\n')
for tudo in range(0,5):
    um1=m1meia[tudo]
    acelu1m=(2*h1)/(um1**2)
    a1m.append(acelu1m)
    print('Aceleração ''10g'' à meia altura (t)-',um1,'=','(a)=',acelu1m)
print('\n')

 #para 20 gramas
for tudo in range(0,5):
    u2=m2[tudo]
    acelu2=(2*h)/(u2**2)
    a2.append(acelu2)
    print('Aceleração ''20g'' (t)-',u2,'=','(a)=',acelu2)
print('\n')
for tudo in range(0,5):
    um2=m2meia[tudo]
    acelu2m=(2*h1)/(um2**2)
    a2m.append(acelu2m)
    print('Aceleração ''20g'' à meia altura (t)-',um2,'=','(a)=',acelu2m)

print('\n----------------------------------------------------------------------\n')
print('acelerações 10g altura total=',a1)
print('acelerações 20g altura total=',a2)
print('aceleraçõe à meia altura 10g=',a1m)
print('acelerações à meia altura 20g=',a2m)

print('MÉDIAS.\n')
#  2 Calcular os tempos de queda médios e acelerações médias de cada massa.
sm1=0
sm1me=0
sm2=0
sm2me=0

A1=0
A1M=0
A2=0
A2M=0
for tudo in range(0,5):
    #para 10 gramas
    M1=m1[tudo]
    M1ME=m1meia[tudo]
    sm1+=M1
    sm1me+=M1ME
    
    acelera1=a1[tudo]
    A1+=acelera1
    acelera1m=a1m[tudo]
    A1M+=acelera1m
    
    #para 20 gramas
    M2=m2[tudo]
    M2ME=m2meia[tudo]
    sm2+=M1
    sm2me+=M2ME

    acelera2=a2[tudo]
    A2+=acelera2
    acelera2m=a2m[tudo]
    A2M+=acelera2m
print('aqui',a1,a1m,a2,a2m)
#para 10 gramas    
media1=sm1/5
media1m=sm1me/5
media1a=A1/5
media1am=A1M/5

#para 20 gramas
media2=sm2/5
media2m=sm2me/5
media2a=A2/5
media2am=A2M/5

print('\nMédia dos tempos para 10g=',media1,'\n'
      'Média dos tempos à meia altura para 10g=',media1m,'\n\n'
      'Média dos tempos para 20g=',media2,'\n'
      'Média dos tempos à meia altura para 20g=',media2m,'\n\n'
      'Média das acelerações para 10g=',media1a,'\n'
      'Média das acelarações à meia altura para 10g=',media1am,'\n\n'
      'Média das acelerações para 20g=',media2a,'\n'
      'Média das acelerações à meia altura para 20g=',media2am,'\n')

print('\n----------------------------------------------------------------------\n')
# 3  Calcular os desvios do tempo de queda em cada lançamento para cada massa.
print('DESVIOS DOS TEMPOS DE QUE EM MÓDULO.\n')
print('10 gramas\n')
dsm1=0
dsm1m=0
dsmq1=0
dsmq1m=0
for tudo in range(0,5):
    massa1=m1[tudo]
    desvio1=abs(massa1-media1)
    dsm1+=desvio1
    dq1=desvio1**2
    dsmq1+=dq1
    
    print('Desvio=',massa1,'-',media1,'=',desvio1)
print('\n')
for tudo in range(0,5):
    massa1meia=m1meia[tudo]
    desvio1meia=abs(massa1meia-media1m)
    dsm1m+=desvio1meia
    dq1m=desvio1meia**2
    dsmq1m+=dq1m
    print('Desvio à meia altura=',massa1meia,'-',media1m,'=',desvio1meia)
    
    #desvio médio dos tempos
dm1=dsm1/5
dm1m=dsm1m/5
print('\nDesvio médio dos tempos 10g=',dm1,'\n'
      'Desvio médio dos tempos à meia altura 10g=',dm1m,'\n\n')
    #desvio padrão dos tempos
dq1=(dsmq1/5)**0.5
dq1m=(dsmq1m/5)**0.5
print('Desvio padrão dos tempos 10g=',dq1,'\n'
      'Desvio padrão dos tempos à meia altura 10g=',dq1m,'\n')

print('\n----------------------------------------------------------------------\n')

# 4 Calcular os desvios da aceleração em cada lançamento para cada massa.
print('DESVIOS DAS ACELERAÇÕES EM MÓDULO.\n')
dsma1=0
dsmqa1=0

dsma1m=0
dsmqa1m=0
for tudo in range(0,5):
    ac1=a1[tudo]
    desvioa1=abs(ac1-media1a)
    dsma1+=desvioa1
    dqa1=desvioa1**2
    dsmqa1+=dqa1
    
    print('Desvio=',ac1,'-',media1a,'=',desvioa1)
print('\n')
for tudo in range(0,5):
    ac1m=a1m[tudo]
    desvioa1meia=abs(ac1m-media1am)
    dsma1m+=desvioa1meia
    dqa1m=desvioa1meia**2
    dsmqa1m+=dqa1m
    print('Desvio à meia altura=',ac1m,'-',media1am,'=',desvioa1meia)

    #desvio médio das acelerações
dma1=dsma1/5
dma1m=dsma1m/5
print('\nDesvio médio das acelerações 10g=',dma1,'\n'
      'Desvio médio das acelerações à meia altura 10g=',dma1m,'\n\n')

    #desvio padrão das acelerações

dqa1=(dsmqa1/5)**0.5
dqa1m=(dsmqa1m/5)**0.5
print('Desvio padrão das acelerações 10g=',dqa1,'\n'
      'Desvio padrão das acelerações à meia altura 10g=',dqa1m,'\n')
print('\n----------------------------------------------------------------------\n')
print('PARA 20 GRAMAS.\n')
dsm2=0
dsm2m=0
dsmq2=0
dsmq2m=0
for tudo in range(0,5):
    massa2=m2[tudo]
    desvio2=abs(massa2-media2)
    dsm2+=desvio2
    dq2=desvio2**2
    dsmq2+=dq2
    
    print('Desvio=',massa2,'-',media2,'=',desvio2)
print('\n')
for tudo in range(0,5):
    massa2meia=m2meia[tudo]
    desvio2meia=abs(massa2meia-media2m)
    dsm2m+=desvio2meia
    dq2m=desvio2meia**2
    dsmq2m+=dq2m
    print('Desvio à meia altura=',massa2meia,'-',media2m,'=',desvio2meia)
    
    #desvio médio dos tempos
dm2=dsm2/5
dm2m=dsm2m/5
print('\nDesvio médio dos tempos 20g=',dm2,'\n'
      'Desvio médio dos tempos à meia altura 20g=',dm2m,'\n\n')
    #desvio padrão dos tempos
dq2=(dsmq2/5)**0.5
dq2m=(dsmq2m/5)**0.5
print('Desvio padrão dos tempos 20g=',dq2,'\n'
      'Desvio padrão dos tempos à meia altura 10g=',dq2m,'\n')

print('\n----------------------------------------------------------------------\n')
print('DESVIOS DAS ACELERAÇÕES EM MÓDULO.\n')
dsma2=0
dsmqa2=0

dsma2m=0
dsmqa2m=0
for tudo in range(0,5):
    ac2=a2[tudo]
    desvioa2=abs(ac2-media2a)
    dsma2+=desvioa2
    dqa2=desvioa2**2
    dsmqa2+=dqa2
    
    print('Desvio=',ac2,'-',media2a,'=',desvioa2)
print('\n')
for tudo in range(0,5):
    ac2m=a2m[tudo]
    desvioa2meia=abs(ac2m-media2am)
    dsma2m+=desvioa2meia
    dqa2m=desvioa2meia**2
    dsmqa2m+=dqa2m
    print('Desvio à meia altura=',ac2m,'-',media2am,'=',desvioa2meia)

    #desvio médio das acelerações
dma2=dsma2/5
dma2m=dsma2m/5
print('\nDesvio médio das acelerações 20g=',dma2,'\n'
      'Desvio médio das acelerações à meia altura 20g=',dma2m,'\n\n')

    #desvio padrão das acelerações

dqa2=(dsmqa2/5)**0.5
dqa2m=(dsmqa2m/5)**0.5
print('Desvio padrão das acelerações 20g=',dqa2,'\n'
      'Desvio padrão das acelerações à meia altura 10g=',dqa2m,'\n')


# 5 Calcular o desvio padrão da aceleração de cada massa.-tá ok já :D



# 6 Calcular a covariância entre as forças sofridas pelas duas massas.-tá ok já :D



# 7 Calcular a covariância e o coeficiente de Pearson entre o tempo de queda e a aceleração para cada massa.

 

# 8 Calcular a covariância e o coeficiente de Pearson entre o quadrado do tempo de queda e a aceleração para cada massa.



# 9 Calcular a razão entre as forças resultantes de cada massa.



#10 Apresentar um gráfico da aceleração de queda em função do tempo de queda para cada massa.



#11 Apresentar uma tabela com a razão entre a aceleração resultante e o seno do ângulo de inclinação do plano inclinado, para cada massa e lançamento. Incluir as médias dessa razão para cada massa.



#12 Apresentar uma tabela com a razão entre a força resultante e o seno do ângulo de inclinação do plano inclinado, para cada massa e lançamento. Incluir as médias dessa razão para cada massa.

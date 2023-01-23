l1=[0.142,0.145,0.144]
l2=[0.215,0.216,0.218]
l3=[0.182,0.184,0.182]
l4=[0.268,0.272,0.272]
l5=[0.293,0.293,0.293]
l6=[0.312,0.310,0.311]
m1=sum(l1)/3
m2=sum(l2)/3
m3=sum(l3)/3
m4=sum(l4)/3
m5=sum(l5)/3
m6=sum(l6)/3
print('MÉDIA DAS ALTURAS OBSERVADAS (METROS).\n')
print('Média s1==',m1,'\n'
      'Média s2==',m2,'\n'
      'Média s3==',m3,'\n'
      'Média s4==',m4,'\n'
      'Média s5==',m5,'\n'
      'Média s6==',m6,'\n\n')
print('---------------------------------------------\n')
print('DESVIOS, DESVIO MÉDIO E DESVIO PADRÃO DAS ALTURAS OBSERVADAS.\n')
s1=0
s2=0
s3=0
s4=0
s5=0
s6=0

sm1=0
sm2=0
sm3=0
sm4=0
sm5=0
sm6=0
for tudo in range(0,3):
    d1=abs(l1[tudo]-m1)
    sm1+=d1
    dq1=d1**2
    s1+=dq1
    
    d2=abs(l2[tudo]-m2)
    sm2+=d2
    dq2=d2**2
    s2+=dq2
    
    d3=abs(l3[tudo]-m3)
    sm3+=d3
    dq3=d3**2
    s3+=dq3
    
    d4=abs(l4[tudo]-m4)
    sm4+=d4
    dq4=d4**2
    s4+=dq4
    
    d5=abs(l5[tudo]-m5)
    sm5+=d5
    dq5=d5**2
    s5+=dq5
    
    d6=abs(l6[tudo]-m6)
    sm6+=d6
    dq6=d6**2
    s6+=dq6
    print('Desvio s1==',l1[tudo],'-',m1,'=',d1,'\n'
          'Desvio s2==',l2[tudo],'-',m2,'=',d2,'\n'
          'Desvio s3==',l3[tudo],'-',m3,'=',d3,'\n'
          'Desvio s4==',l4[tudo],'-',m4,'=',d4,'\n'
          'Desvio s5==',l5[tudo],'-',m5,'=',d5,'\n'
          'Desvio s6==',l6[tudo],'-',m6,'=',d6,'\n')

dm1=(sm1/3)
dm2=(sm2/3)
dm3=(sm3/3)
dm4=(sm4/3)
dm5=(sm5/3)
dm6=(sm6/3)
print('---------------------------------------------\n')

print('Desvio médio s1=',dm1,'\n'
      'Desvio médio s2=',dm2,'\n'
      'Desvio médio s3=',dm3,'\n'
      'Desvio médio s4=',dm4,'\n'
      'Desvio médio s5=',dm5,'\n'
      'Desvio médio s6=',dm6,'\n\n')

DQ1=(s1/3)**0.5
DQ2=(s2/3)**0.5
DQ3=(s3/3)**0.5
DQ4=(s4/3)**0.5
DQ5=(s5/3)**0.5
DQ6=(s6/3)**0.5
print('---------------------------------------------\n')

print('Desvio padrão s1=',DQ1,'\n'
      'Desvio padrão s2=',DQ2,'\n'
      'Desvio padrão s3=',DQ3,'\n'
      'Desvio padrão s4=',DQ4,'\n'
      'Desvio padrão s5=',DQ5,'\n'
      'Desvio padrão s6=',DQ6,'\n')
print('---------------------------------------------\n')
print('VARIÂNCIAS.\n')
v1=DQ1**2
v2=DQ2**2
v3=DQ3**2
v4=DQ4**2
v5=DQ5**2
v6=DQ6**2
print('Variância (s1)=',v1,'\n'
      'Variância (s2)=',v2,'\n'
      'Variância (s3)=',v3,'\n'
      'Variância (s4)=',v4,'\n'
      'Variância (s5)=',v5,'\n'
      'Variância (s6)=',v6,'\n')

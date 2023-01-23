l1=[0.142,0.145,0.144]
l2=[0.215,0.216,0.218]
l3=[0.182,0.184,0.182]
l4=[0.268,0.272,0.272]
l5=[0.293,0.293,0.293]
l6=[0.312,0.310,0.311]

maximosh=[max(l1),max(l2),max(l3),max(l4),max(l5),max(l6)]
print('alturas máximas atingindas pelo pêndulo=',maximosh)
a=0.1456
b=0.2197
c=0.1831
d=0.2746
e=0.293
f=0.3113
for tudo in range(0,3):
    r1=(a/l1[tudo])
    r2=(b/l2[tudo])
    r3=(c/l3[tudo])
    r4=(d/l4[tudo])
    r5=(e/l5[tudo])
    r6=(f/l6[tudo])

    print('Razão entre hi',a,';hf',l1[tudo],'(s1)=',r1,'\n'
          'Razão entre hi',b,';hf',l2[tudo],'(s2)=',r2,'\n'
          'Razão entre hi',c,';hf',l3[tudo],'(s3)=',r3,'\n'
          'Razão entre hi',d,';hf',l4[tudo],'(s4)=',r4,'\n'
          'Razão entre hi',e,';hf',l5[tudo],'(s5)=',r5,'\n'
          'Razão entre hi',f,';hf',l6[tudo],'(s6)=',r6,'\n\n')
hi=[0.1456,0.2197,0.1831,0.2746,0.293,0.3113]
hf=[0.14366666666666664,0.21633333333333335,0.18266666666666667,0.27066666666666667,0.293,0.311]
C=sum(hi)
D=sum(hf)
media1=C/6
media2=D/6
soma=0
for todos in range (0,6):
    q=hi[todos]
    p=hf[todos]
    e=(q-media1)*(p-media2)
    soma+=e
cov=soma/6
print('Covariância entre as alturas iniciais e finais=',cov)








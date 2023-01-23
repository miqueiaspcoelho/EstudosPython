l1=[0.142,0.145,0.144]
l2=[0.215,0.216,0.218]
l3=[0.182,0.184,0.182]
l4=[0.268,0.272,0.272]
l5=[0.293,0.293,0.293]
l6=[0.312,0.310,0.311]
m=0.3834
g=10

y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
y6=[]

print('ENERGIA POTENCIAL NAS POSIÇÕES FINAIS.\n')
for tudo in range(0,3):
    e1=round(m*g*(l1[tudo]),4)
    y1.append(e1)
    
    e2=round(m*g*(l2[tudo]),4)
    y2.append(e2)
    
    e3=round(m*g*(l3[tudo]),4)
    y3.append(e3)
    
    e4=round(m*g*(l4[tudo]),4)
    y4.append(e4)
    
    e5=round(m*g*(l5[tudo]),4)
    y5.append(e5)
    
    e6=round(m*g*(l6[tudo]),4)
    y6.append(e6)

    print('Energia potencial (s1)==',m,'*',g,'*',l1[tudo],'=',round(e1,4),'\n'
          'Energia potencial (s2)==',m,'*',g,'*',l2[tudo],'=',round(e2,4),'\n'
          'Energia potencial (s3)==',m,'*',g,'*',l3[tudo],'=',round(e3,4),'\n'
          'Energia potencial (s4)==',m,'*',g,'*',l4[tudo],'=',round(e4,4),'\n'
          'Energia potencial (s5)==',m,'*',g,'*',l5[tudo],'=',round(e5,4),'\n'
          'Energia potencial (s6)==',m,'*',g,'*',l6[tudo],'=',round(e6,4),'\n')
Y=y1+y2+y3+y4+y5+y6

print('ENERGIA POTENCIAL NAS POSIÇÕES INICIAIS.\n')
b=[0.1456,0.2197,0.1831,0.2746,0.293,0.3113]
c=[]
for tudo in range(0,6):
    e7=round(m*g*(b[tudo]),4)
    c.append(e7)
    print('Energia na posição==',b[tudo],'=',e7)
b_p=[]
for tudo in range(0,6):
    kk=round((c[tudo])/(m*10),3)
    b_p.append(kk)
print('\nEnergia das posições iniciais divida pelo peso=',b_p)
Y_p=[]
for tudo in range(0,18):
    uu=round((Y[tudo])/(m*10),4)
    Y_p.append(uu)
print('\nEnergia de cada uma das posições finais dividida pelo peso=',Y_p,'\n')

med=[0.143666667,0.216333333,0.182666667,0.270666667,0.293,0.311]
for tudo in range(0,6):
    e8=m*g*(med[tudo])
    print('Enegia de=',round(med[tudo],4),'=',round(e8,4))



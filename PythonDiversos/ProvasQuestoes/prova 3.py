massas=[0.05001,0.05011,0.05008]
voltagens=[2.5,2.51,2.53]
p=[0.840123,0.850993,0.845666]

#1
#a) Média e desvio padrão de cada conjunto.
M1massas=sum(massas)/3
M2vol=sum(voltagens)/3
M3perio=sum(p)/3
s1=0
s2=0
s3=0
for tudo in range(0,3):
    a=(massas[tudo] - 0.05007)**2
    b=(voltagens[tudo] - M2vol)**2
    c=(p[tudo] - 0.845594)**2
    


    s1+=a
    s2+=b
    s3+=c
d=(s3/3)**0.5
'''
print(((0.00001)**2+(0.000042426)**2))
print(((0.03)**2 + (0.012909944)**2)**0.5)
print(((0.000001)**2+(0.004437904)**2)**0.5)
'''
pi=3.141592654
for tudo in range(0,3):
    e=(((2*pi)/(p[tudo]**2))**2+(0.000001**2))**0.5
    f=((e)**2+(0.004437904**2))**0.5
    print(f)



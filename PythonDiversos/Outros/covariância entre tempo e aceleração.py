t1=[0.534007,0.568506,0.701483,0.678405,0.437344]
a1=[4.222139583517754, 3.7252582206235134, 2.446764584138726, 2.6160642544287236, 6.294773987054305]
#covariância entre tempo e aceleração 10 gramas, altura total.

c=sum(t1)
d=sum(a1)
media1=c/5
media2=d/5
soma=0
for todos in range (0,5):
    q=t1[todos]
    p=a1[todos]
    e=(q-media1)*(p-media2)
    soma+=e
cov=soma/5
print('Covariância entre tempo e aceleração (10 gramas e ALTURA TOTAL)=',cov)

#covariância entre tempo e acelração 10 gramas, meia altura.
t1m=[0.496625,0.464638,0.415051,0.451326,0.421002]
a1m=[2.4408401309898955, 2.7884768329166914, 3.49456853432759, 2.955396706996395, 3.3964730526559515]
cc=sum(t1m)
dd=sum(a1m)
media3=cc/5
media4=dd/5
soma1=0
for todos in range (0,5):
    qq=t1m[todos]
    pp=a1m[todos]
    ee=(qq-media3)*(pp-media4)
    soma1+=ee
cov1=soma1/5
print('Covariância entre tempo e aceleração (10 gramas e MEIA ALTURA)=',cov1)

#covariância entre tempo e aceleração 20 gramas, altura total.
t2=[0.626161,0.607598,0.525210,0.587240,0.599603]
a2=[3.0708206905577784, 3.2613230176877854, 4.364761460723557, 3.491364783123542, 3.3488746557589386]
c1=sum(t2)
d1=sum(a2)
media5=c1/5
media6=d1/5
soma2=0
for todos in range (0,5):
    q1=t2[todos]
    p1=a2[todos]
    e1=(q1-media5)*(p1-media6)
    soma2+=e1
cov2=soma2/5
print('Covariância entre tempo e aceleração (20 gramas e ALTURA TOTAL)=',cov2)

#covariância entre o tempo de aceleração 20 gramas, meia altura.
t2m=[0.403546,0.426037,0.361667,0.383450,0.428052]
a2m=[3.6966675694509363, 3.3166668917784534, 4.602340260287568, 4.094293831315536, 3.2855148172352564]
c2=sum(t2m)
d2=sum(a2m)
media7=c2/5
media8=d2/5
soma3=0
for todos in range (0,5):
    q2=t1m[todos]
    p2=a1m[todos]
    e2=(q2-media7)*(pp-media8)
    soma3+=e2
cov3=soma1/5
print('Covariância entre tempo e aceleração (20 gramas e MEIA ALTURA)=',cov3)
#coeficiente de Pearson (covariância dividido pela multiplicação das variâncias)






#calculo das forças e covariâncias
a1t= [4.222139583517754, 3.7252582206235134, 2.446764584138726, 2.6160642544287236, 6.294773987054305]
a2t= [3.0708206905577784, 3.2613230176877854, 4.364761460723557, 3.491364783123542, 3.3488746557589386]
am1= [2.4408401309898955, 2.7884768329166914, 3.49456853432759, 2.955396706996395, 3.3964730526559515]
am2= [3.6966675694509363, 3.3166668917784534, 4.602340260287568, 4.094293831315536, 3.2855148172352564]

f1total=[]
f2total=[]
f1meia=[]
f2meia=[]
for tudo in range(0,5):
  y=a1t[tudo]
  yy=y*0.01
  f1total.append(yy)
  
  z=a2t[tudo]
  zz=z*0.02
  f2total.append(zz)
  
  g=am1[tudo]
  gg=g*0.01
  f1meia.append(gg)

  
  j=am2[tudo]
  jj=j*0.02
  f2meia.append(jj)
  
print('f10t=',f1total,'\n','f20t',f2total,'\n'
      'fm10=',f1meia,'\n','fm20=',f2meia,'\n')

  

#covariância, das totais.
Cf10t= [0.04222139583517755, 0.03725258220623513, 0.02446764584138726, 0.026160642544287238, 0.06294773987054306]
Cf20t= [0.06141641381115557, 0.0652264603537557, 0.08729522921447114, 0.06982729566247084, 0.06697749311517877]
c=sum(Cf10t)
d=sum(Cf20t)
media1=c/5
media2=d/5
soma=0
for todos in range (0,5):
    q=Cf10t[todos]
    p=Cf20t[todos]
    e=(q-media1)*(p-media2)
    soma+=e
cov=soma/5
print('Covariância entre as forças (massas na altura)',cov)
#covariância, das meia altura.
Cfm10= [0.024408401309898957, 0.027884768329166913, 0.0349456853432759, 0.02955396706996395, 0.03396473052655952]
Cfm20= [0.07393335138901873, 0.06633333783556906, 0.09204680520575137, 0.08188587662631072, 0.06571029634470513]
cc=sum(Cfm10)
dd=sum(Cfm20)
media3=cc/5
media4=dd/5
soma1=0
for todos in range (0,5):
    qq=Cfm10[todos]
    pp=Cfm20[todos]
    ee=(qq-media3)*(pp-media4)
    soma1+=ee
cov1=soma1/5
print('Covariância entre as forças (massas à meia altura)',cov1)

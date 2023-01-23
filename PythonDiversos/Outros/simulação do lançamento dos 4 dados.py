print('Simulação do lançamento de 4 dados não viciados e a soma de suas faces\n'
      '10.000 lançamentos\n')
from random import*

a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]
c=[1,2,3,4,5,6]
d=[1,2,3,4,5,6]
s=[]
for x in range(0,10000):
    A=choice(a)
    B=choice(b)
    C=choice(c)
    D=choice(d)
    e=A+B+C+D
    s.append(e)
c4=(s.count(4))
c5=(s.count(5))
c6=(s.count(6))
c7=(s.count(7))
c8=(s.count(8))
c9=(s.count(9))
c10=(s.count(10))
c11=(s.count(11))
c12=(s.count(12))
c13=(s.count(13))
c14=(s.count(14))
c15=(s.count(15))
c16=(s.count(16))
c17=(s.count(17))
c18=(s.count(18))
c19=(s.count(19))
c20=(s.count(20))
c21=(s.count(21))
c22=(s.count(22))
c23=(s.count(23))
c24=(s.count(24))

A=[c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24]
print('Número de vezes que saiu cada soma na simulação\n\n')
print('4=',c4,'5=',c5,'6=',c6,'7=',c7,'8=',c8,'\n'
      '9=',c9,'10=',c10,'11=',c11,'12=',c12,'\n'
      '13=',c13,'14=',c14,'15=',c15,'16=',c16,'\n'
      '17=',c17,'18=',c18,'19=',c19,'20=',c20,'\n'
      '21=',c21,'22=',c22,'23=',c23,'24=',c24,'\n\n')

print('Frequência relativa para cada soma na simulção\n')
soma=0
lista=[]
for tudo in range(0,21):
    f=(A[tudo]/10000)
    lista.append(f)
    soma+=f
    print(tudo+4,'=',f)


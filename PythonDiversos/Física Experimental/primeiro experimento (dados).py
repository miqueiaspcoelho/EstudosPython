'''
L=[4,5,4,3,3,6,4,4,2,5,5,6,4,6,6,5,1,6,1,1,6,5,1,2,1,3,2,1,6,4,5,3,4,2,4,1,5,4,5,5,4,1,2,3,4,3,3,1,5,2,3,3,6,6,5,3,6,6,2,3,6,5,2,4,5,2,5,2,1,6,5,2,2,6,4,1,4,4,5,1,2,2,1,6,6,1,5,6,2,2,4,1,2,4,5,5,2,6,2,4,1,2,2,4,1,3,2,5,4,5,3,6,1,6,4,5,6,6,1,4,3,2,2,3,2,3,5,3,4,4,3,1,6,5,4,5,2,1,5,4,6,5,2,1,6,5,4,1,4,5,5,6,5,3,6,5,6,2,2,5,4,2,3,6,5,6,2,1,4,1,1,2,2,3,1,3,5,2,6,2,3,5,2,2,1,2,3,6,3,3,4,6,1,6,2,1,5,5,6,3,6,3,6,3,5,3,6,3,1,6,2,6,5,4,4,1,6,2,4,3,2,5,4,4,2,4,5,5,1,1,3,3,1,4,3,5,3,3,6,5,5,2,1,1,6,5,2,1,5,3,2,5,3,5,6,6,4,2,1,5,2,1,2,2,2,1,1,2,3,5]
R=L
T=[0,4,5,4,3,3,6,4,4,2,5,5,6,4,6,6,5,1,6,1,1,6,5,1,2,1,3,2,1,6,4,5,3,4,2,4,1,5,4,5,5,4,1,2,3,4,3,3,1,5,2,3,3,6,6,5,3,6,6,2,3,6,5,2,4,5,2,5,2,1,6,5,2,2,6,4,1,4,4,5,1,2,2,1,6,6,1,5,6,2,2,4,1,2,4,5,5,2,6,2,4,1,2,2,4,1,3,2,5,4,5,3,6,1,6,4,5,6,6,1,4,3,2,2,3,2,3,5,3,4,4,3,1,6,5,4,5,2,1,5,4,6,5,2,1,6,5,4,1,4,5,5,6,5,3,6,5,6,2,2,5,4,2,3,6,5,6,2,1,4,1,1,2,2,3,1,3,5,2,6,2,3,5,2,2,1,2,3,6,3,3,4,6,1,6,2,1,5,5,6,3,6,3,6,3,5,3,6,3,1,6,2,6,5,4,4,1,6,2,4,3,2,5,4,4,2,4,5,5,1,1,3,3,1,4,3,5,3,3,6,5,5,2,1,1,6,5,2,1,5,3,2,5,3,5,6,6,4,2,1,5,2,1,2,2,2,1,1,2,3,5]
A=len(T)
A=A-1
if A%2==0:
    a=A/2
    b=a+1
    a=int(a)
    b=int(b)
    c=T[a]
    d=T[b]
    mediana=(c+d)/2
print('Mediana ordenada por ordem de lançamento:',mediana)
T=sorted(T)
A=len(T)
A=A-1

if A%2==0:
    a=A/2
    b=a+1
    a=int(a)
    b=int(b)
    c=T[a]
    d=T[b]
    mediana=(c+d)/2
print('Mediana ordenda de forma crescente:',mediana)

D=len(L)
if D%2==0:
    w=(D-2)/2
    w=int(w)
    j=(w+1)
    j=int(j)
    f=L[w]
    g=L[j]
mediana=(f+g)/2
print('MEDIANA',mediana)


del Y[-1]
print('Y',Y)
T=T[1::]
print('T',T)
L=sorted(L)
for x in range(0,270):
    print(x,'=',L[x])
print(L[269])
A=len(L)
if A%2==0:
    a=A/2
    a=int(a)
    b=(A/2)+1
    b=int(b)
    c=L[a]
    print('c',c)
    d=L[b]
    print('d',d)
    mediana=(c+d)/2
print('mediana é:',int(mediana))
B=len(R)
if B%2==0:
    a=B/2
    a=int(a)
    b=(A/2)+1
    b=int(b)
    c=R[a]
    print('c',c)
    d=R[b]
    print('d',d)
    mediana1=(c+d)/2
print('mediana em ordem de lançamento é',mediana1)
for todos in range(0,270):
    print(todos,'=',R[todos])
soma=0
soma1=0
for todos in L:
    soma=soma+(todos)**2
    soma1=soma1+todos
media1=soma1/len(L)
print('Média',media1)
media=soma/len(L)
media=media**0.5
print(media)
L=sorted(L)
a=L.count(1)
b=L.count(2)
c=L.count(3)
d=L.count(4)
e=L.count(5)
f=L.count(6)
A=len(L)

print('Total de amostras: ',A,'\n1=',a,'2=',b,'3=',c,'4=',d,'5=',e,'6=',f)
print('Número de vezes que cada face aparece.')
'''


L=[4,5,4,3,3,6,4,4,2,5,5,6,4,6,6,5,1,6,1,1,6,5,1,2,1,3,2,1,6,4,5,3,4,2,
   4,1,5,4,5,5,4,1,2,3,4,3,3,1,5,2,3,3,6,6,5,3,6,6,2,3,6,5,2,4,5,2,5,2,
   1,6,5,2,2,6,4,1,4,4,5,1,2,2,1,6,6,1,5,6,2,2,4,1,2,4,5,5,2,6,2,4,1,2,
   2,4,1,3,2,5,4,5,3,6,1,6,4,5,6,6,1,4,3,2,2,3,2,3,5,3,4,4,3,1,6,5,4,5,
   2,1,5,4,6,5,2,1,6,5,4,1,4,5,5,6,5,3,6,5,6,2,2,5,4,2,3,6,5,6,2,1,4,1,
   1,2,2,3,1,3,5,2,6,2,3,5,2,2,1,2,3,6,3,3,4,6,1,6,2,1,5,5,6,3,6,3,6,3,
   5,3,6,3,1,6,2,6,5,4,4,1,6,2,4,3,2,5,4,4,2,4,5,5,1,1,3,3,1,4,3,5,3,3,
   6,5,5,2,1,1,6,5,2,1,5,3,2,5,3,5,6,6,4,2,1,5,2,1,2,2,2,1,1,2,3,5]
L=sorted(L)
a=L.count(1)
b=L.count(2)
c=L.count(3)
d=L.count(4)
e=L.count(5)
f=L.count(6)
A=len(L)

print('Total de amostras: ',A,'\n1=',a,'2=',b,'3=',c,'4=',d,'5=',e,'6=',f)
print('Número de vezes que cada face aparece.')






























'''#três listas para armazenar dados e quantas vezes cada dado se repete.
r=[]
l=[]
l1=[]
#somas iguais a zero para fazer o incremento delas com os dados passados.
s=0
s1=0
#contador que coordena o laço de repetição
n=1
#fim do intervalo que interrompe o laço (número de amostras)
am=int(input('Amostras: '))
#dicionários
dic={}
fre={}
#laço de repetição que pega o dado e faz as somas, para a média e média quadrática
#não sei se a média quadrática se faz necessária nesse caso.
while n <= am:
    num=int(input('Dado: '))
    num1=num
    num1=num1**2
    l.append(num)
    s=s+num
    s1=s1+num1
    n+=1
#Média, média quadrática e mediana
m=s/am
mq=(s1/am)**0.5
A=len(l)
d=int((A/2)-1)
e=int(d+1)
l=sorted(l)
direita=l[d]
esquerda=l[e]

mediana=(direita+esquerda)/2


#quantidade de vezes que cada face do dado se repetiu.
a=l.count(1)
b=l.count(2)
c=l.count(3)
d=l.count(4)
e=l.count(5)
f=l.count(6)


l1.append(a)
l1.append(b)
l1.append(c)
l1.append(d)
l1.append(e)
l1.append(f)
print('l1',l1)
#probabilidade de cada uma das faces aparecer em relação ao total de amostras.
u=[]
prob={}
for todos in l1:
    x=todos/am
    u.append(x)

for todos in range (0,6):
    y=l[todos]
    prob[y]=u[todos]


#fui usado no momento de descobrir a moda.
dic[a]=1
dic[b]=2
dic[c]=3
dic[d]=4
dic[e]=5
dic[f]=6

#frequência de cada número.
fre[1]=a
fre[2]=b
fre[3]=c
fre[4]=d
fre[5]=e
fre[6]=f

#aqui eu estava pensando um jeito de tirar o problema que encontrei na moda, mas ainda não consegui.
n=0
aqui=[]

while n < len(l1):
    x=l1[n]
    if x!=0:
        aqui.append(x)
    n+=1
print(aqui)

while 0 in l1:
    l1.remove(0)

#Na moda eu encontrei um problema, e se tivermos dados que se repetem de forma igual? como mostrar isso?
#Fica aí a questão.
M=max(l1)
moda=dic[M]

queda=int(input('Quantas vezes o dado caiu da mesa? '))
pqt=(queda*100)/am
print('Porcentagem de queda dos dados em relação à quantidade de vezes lançado.\n',round(pqt,5),'% das vezes.')
print('Média: ',m)
print('Média quadratica: ',mq)
print('Moda: ',moda)
print('Frequência: ',fre)
print('Mediana: ', mediana)
print('Probabilidade de cada uma das faces aparecer em relação às amostras\n:',prob)
'''

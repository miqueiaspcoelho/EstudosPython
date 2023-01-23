'''
dic={'Miq':(1,10,6.9)}
lista=[]
pontos=0
lugar=0
for tudo in range(0,3):
    lugar=lugar+1
    print(lugar)


    for tudo in dic:
        aqui=dic[tudo]
        lista.append(aqui)
        print(lista)

lista=lista[0]
print(lista)
lista=lista[lugar]
print(lista)



    
for tudo in range(0,3):
  
    
    print('aqui o valor da posição',lugar,'=',lista)
    if lista>=7:
        print('Maior que sete')
    else:
        print('Menor que sete')
    

dic={'M':(1,1,2,3,4,5,6,7,9,10,11,12,13,14,15,16),'B':(123123,123123,545)}
dic2={}
aprovados=[]
notas=[]
pontos=0

for tudo in dic:
    recebe=dic[tudo]
    notas.append(recebe)
for todas in notas:
    dic2[todas]=tudo
print(dic2)


for tudo in range(len(notas)):
    a=notas[tudo]
    print(a)
    for tudo in range(len(a)):
        b=a[tudo]
        if b >7:
            pontos=pontos+1
            print(b,pontos)
if pontos > 5:
    for tudo in dic:
        recebe2=dic[tudo
    dic[a]='aprovado'
print(dic)
    

dic={'M':(1,1,2,3,4,5,6,7,9,10,11,12,13,14,15,16),'B':(123123,123123,545)}
l=[]
li=[]
a=0
print(dic.items())
for tudo in dic:
    l.append(dic[tudo])
print(l)
for tudo in l[a]:
    li.append(tudo)
    a=a+1
print(li)

dic={'M':(10,11,12,13),'B':(3,4,12,13,14),'C':(5,6,15,16,17),'D':(7,8,18,19,20)}
tam=len(dic)
print(tam)
l=[]
s=[]

cont=0
aprovados=0
for isso in range(0,tam):
    for tudo in dic:
        recebe=dic[tudo]
        if recebe not in l:

            l.append(recebe)
    
print(l)
    
    for tudo in l[cont]:
        if tudo > 7 and tudo not in s:
            s.append(tudo)
                      
                         
    cont+=1
print(s)
'''
dic={'Alano':(7.5,8.0,6.5),'Denise':(9.0,8.5,9.5),'Ana Paula':(3.5,1.0,6.5)}
com=(7,7,7)
for todos in dic:    
    if (dic[todos][0]) > (com[0]) and (dic[todos][1]) > (com[1]) and (dic[todos][2]) > (com[2]):
        print(todos,',',dic[todos],'= aprovado(a)')
    else:
        print(todos,',',dic[todos],'= reprovado(a)')


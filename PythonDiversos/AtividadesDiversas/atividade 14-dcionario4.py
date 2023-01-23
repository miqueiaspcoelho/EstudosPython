
dic={'Alano':(7.5,8.0,6.5),'Denise':(9.0,8.5,9.5),'Ana':(3.5,1.0,6.5)}
posi=0
pontos=0
dic2={}
com=(7,7,7)
l=[]
dic3={}
for todos in dic:
    a=dic[todos]
    dic2[a]=todos
print(dic2)
tam=len(dic2)
for todos in dic2:
    l.append(todos)
print(l)
for tupla in l:
    a,b,c=tupla
    print(tupla[0])
    if a[0] > 7 or b>7 or c>7:
        dic3[l[0]]='aprovado'
print(dic3)


'''
if l[1]>=com:
    dic3[l[1]]='aprovado'
else:
    dic3[l[1]]='reprovado'
    print(dic3)


if l[0] com:
    print('Deu certo')





if c>=com:
    print('aprovado')
else:
    print('reprovado')

for todos in l:
    if todos>= l[0]:
        print('aprovado')
    else:
        print('reprovado')
    

for notas in range(0,tam):
    if dic2[0] >= com:
        print('aprovado')
    else:
        print('reprovado')

    for todos in a:
        if a[0]>=com[0]:
            pontos=pontos+1
            print(pontos)

        else:
            pontos=pontos-1
        posi+=1
    if pontos==3:
        print('aprovado')
    else:
        print('reprovado')

if pontos ==3:
    print('Estudante aprovado')
else:
    print('Estudante reprovado')


posi=0
pontos=0
for todos in range(0,b):
    
    if a[posi] >= 7:
        pontos=pontos+1
        posi+=1
    else:
        pontos=pontos-1
if pontos ==3:
    print('Estudante aprovado')
else:
    print('Estudante reprovado')
'''


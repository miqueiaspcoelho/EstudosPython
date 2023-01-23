'''
#1 jogando na lista os que se repetem.

#Maneira 1 de fazer.
lista=[]
lista1=[]

tam=int(input('Quantos elementos na lista?'))
for tudo in range(0,tam):
    numero=int(input('Digite um inteiro: '))
    lista.append(numero)
for numero in lista:
    cont=lista.count(numero)
    if cont>1 and numero not in lista1:
        lista1.append(numero)
print('os que se repetem:',lista1)

#Maneira 2 obs: utilizando a lista de entrada colocada pelo usuário
#na maneira 1.
quantidade=0
lista2=[]
i=0
for tudo in lista:
    b=lista[i]
    print('B=',b)

    for numeros in lista:
        print(b,'=',numeros)
        if b==numeros:
            quantidade+=1
        

    if quantidade>=2 and b not in lista2:
        lista2.append(b)

    quantidade=0
    i+=1
print('lista3, final',lista2)
'''
#-----------------------------------------------------------
'''
#2- Gerenciando frutas.
frutas=[]
precos=[]
dif=int(input('quantas frutas diferentes há?'))
for tudo in range(0,dif):
    fruta=str(input('Digite o nome da fruta: ')).lower()
    preco=float(input('Digite quanto a mesma custa: '))
    frutas.append(fruta)
    precos.append(preco)
print('frutas',frutas,'preços',precos)
dic={}
for tudo in range(0,dif):
    dic[frutas[tudo]]=precos[tudo]
while True:
    pesquisar=str(input('Digite o nome da fruta: ')).lower()
    if pesquisar in dic:
        recebe=dic[pesquisar]
        print(pesquisar,'custa',recebe,'R$')
    else:
        print('Fruta não catalogada')
    perg=str(input('Deseja pesquisar novamente?(s/n)')).upper()
    if perg=='S':
        continue
    if perg=='N':
        break
print('Dicionário',dic)
#------------------------------------------
#Maneira 2 de colocar os nomes e preços como chave e conteúdo
#em um dicionário.
dic2={}
for tudo in range(0,dif):
    fruta1=frutas[tudo]
    preco1=precos[tudo]
    dic2[fruta1]=preco1
print('dicionário 2',dic2)

#----------------------------------------------------------------------

#3- Criação de uma lista implícita.
lista=[((x*x)+2) for x in range(10)]
lista1=[]
i=0
for tudo in lista:
    recebe=lista[i]
    if i%2==0:
        lista1.append(recebe)
    i+=1
print('Lista inicial construída:',lista,'\nLista apenas com as posições pares:',lista1)

#Maneira de fazer sem utilizar lista implícita.
lista=[]
lista2=[]
for tudo in range(10):
    numero=(tudo*tudo)+2
    lista.append(numero)
    if tudo%2==0:
        lista2.append(numero)
print('Lista geral:',lista,'\nLista somente com posições as pares:',lista2)

#4-Usar dicionário para saber se os alunos passaram ou não.
print('Vamos criar o dicionário com as informações.')
tam=int(input('Quantos são os dados: '))
dic={}
for tudo in range(0,tam):
    nome=str(input('Digite o nome do aluno: ')).capitalize()
    print('Vamos inserir as 3 notas.')
    Notas=[]
    for tudo in range(0,3):
        nota=float(input('Digite a nota: '))
        Notas.append(nota)
    geral=tuple(Notas)
    dic[nome]=geral
print(dic)

dicaprovados={}
dicreprovados={}
dicrecuperacao={}
for tudo in dic:
    soma=0
    pontos=dic[tudo]
    for numeros in range(0,3):
        numero=pontos[numeros]
        soma=soma+numero
    if soma >15 and soma<21:
        dicrecuperacao[tudo]=soma
    if soma<=15:
        dicreprovados[tudo]=soma
    if soma>=21:
        dicaprovados[tudo]=soma
print('Aprovados:',dicaprovados,'\nReprovados:',dicreprovados,'\nRecuperação:',dicrecuperacao)
#----------------------------------------------------------------

#Outra maneira de fazer.
dic={}
dic2={}
dic3={}
dic4={}
lista=[]
print('Vamos construir o dicionário.')
tam=int(input('Quantos são os alunos?'))
for tudo in range(0,tam):
    nome=str(input('Nome: ')).capitalize()
    soma=0
    for tudo in range(0,3):
        nota=float(input('Nota: '))
        lista.append(nota)
        soma=soma+nota
    notas=tuple(lista)
    lista=[]
    dic[nome]=notas
    if soma>15 and soma<21:
        dic2[nome]=soma
    if soma<=15:
        dic3[nome]=soma
    if soma>=21:
        dic4[nome]=soma
print('Todos: ',dic)
print('Aprovados: ',dic4)
print('Reprovados: ',dic3)
print('Recuperação: ',dic2)
'''

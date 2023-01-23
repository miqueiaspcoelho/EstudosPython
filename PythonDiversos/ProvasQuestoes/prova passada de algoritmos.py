#1-
'''
lista=[]
lista2=[]
tam=int(input('Quantos números tem a lista? '))
for todos in range(0,tam):
    numero=int(input('Digite um número: '))
    lista.append(numero)
for todos in lista:
    cont=lista.count(todos)
    if cont==1:
        lista2.append(todos)
print('Lista inicial: ',lista)
print('Lista sem as repetições: ',lista2)

#---------------------------------------------
#2-
palavra0=str(input('Digite algo: ')).lower()
palavra1=str(input('Digite algo: ')).lower()
palavra=''
cont0=len(palavra0)
cont1=len(palavra1)
if cont0>=cont1:
    cont=palavra0
    cont1=palavra1
else:
    cont=palavra1
    cont1=palavra0
for todos in cont:
    if todos in cont1 and todos not in palavra:
        palavra=palavra+todos
if palavra=='':
    print('Não há interseção')
            
print('A interseção entre as palavras é: ', palavra)
'''
#--------------------------------------------
#3-
#Defini 10 variáveis e mais uma de entrada para o usuário.
dic={}
dic2={}
dic3={}
dic4={}

notas=()

lista=[]
lista2=[]
lista3=[]

soma=0
media=0

quant=int(input('Quantos são os competidores? '))

#Criei um laço para o usuário decidir quantos nomes irá colocar.
#Dentro deste mesmo laço é calculada a media, que é jogada em outro dicionário relativo ao nome digitado.
#Após cada ciclo de 3 notas digitas a média zera e a lista usada para criar a tupla de notas para cada nome também.
#No dicionário principal(dic) é colocado o nome e a tupla correspondente.


for todos in range(0,quant):
    nome=str(input('Nome: ')).capitalize()
    for todos in range(0,3):
        nota=float(input('Nota: '))
        lista.append(nota)
        media=media+nota
    media=media/3
    media=round(media,3)
    dic2[nome]=media
    print(media,'media')
    media=0
    notas=tuple(lista)
    dic[nome]=notas
    lista=[]
print(dic2)

#Após ver as médias, verifico se elas não são todas iguais, pois se forem ocorreu um empate.
#Para isso usei dois laços e uma condição. Dentro da condição foi apenas matemática para saber se todos são iguais.
#Pra ver se são iguais foi preciso primeiro alinhar de forma crescente os itens.
#Se der empate o programa para a execução e encerra.

for todos in dic2:
    recebe3=dic2[todos]
    lista3.append(recebe3)

for todos in lista3:
    soma=soma+todos
    lista3=sorted(lista3)
tamanho=len(lista3)
if soma/tamanho==lista3[0]:
    print('Deu empate todos venceram.')
    exit()

#Aqui começa a primeira parte para checar quem teve a maior nota.
#Peguei a média usando cada nome como chave e joguei em uma lista, depois peguei a maior média.
for todos in dic2:
    recebe=dic2[todos]
    lista2.append(recebe)
    aprovado=max(lista2)

#No dicionário 3 eu fiz a inversão, tudo que era chave agora é conteúdo, daí fica mais fácil de procurar quem foi aprovado
#de acordo com a média que foi onde usei a função max anteriormente.
for todos in dic2:
    recebe1=dic2[todos]
    dic3[recebe1]=todos

#Aqui faço a pesquisando usando a variável aprovado que de mais acima. Eu usei ela como chave, e isso foi possivel depois da inversão.
for todos in dic3:
    recebe2=dic3[aprovado]

#Aqui mostro os resultados.
print(recebe2,'calssificado(a), com a nota: ',aprovado)
print('dicionario que mudou: ',dic3)
print('Lista 2: ',lista2)
print('Dicionário incial: ',dic)
print('Dicionário 2: ',dic2)

#Aqui eu excluo quem foi o classificado do dicionário 3.
#e ao adicionar os demais no dicionário 4 eu já faço a inversão, e os nomes voltam a ser cahve e as notas conteúdo.
del dic3[aprovado]
for todos in dic3:
    recebe4=dic3[todos]
    dic4[recebe4]=todos

#Aqui apenas mostro os desclassificados, exibindo o dicionário 4, que é semelhante ao 3, porém sem o vencedor.
print('Desclassificados:\n',dic4)


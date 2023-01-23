lista=[]
nome=''
while nome!='false':
    nome=str(input('Nome: '))
    if nome!='false':
        lista.append(nome.title())
lista=sorted(lista)
for elem in lista:
    print(elem)

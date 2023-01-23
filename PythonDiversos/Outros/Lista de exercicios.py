#1-

print('Questão 1\n')
lista=[76,92.3,'oi','True',4,76]
print('a)inserir "laranja" e 76 no final da lista.')
#a)inserir "laranja" e 76 no final da lista.
lista.append('laranja')

lista.append(76)
print(lista,'\n')
print('b)inserir "gato" na posição de índice 3.')
#b)inserir "gato" na posição de índice 3.
lista[3]='gato'
print(lista,'\n')
print('c) inserir 99 no início da lista.')
#c) inserir 99 no início da lista.
lista2=[99]
lista= lista2 + lista
print(lista,'\n')
print('d) Encontrar o índice de "oi"')
#d) Encontrar o índice de "oi"
for todos in lista:
    if todos == 'oi':
        print(lista.index(todos),'\n')

print('e) Contar o número de ocorrências de 76 na lista.')
#e) Contar o número de ocorrências de 76 na lista.
vezes=lista.count(76)
print(vezes,'\n')
print('f) Remover a primeira ocorrência de 76 na lista.')
#f) Remover a primeira ocorrência de 76 na lista.
lista2=[]
for todos in lista:
    if todos==76:
        
        lista2.append(76)
        if 76 in lista2:
            lista.remove(76)
            break
print(lista,'\n')




#2-
print('Questão 2')
def calcula_maximo_2(lista=[]):
    quantidade=int(input('Quantos números tem a lista? '))
    for tudo in range(0,quantidade):
        numero=int(input('Digite um número: '))
        lista.append(numero)
    print(lista)
    maxi= max(lista)
    mini= min(lista)
    calcula_maximo_2=maxi+mini
    print('Resposta, soma do máximo e mínimo da lista',mini,'+',maxi,'=',calcula_maximo_2)
lista=[]
calcula_maximo_2(lista)




#3-
print('Questão 3')
def soma_quadrados(lista=[]):
    quantidade=int(input('Quantos números tem a lista? '))
    for tudo in range(0,quantidade):
        numero=int(input('Digite um número: '))
        lista.append(numero)
    
    print(lista)
    lista2=[]
    for todos in lista:
        quadrado=todos**2
        lista2.append(quadrado)
    atual=0
    depois=0
    for todos in lista2:
       atual=todos
       depois=depois+atual
       atual=0
    print('Resposta =',depois)
lista=[]
soma_quadrados(lista)




#4-
print('Questão 4')
def soma_impares(lista=[]):
    quantidade=int(input('Quantos números tem a lista? '))
    for tudo in range(0,quantidade):
        numero=int(input('Digite um número: '))
        lista.append(numero)
    
    lista2=[]
    for todos in lista:
        if todos%2!=0:
            lista2.append(todos)
    atual=0
    depois=0
    for todos in lista2:
        atual=todos
        depois=depois+atual
        
    print('A soma de todos os números ímpares da lista é: ',depois)
lista=[]
soma_impares(lista)




#5-
print('Questão 5')
def quantidade_negativos(lista=[]):
    quantidade=int(input('Quantos números tem a lista? '))
    for tudo in range(0,quantidade):
        numero=int(input('Digite um número: '))
        lista.append(numero)
    cont=0
    for todos in lista:
        if todos < 0:
            cont+=1
    print('A quantidade de números negativos na lista é: ',cont)
lista=[]
quantidade_negativos(lista)




#6-
print('Questão 6')
def quantidade_palavras_5(lista=[]):
    quantidade=int(input('Quantas palavras tem a lista? '))
    for tudo in range(0,quantidade):
        palavra=str(input('Digite uma palavra: '))
        lista.append(palavra)
    posicao=0
    quantidade=0
    for todos in lista:
        a=len(lista[posicao])
        posicao+=1
        if a==5:
            quantidade+=1
    print('O número de palavras com cinco letras é: ',quantidade)
lista=[]
quantidade_palavras_5(lista)



#7-
print('Questão 7')
def soma_par(lista=[]):
    quantidade=int(input('Quantos números tem a lista? '))
    for tudo in range(0,quantidade):
        numero=int(input('Digite um número: '))
        lista.append(numero)
    soma=0
    for todos in lista:
        if todos%2==0:
            lista.remove(todos)
            break
    for todos in lista:
        if todos%2==0:
            print('soma: ',soma, '+' ,todos)
            soma=soma+todos
    print('A soma dos números pares exceto o primeiro é: ', soma)
lista=[]
soma_par(lista)




#8-
print('Questão 8')
def quantidade_palavras_fim(lista=[]):
    quantidade=int(input('Quantas palavras tem a lista? '))
    for tudo in range(0,quantidade):
        palavra=str(input('Digite uma palavra: '))
        lista.append(palavra)
    quantidade=0
    for todos in lista:
        if 'fim' in lista:
            for todos in lista:  
                if todos != 'fim':
                    quantidade+=1
                else:
                    if todos=='fim':
                        quantidade+=1
                        break
    print('Quatidade de palavras na lista:',lista,
          'antes da primeira palavra FIM  + a mesma =',quantidade)
   
   
lista=[]
quantidade_palavras_fim(lista)




#9-
print('Questão 9')
def palavras_inicio_fim_iguais(lista=[]):
    quantidade=int(input('Quantas palavras tem a lista? '))
    for tudo in range(0,quantidade):
        palavra=str(input('Digite uma palavra: '))
        lista.append(palavra)
    lista2=[]
    quantidade=0
    for todos in lista:
        letras1=len(todos)
        if letras1 >=2:
            lista2.append(todos)
    print(lista2)
    for todos in lista2:
        primeira=todos[0]
        ultima=todos[-1]
        if primeira==ultima:
            quantidade+=1
    print('Quantidade de palavras com',
          'duas ou mais letras e com',
    'a primeira e a última letras iguais: ',quantidade,lista2)
lista=[]
palavras_inicio_fim_iguais(lista)



#10-
print('Questão 10')

texto1= 'velho novo velho velho velho novo'
texto2=''
if ',' in texto1:
    separa=texto1.split(',')
if ' ' in texto1:
    separa=texto1.split()
for todos in separa:
    if todos=='velho':
        texto2=texto2 + 'novo'+ ' '
    if todos=='novo':
        texto2=texto2+ 'velho'+' ' 
print(texto1)
print(texto2)



#11-
print('Questão 11')
numero=int(input('Digite um número: ' ))
print('Quantidade de digitos presentes no número: ',len(str(numero)))

    

#12-
print('Questão 12')
def palindroma(t):
    texto=str(input('Digite um texto, vamos ver se ele é igual lido normal e de trás pra frente: '))
    texto1=texto.lower()
    texto1=texto1.split()
    texto2=''
    texto2=texto2.join(texto1)
    texto3=texto2
    for tudo in texto3:
        texto3=texto3[::-1]
    texto4=texto[::-1]
    if texto3==texto2:
        print(texto,' ',texto4)
        print('Palindromo, TRUE')
palvra=''
palindroma(a)


#13-
print('Questão 13, verificação de comandos.\n')
print('Respostas: ','Python'[1]
      ,'Strings são sequências de caracteres'[5]
      ,len('maravilhoso')
      ,'Mistério'[:4]
      ,'p' in 'Pineapple'
      ,'pear' not in 'Pineapple'
      ,'apple' in 'Pineapple'
      ,'apple' > 'pineapple'
      ,'pineapple' < 'Peach')
#resultados :y g 11 Mist True True True False False
'''


#essa questão não funcionou, dava erro, fui tentar resolver e ainda não consegui.
#15-
print('Questão 15, o jogo da velha.')
a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9

print(a,'|',b,'|',c)
print('------------')
print(d,'|',e,'|',f)
print('------------')
print(g,'|',h,'|',i)


muda=1
velha=[]

lista=[1,2,3,4,5,6,7,8,9]


jogadas1=[]
jogadas2=[]

linha1=[1,2,3]
linha2=[1,4,7]
linha3=[1,5,9]
linha4=[4,5,6]
linha5=[7,8,9]
linha6=[2,5,8]
linha7=[3,6,9]
linha8=[3,5,7]



tam=len(lista)


for todos in range(len(lista)):
    if lista==velha:
        print('Deu velha, SOL LÁ MENTOS!!!kkkkk')
        break
    
    if muda==1 and tam>0:
        jogador1=int(input('JOGADOR 1 (O): '))
        if jogador1 in lista:
            if jogador1==1:
                a='O'
            if jogador1==2:
                b='O'
            if jogador1==3:
                c='O'
            if jogador1==4:
                d='O'
            if jogador1==5:
                e='O'
            if jogador1==6:
                f='O'
            if jogador1==7:
                g='O'
            if jogador1==8:
                h='O'
            if jogador1==9:
                i='O'
        if jogador1 not in lista:
            print('\nPosição ocupada(ou não existe), tente novamente.\n')
            continue
        
        jogadas1.append(jogador1)
        jogadas1=sorted(jogadas1)
        print(a,'|',b,'|',c)
        print('------------')
        print(d,'|',e,'|',f)
        print('------------')
        print(g,'|',h,'|',i,'\n')

        if 1 in jogadas1:
            if jogadas1[0]==linha1[0] and jogadas1[1]==linha1[1] and jogadas1[2]==linha1[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha2[0] and jogadas1==linha2[1] and jogadas1[2]==linha2[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha3[0] and jogadas1[1]==linha3[1] and jogadas1[2]==linha3[2]:
                print('Jogador 1(O) venceu!!!.')
                break

        if 3 in jogadas1:
            if jogadas1[0]==linha1[0] and jogadas1[1]==linha1[1] and jogadas1[2]==linha1[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha7[0] and jogadas1[1]==linha7[1] and jogadas1[2]==linha7[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha8[0] and jogadas1[1]==linha8[1] and jogadas1[2]==linha8[2]:
                print('Jogador 1(O) venceu!!!.')
                break

        if 2 in jogadas1:
            if jogadas1[0]==linha1[0] and jogadas1[1]==linha1[1] and jogadas1[2]==linha1[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha6[0] and jogadas1[1]==linha6[1] and jogadas1[2]==linha6[2]:
                print('Jogador 1(O) venceu!!!.')
                break

        if 4 in jogadas1:
            if jogadas1[0]==linha2[0] and jogadas1[1]==linha2[1] and jogadas1[2]==linha2[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha4[0] and jogadas1[1]==linha4[1] and jogadas1==linha4[2]:
                print('Jogador 1(O) venceu!!!.')
                break

        if 5 in jogadas1:
            if jogadas1[0]==linha3[0] and jogadas1[1]==linha3[1] and jogadas1[2]==linha3[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha4[0] and jogadas1[1]==linha4[1] and jogadas1[2]==linha4[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha6[0] and jogadas1[1]==linha6[1] and jogadas1[2]==linha6[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha8[0] and jogadas1[1]==linha8[1] and jogadas1[2]==linha8[2]:
                print('Jogador 1(O) venceu!!!.')
                break

        if 6 in jogadas1:
            if jogadas1[0]==linha4[0] and jogadas1[1]==linha4[1] and jogadas1[2]==linha4[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha7[0] and jogadas1[1]==linha7[1] and jogadas1[2]==linha7[2]:
                print('Jogador 1(O) venceu!!!.')
                break

        if 7 in jogadas1:
            if jogadas1[0]==linha2[0] and jogadas1[1]==linha2[1] and jogadas1[2]==linha2[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha5[0] and jogadas1[1]==linha5[1] and jogadas1[2]==linha5[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha8[0] and jogadas1[1]==linha8[1] and jogadas1[2]==linha8[2]:
                print('Jogador 1(O) venceu!!!.')
                break

        if 8 in jogadas1:
            if jogadas1[0]==linha5[0] and jogadas1[1]==linha5[1] and jogadas1[2]==linha5[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha6[0] and jogadas1[1]==linha6[1] and jogadas1[2]==linha6[2]:
                print('Jogador 1(O) venceu!!!.')
                break

        if 9 in jogadas1:
            if jogadas1[0]==linha3[0] and jogadas1[1]==linha3[1] and jogadas1[2]==linha3[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha5[0] and jogadas1[1]==linha5[1] and jogadas1[2]==linha5[2]:
                print('Jogador 1(O) venceu!!!.')
                break
            if jogadas1[0]==linha7[0] and jogadas1[1]==linha7[1] and jogadas1[2]==linha7[2]:
                print('Jogador 1(O) venceu!!!.')
                break
        

        
        
        
        
        
        
        lista.remove(jogador1)
        
        tam=len(lista)
        
        muda-=1
            
    if muda==0 and tam>0:
        jogador2=int(input('JOGADOR 2 (X): '))
        if jogador2 in lista:
            if jogador2==1:
                a='X'
            if jogador2==2:
                b='X'
            if jogador2==3:
                c='X'
            if jogador2==4:
                d='X'
            if jogador2==5:
                e='X'
            if jogador2==6:
                f='X'
            if jogador2==7:
                g='X'
            if jogador2==8:
                h='X'
            if jogador2==9:
                i='X'

        if jogador2 not in lista:
            print('\nPosição ocupada(ou não existe), tente novamente.\n')
            continue
        jogadas2.append(jogador2)
        jogadas2=sorted(jogadas2)
        print(a,'|',b,'|',c)
        print('------------')
        print(d,'|',e,'|',f)
        print('------------')
        print(g,'|',h,'|',i,'\n')


        if 1 in jogadas2:
            if jogadas2[0]==linha1[0] and jogadas2[1]==linha1[1] and jogadas2[2]==linha1[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha2[0] and jogadas2==linha2[1] and jogadas2[2]==linha2[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha3[0] and jogadas2[1]==linha3[1] and jogadas2[2]==linha3[2]:
                print('Jogador 2(X) venceu!!!.')
                break

        if 3 in jogadas2:
            if jogadas2[0]==linha1[0] and jogadas2[1]==linha1[1] and jogadas2[2]==linha1[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha7[0] and jogadas2[1]==linha7[1] and jogadas2[2]==linha7[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha8[0] and jogadas2[1]==linha8[1] and jogadas2[2]==linha8[2]:
                print('Jogador 2(X) venceu!!!.')
                break

        if 2 in jogadas2:
            if jogadas2[0]==linha1[0] and jogadas2[1]==linha1[1] and jogadas2[2]==linha1[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha6[0] and jogadas2[1]==linha6[1] and jogadas2[2]==linha6[2]:
                print('Jogador 2(X) venceu!!!.')
                break

        if 4 in jogadas2:
            if jogadas2[0]==linha2[0] and jogadas2[1]==linha2[1] and jogadas2[2]==linha2[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha4[0] and jogadas2[1]==linha4[1] and jogadas2==linha4[2]:
                print('Jogador 2(X) venceu!!!.')
                break

        if 5 in jogadas2:
            if jogadas2[0]==linha3[0] and jogadas2[1]==linha3[1] and jogadas2[2]==linha3[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha4[0] and jogadas2[1]==linha4[1] and jogadas2[2]==linha4[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha6[0] and jogadas2[1]==linha6[1] and jogadas2[2]==linha6[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha8[0] and jogadas2[1]==linha8[1] and jogadas2[2]==linha8[2]:
                print('Jogador 2(X) venceu!!!.')
                break

        if 6 in jogadas2:
            if jogadas2[0]==linha4[0] and jogadas2[1]==linha4[1] and jogadas2[2]==linha4[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha7[0] and jogadas2[1]==linha7[1] and jogadas2[2]==linha7[2]:
                print('Jogador 2(X) venceu!!!.')
                break

        if 7 in jogadas2:
            if jogadas2[0]==linha2[0] and jogadas2[1]==linha2[1] and jogadas2[2]==linha2[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha5[0] and jogadas2[1]==linha5[1] and jogadas2[2]==linha5[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha8[0] and jogadas2[1]==linha8[1] and jogadas2[2]==linha8[2]:
                print('Jogador 2(X) venceu!!!.')
                break

        if 8 in jogadas2:
            if jogadas2[0]==linha5[0] and jogadas2[1]==linha5[1] and jogadas2[2]==linha5[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha6[0] and jogadas2[1]==linha6[1] and jogadas2[2]==linha6[2]:
                print('Jogador 2(X) venceu!!!.')
                break

        if 9 in jogadas2:
            if jogadas2[0]==linha3[0] and jogadas2[1]==linha3[1] and jogadas2[2]==linha3[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha5[0] and jogadas2[1]==linha5[1] and jogadas2[2]==linha5[2]:
                print('Jogador 2(X) venceu!!!.')
                break
            if jogadas2[0]==linha7[0] and jogadas2[1]==linha7[1] and jogadas2[2]==linha7[2]:
                print('Jogador 2(X) venceu!!!.')
                break
    
        
        
        
        lista.remove(jogador2)
        
        tam=len(lista)
        
        muda+=1
    
    
print('Acabou o jogo')
'''

print('QUESTÃO 7\n')
l=[-9,0.5,1,1,4,2,3,5,76,67,98,2000]
a=0
b=1
for x in l:
    #pega o maior, comparamos cada numero da lista com
    #uma variável 'a' que começa em zero.
    #sempre que o valor da lista é maior que 'a',
    #'a' recebe o valor da lista, aí o 'x' recebe o próximo valor
    #e compara com o anterior, se for maior o 'a' recebe o valor da lista,
    #se for menor ele ignora e pula para o próximo número da lista.
    if x>a:
        a=x
    #pega o menor, comparamos cada número da lista com
    #uma variável 'b' que começa em 1. Se o número for menor que 'b',
    #'b' recebe o valor do número da lista, caso contrário ele ignora e pula
    #para o próximo, assim ele compara todos os elementos e pega o menor deles.
    if x<b:
        b=x
#aqui nós temos a função pré-pronta do python que pega o maior e o menor
#números de uma lista.
print('Máximo e mínimo pela função pronta do python=',max(l),',',min(l))
#aqui temos a nossa função, percebemos que temos o mesmo resultado,
#logo a lógica da nossa função está certa.
print('Máximo e mínimo pela nossa função=',a,',',b,'\n')


# para determinar o soma dos elementos da lista
#construímos uma função que pega cada elemento e fazemos um incremento
#de variável.

#verificamos o tamanho da lista
n=len(l)

#variável soma (variável para ir sempre recebendo os valores da lista e os ir somando)
soma=0

#laço 'for' que vai da posição '0' até a posição 'n-1'(tamanho da lista)
for x in range(0,n):
    #soma recebe sempre a si mesma + o valor de cada elemento da lista na posição da faixa 'range'.
    soma=soma + l[x]


#notamos que os valores são iguais, logo a nossa lógica está correta.    
print('Soma pelo nosso programa=',soma)
print('Soma pela função pronta do python=',sum(l),'\n')


#questão 8 imprimir um número colocado pelo usuário,
#porém de vemos imprimir ao contrário.
print('QUESTÃO 8\n')

#primeiro pedimos para o usuário digitar o número.
num=int(input('digite um número inteiro positivo: '))

#em seguida transformamos esse número inteiro em uma string (variável do tipo texto)
num=str(num)
#contamos quantos caracteres há nesse número que agora é uma string
tam=len(num)
#esse 'x' é a grande sacada para percorrer a string de forma invertida.
#'x' é o número total de caracteres - 1, pois vamos precisar colocá-lo
#dentro de um parâmetro que definirá a posição.
x=tam-1

#criamos uma lista vazia que vai receber os caracteres em ordem invertida.
e=[]
#a variável 't' recebe um espaço, pois ela será incrementada.
t=''

#aqui temos um laço que percorre de forma invertida a nossa string.
for tudo in range(0,tam):
    #'z' recebe os caracteres da variável que o usuário digitou
    #mas a grande sacada é que a posição que ela recebe é:
    #x- tudo==== para o número 152732439979, teremos: [11 - 0]= posição 11 / [11 - 1]= posição 10 / [11 - 2]= posição 9 / ...
    #estamos pegando os caracteres de trás para frente.
    z=num[x-tudo]
    #jogamos eles em uma lista.
    e.append(z)

#para todos os elementos na lista, vamos concatenar (juntar todos os caracteres) em uma variável.
#Aqui entra a variável 't' que recebeu um espaço vazio inicialmente.
for tudo in e:
    #concatenação.
    t=t+tudo
print('Imprimindo ao contrário pelo nosso programa=', t)
#aqui temos a função pré-pronta do Python, notamos que dá o mesmo resultado da nossa função,
#logo, a nossa lógica esta certa.
print('Imprimindo ao contrário pela função pré-pronta do Python=',num[::-1])

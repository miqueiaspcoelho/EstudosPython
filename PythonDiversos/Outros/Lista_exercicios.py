#11º
'''
def numero_digitos(numero):
    global y
    x = str(numero)
    y = len(x)
    return y
print(numero_digitos(input("Digite um numero inteiro: ")))
'''
#7º
'''
def soma_par(*lista):
    global x
    global y
    x = [*lista]
    y = []
    qtd = 0
    cont = 0
    for n in range(len(x)):
        if x[qtd]%2==0:
            y.append(x[qtd])
            cont = cont + x[qtd]
            qtd += 1
        else:
            qtd += 1
    return cont - y[0]
print("""Para chamar a função digite \" soma_par() \". E dentro
dos parenteses digite os numeros inteiros que deseja somar,
separados por vigula. EX: soma_par(2,4,3,1,6)""")
'''
#4º
'''
def soma_impares(*lista):
    global x
    global y
    x = [*lista]
    y = []
    qtd = 0
    cont = 0
    for n in range(len(x)):
        if x[qtd]%2==1:
            y.append(x[qtd])
            cont = cont + x[qtd]
            qtd += 1
        else:
            qtd += 1
    return cont
print("""Para chamar a função digite \" soma_impares() \". E dentro
dos parenteses digite os numeros inteiros que deseja somar,
separados por vigula. EX: soma_impares(2,4,3,1,6)""")
'''
#5º
'''
def quantidade_negativos(*lista):
    global x
    global y
    x = [*lista]
    y = []
    qtd = 0
    cont = 0
    for n in range(len(x)):
        if x[qtd]<0:
            cont += 1
            qtd +=1
        else:
            qtd += 1
    return cont
print("""Para chamar a função digite \" quantidade_negativos() \". E dentro
dos parenteses digite os numeros inteiros que deseja contar a quantidade
dos mesmos, separados por vigula. EX: quantidade_negativos(2,-4,3,-1,6)""")
'''
#3º
'''
def soma_quadrados(*lista):
    global x
    global y
    x = [*lista]
    y = []
    qtd = 0
    cont = 0
    for n in range(len(x)):
        cont = cont + x[qtd]**2
        qtd += 1
    return cont
print("""Para chamar a função digite \" soma_quadrados() \". E dentro
dos parenteses digite os numeros inteiros que deseja somar os quadrados
dos mesmos, separados por vigula. EX: soma_quadrados(2,-4,3,-1,6)""")
'''







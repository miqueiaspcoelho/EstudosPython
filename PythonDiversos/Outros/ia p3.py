import numpy as np
import random
import math
from copy import deepcopy


def Decimal(x):#pegamos uma  string de  binário e transformamos em decimal float
    if '.' not in x:
        soma=0
        inverte=x[::-1]
        for posicao in range(0,len(inverte)):
            soma=soma + ((2**(posicao))*float(inverte[posicao]))
        return soma
    else:
        for numero in range(0,len(x)):
            if x[numero]=='.':
                a=numero
        esquerda=x[0:(a)]
        
        
        direita=x[(a+1):]
        
        
        somaE=0
        somaD=0
        inverteE=esquerda[::-1]
        for posicaoE in range(0,len(inverteE)):
            somaE=somaE + ((2**(posicaoE))*(float(inverteE[posicaoE])))
            
        for posicaoD in range(0,len(direita)):
            somaD=somaD + ((2**(-(posicaoD+1)))*(float(direita[posicaoD])))
        return somaE+somaD


def Binario(x,tamD,tamE):# transforma decimal em binario, nós definimos o tamanho da parte inteira (tamD) e da parte fracionária (tamE)
    b=str(x)
    if '.' in b:
        for item in range(0,len(b)):
            if b[item]=='.':
                corte=item
        esquerda=int(b[0:corte])
        direita=str(b[(corte):])
        guarda=''
        fracao=direita
        for y in range(0,tamE):
            fracao=str(fracao)
            tam=len(fracao)
            k=float(fracao)
            m=k*2
            if m==1:
                guarda=guarda+'1'+(tamE-y)*'0'
                break
            if m>1:
                fracao=abs(1-m)
                guarda=guarda+'1'
            if m<1:
                fracao=m
                guarda=guarda+'0'
                
        return np.binary_repr(esquerda,width=tamD)+'.'+guarda
    else:
        return np.binary_repr(x,width=tamD)+'.'+tamE*'0'

def function1(x,y):
    f=-20*math.exp(-0.2*((x**(2)+y**(2))/2)**(0.5))-1*math.exp((math.cos(2*math.pi*x)+math.cos(2*math.pi*y))/2)+20+math.exp(1)#função do problema
    return f

def Fitfunction1(x):
    f=1/(1+x) #função fitness, devemos maximiza-la
    return f


def geraCasais(Populacao,fitness,tam): #paramentros: Uma geração, o fitness de cada um e tamanho da população
    k=0.75
    i=0
    p=0
    q=0
    casais=[]
    while i!=tam: #metodo de seleção por meio de sorteio
    #aqui geramos o pai
        while p!=1:
            numero1=random.randrange(0,tam)
            numero2=random.randrange(0,tam)
            if (numero1)!=(numero2):
                p=1
        r=round((random.random()),2)
        #print('PAi r=',r,'n1=',numero1,'n2=',numero2)
        if r < k:
            
            compara1=fitness[numero1]
            compara2=fitness[numero2]
            #print(compara1,compara2)
            if compara1>=compara2:
                sortudo=Populacao[numero1]
                
            else:
                sortudo=Populacao[numero2]
                
        else:
            
            compara1=fitness[numero1]
            compara2=fitness[numero2]
            #print(',',compara1,compara2)
            if compara1<=compara2:
                sortudo=Populacao[numero1]
                
            else:
                sortudo=Populacao[numero2]
    #aqui geramos a mãe
        while q!=1:
            numero3=random.randrange(0,tam)
            numero4=random.randrange(0,tam)
            if (numero3)!=(numero4):
                q=1
        r=round((random.random()),2)
        #print(' MAE r=',r,'n3=',numero3,'n4=',numero4)

        if r < k:
    
            compara3=fitness[numero3]
            compara4=fitness[numero4]
            #print(compara3,compara4)
            
            if compara3>=compara4:
                sortudo1=Populacao[numero3]
                
            else:
                sortudo1=Populacao[numero4]
        else:
            
            compara3=fitness[numero3]
            compara4=fitness[numero4]
            #print(',',compara3,compara4)
            if compara3<=compara4:
                sortudo1=Populacao[numero3]

            else:
                sortudo1=Populacao[numero4]
                
        casais.append((sortudo,sortudo1))
        
        i+=1
        p=0
        q=0
    return casais


def geraFilhos(ListaCasais,TC,tam): #Crossover, parametros: Lista de casais, taxa de cruzamento e tamanho do cromossomo
    gerados=[]
    for x in range(0,len(ListaCasais)):
        r = round((random.random()),2)
        if r < TC:
            #print('r=',r)
            casal=ListaCasais[x]
            Pai = casal[0]
            Mae=casal[1]
            GenePaiC1 = Pai[0]
            GeneMaeC1 = Mae[0]
            GenePaiC2 = Pai[1]
            GeneMaeC2 = Mae[1]
            corte= random.randrange(1,(tam-1))
            fC1 = GenePaiC1[0:corte] + GeneMaeC1[corte:]
            fC2 = GenePaiC2[0:corte] + GeneMaeC2[corte:]
            filho = (fC1,fC2)
            gerados.append(filho)
            
        else:
            casal=ListaCasais[x]
            d=(random.randrange(0,1))
            filho = casal[d]
            gerados.append(filho)
    return gerados


def Mutacao(geracao,TM):#gera ou não mutaçoes, parametros: uma geração e a taxa de mutação
    Q=[]
    for m in range(0,len(geracao)):
        a=''
        b=''
        L1=[]
        LC1=[]
        
        L2=[]
        LC2=[]
        
        FILHO=geracao[m]
        
        C1=FILHO[0]
        C2=FILHO[1]
        for tam in range(0,len(C1)):
            L1.append(C1[tam])
        for elemento in L1:
            r = random.random()
            if r < TM:
                if elemento=='0':
                    LC1.append('1')
                if elemento=='1':
                    LC1.append('0')
                if elemento=='.':
                    LC1.append(elemento)
            else:
                LC1.append(elemento)
        for dado in LC1:
            a=a+dado

        for tam in range(0,len(C2)):
            L2.append(C2[tam])
        for elemento in L2:
            r = random.random()
            if r < TM:
                if elemento=='0':
                    LC2.append('1')
                if elemento=='1':
                    LC2.append('0')
                if elemento=='.':
                    LC2.append(elemento)
            else:
                LC2.append(elemento)
        for dado in LC2:
            b=b+dado
        Q.append((a,b))

    return Q


def geradorAleatorio(Inferior,Superior,populacao,passo):#gerador de numeros aleatorios, paramentros limites: inferior, superior e a população
    l=[]
    limites=[Inferior,Superior]
    if Inferior<0 or Superior<0:
        a=Inferior+32.768
        b=Superior+32.768
        limites=[a,b]
    if passo==0: #continuo
        
        for x in range(0,populacao):
            recebe=random.random()*random.choice(limites)
            l.append(recebe)
        return l
    else: #discreto
        for x in range(0,populacao):
            recebe=random.randrange(Inferior,Superior)
            l.append(recebe)
        return l
 
Linferior=-32.768 #limite inferior 

Lsuperior=32.768 #limite superior

tamD=6 #tamanho em bits da parte inteira

tamE=26 #tamanho em bits da parte fracionária

bits=tamD+tamE+1 #tamanho do cromossomo

listaC1=[] #guarda os valores iniciais da caracteristica 1

listaC2=[] #guarda os valores iniciais da caracteristica 2

Escolhidos=[] #guarda os escolhidos aleatorios dos iniciais

Fitness=[] #guarda os valores da função fitness

populacao=20#escolhe a quantidade de individuos

TC=0.75 #taxa de cruzamento

TM=0.005# taxa de mutação

geracoes=220 #numero geraçoes, vai ser o número de vezes que vamos criar gerações



listaC1=geradorAleatorio(Linferior,Lsuperior,populacao,0) #valores da caracteristica 1 - decimal

listaC2=geradorAleatorio(Linferior,Lsuperior,populacao,0) #valores da caracteristica 2 - decimal

for x in range(0,populacao): #cria os cromossomos binários
    B1=Binario(listaC1[x],tamD,tamE)
    B2=Binario(listaC2[x],tamD,tamE)
    individuo=(B1,B2)
    Escolhidos.append(individuo)

for y in Escolhidos:
    z=0
    fitC1=Decimal(y[0])-32.768 #tirando o acréscimo que coloquei, para não dar números negativos nos binários
    fitC2=Decimal(y[1])-32.768
    z=function1(fitC1,fitC2)
    aplicada=Fitfunction1(z)
    Fitness.append(round(aplicada,6))

Gerados1= deepcopy(Escolhidos) #copia profunda dos individuos iniciais, garante que podemos modificar sem perder a informação inicial

Fitness1= deepcopy(Fitness) #copia profunda do fitness dos individuos iniciais, garante que podemos modificar sem perder a informação inicial

for geracao in range(0,geracoes):
    a=geraCasais(Gerados1,Fitness1,populacao)
    b=geraFilhos(a,TC,bits)
    c=Mutacao(b,TM)

    Gerados1=c
    Fitness1=[]
    print('Geração:',geracao)
    for y in Gerados1:
        z=0
        fitC1=Decimal(y[0])-32.768 #tirando o acréscimo que coloquei, para não dar números negativos nos binários
        fitC2=Decimal(y[1])-32.768
        z=function1(fitC1,fitC2)
        aplicada=Fitfunction1(z)
        print(fitC1,fitC2,aplicada)
        Fitness1.append(round(aplicada,6))
    media=sum(Fitness1)/populacao
    
    #print(c)
    #print('Média=',media)
    #print(Fitness1)
#print(Gerados1)
for numero in range(0,len(Gerados1)):
    pa=Gerados1[numero][0]
    pb=Gerados1[numero][1]
    #print((Decimal(pa)-32.768),(Decimal(pb)-32.768))



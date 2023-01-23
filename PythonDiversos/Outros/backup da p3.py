'''
for x in escolhidos: #calcula o fitness de cada individuo
    fit=Fitfunction(Decimal(x))
    fitness.append(fit)


Gerados= deepcopy(escolhidos) #copia profunda dos individuos iniciais, garante que podemos modificar sem perder a informação inicial

Fitness= deepcopy(fitness) #copia profunda do fitness dos individuos iniciais, garante que podemos modificar sem perder a informação inicial

geracoes=5 #numero geraçoes, vai ser o número de vezes que vamos criar gerações

print('população do inicio')
print(lista)
print('população selecionada de forma aleatória')
print(escolhidos)

for x in range(0,geracoes): #selecionamos, fazemos o crossover, mutação e construímos as gerações
    #a cada novo ciclo formamos novas gerações, não foi empregado o elitismo
    casais=geraCasais(Gerados,Fitness,populacao) #forma os casais mediante uma geração e seu fitness

    filhos=geraFilhos(casais,TC,bits) #os casais geram filhos, na proporção de 1 casal gera 1 filho

    geracaofinal=Mutacao(filhos,TM) #avaliamos se vai ocorrer mutação em alguém

    Gerados=geracaofinal #a geraçao finalizada

    Fitness=[]#fitness da geração
    for y in Gerados:
        Fit=Fitfunction(Decimal(y))
        Fitness.append(Fit)
    print('Geração:',x)
    print(casais,'casais')
    print(Gerados,'filhos')
    print(Fitness,'fitness de cada um')
    print(int(sum(Fitness)/populacao))
'''
'''
for x in range(0,geracoes): #selecionamos, fazemos o crossover, mutação e construímos as gerações
    #a cada novo ciclo formamos novas gerações, não foi empregado o elitismo
    GeradosC1=[]
    GeradosC2=[]
    for u in Gerados1:
        GeradosC1.append(u[0])
        GeradosC2.append(u[1])
    casaisC1=geraCasais(GeradosC1,FitnessC1,populacao)
    casaisC2=geraCasais(GeradosC2,FitnessC2,populacao)
    

    filhosC1=geraFilhos(casaisC1,TC,bits) #os casais geram filhos caracteristica 1, na proporção de 1 casal gera 1 filho
    filhosC2=geraFilhos(casaisC2,TC,bits) #os casais geram filhos caracteristica 2, na proporção de 1 casal gera 1 filho

    mutacaoC1=Mutacao(filhosC1,TM) #avaliamos se vai ocorrer mutação na caracteristica 1
    mutacaoC2=Mutacao(filhosC2,TM) #avaliamos se vai ocorrer mutação na caracteristica 2

  

    for o in range(0,populacao):
        ser=(mutacaoC1[o],mutacaoC2[o])
        Gerados1.append(ser)

    Fitness1=[]#fitness da geração
    FitnessC1=[]
    FitnessC2=[]
    for p in Gerados1:
        fitC1=Decimal(p[0])
        fitC2=Decimal(p[1])
        aplicadaC1=Fitfunction(fitC1)
        aplicadaC2=Fitfunction(fitC2)
        FitnessC1.append(aplicadaC1)
        FitnessC2.append(aplicadaC2)
    for y in Gerados1:
        Fit=Fitfunction(Decimal(y[0])+Decimal(y[1]))
        Fitness1.append(Fit)
    print('Geração:',x)
    print(casaisC1,'casaisC1')
    print(casaisC2,'casaisC2')
    print(Gerados1,'filhos')
    print(Fitness1,'fitness de cada um')
    print(int(sum(Fitness1)/populacao))
'''
import random
limites=[-32,32]
for x in range(0,5):
    a=random.random()*random.choice(limites)
    print(a)

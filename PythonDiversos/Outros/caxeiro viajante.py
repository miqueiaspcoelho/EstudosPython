import random as rd #biblioteca para escolha de números aleatórios


#definimos o número de cidades
#montamos uma matriz onde cada linha i representa uma cidade
#cada elemtento j dentro de i representa o custo de i para j
#obs: o custo de i para j quando i=j é sempre 0.

rotas=[
    [0,54,38,79],
    [54,0,76,46],
    [38,76,0,71],
    [79,46,71,0]
]

n_cidades=len(rotas)



#Função que checa a melhor rota dada uma cidade i, uma matriz de rotas e todas as cidades já visitadas.
#Foi implementada a condição de que se uma cidade já foi visitada, não podemos retornar à mesma
#desta forma excluímos as subrotas.

def MelhorRota(i,matriz,sai):
    temp=10000
    rota=''
    for x in range(0,len(matriz)):
        if matriz[i][x]!=0 and matriz[i][x]<=temp:
            if x not in sai:
                temp=matriz[i][x]
                rota=[i,x]
    return rota

#Checa de onde estamos saindo, qual nossas cidade i.
def Sai(matriz):
    return matriz[0]

#Checa para onde iremos, nosso destino, nossa cidade j.
def Cheguei(matriz):
    return matriz[1]

#lista que guarda de onde já saímos.
sai=[] 

#lista que guarda de onde já chegamos.
cheguei=[]

#Cidade aleatório de onde vamos começar.
#inicio=rd.randrange(0,n_cidades)
inicio=3
#Nosso custo de caminho
custo=0


#Nosso programa em si, toda a lógica foi desenvolvida aqui.
for x in range(0,len(rotas)-1):
    a=MelhorRota(inicio,rotas,sai)
    
    saida=Sai(a)
    chegada=Cheguei(a)
    custo+=rotas[saida][chegada]
    
    if saida not in sai:
        sai.append(saida)
        
    if chegada not in cheguei:
        cheguei.append(chegada)
        
    inicio=chegada

#Nosso caminho total percorrido
caminho=[]

#esse custo adicional nada mais é que a volta, ou seja, da última cidade para voltar para a primeira
#e assim finalizar nosso ciclo.
custoadicional=rotas[cheguei[-1]][sai[0]]

#Montamos nosso caminho com base nas saídas e chegadas.
for x in range(0,len(sai)):
    caminho.append(sai[x])
caminho.append(cheguei[-1])
caminho.append(sai[0])


#Exibimos nossos resultados obtidos.
print('saidas=',sai)
print('chegadas=',cheguei)
print('caminho=',caminho)
print('custo=',custo+custoadicional)

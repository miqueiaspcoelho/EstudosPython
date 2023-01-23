#Questão 2.
#i= linha j=coluna
'''calcula a distancia em quarteirão (de forma a ser usada como heuristica
#para a implementação do algoritmo A*'''
def distManhatan(numero,i,j):
    contV=0
    contH=0
    tabuleiroCerto=[[0,1,2],
                    [3,4,5],
                    [6,7,8]]
    stop=False
    for x in range(0,3):
        for y in range(0,3):
            if tabuleiroCerto[x][y]!= numero:
                stop=False
            else:
                stop=True
                distY=abs(x-i)
                distX=abs(y-j)
                distTotal=distX + distY
                return [(x,y),('dist=',distTotal),('distH=',distX),('distV=',distY)]
      
'''Calcula a distancia em quarteirão de cada peça do tabuleiro.
fazendo uso da função anteriormente citada, aqui passamos
um tabuleiro(matriz) de forma que nossa função trabalha sobre
ela calculando a distancia quarteirão relacionando as posições
que nossos números ocupam para as posições que eles devem ocupar
em um estado final, que seria nosso estado objetivo'''
def avaliaTabuleiro(tabuleiro):
    Ldistancias=[]
    for q in range(0,3):
        for w in range(0,3):
            a=tabuleiro[q][w]
            b=distManhatan(a,q,w)
            d=(str(a),(q,w),b)
            Ldistancias.append(d)
    return(Ldistancias)

#verifica onde está a nossa posição vazia.
'''Partindo do ponto que só podemos mover peças na horizontal
ou vertical essa função procura sempre onde temos a posição vazia,
ou seja, localiza para onde podemos mover'''
def buscaVazio(tabuleiro1):
    for e in range(0,3):
        for r in range(0,3):
            if tabuleiro1[e][r]==0:
                return ['vazio está=',(e,r)]

#diz quais as peças podem ser movidas, usando como base o espaço vazio
'''verifica quais peças estão nas redondezas do espaço vazio, dessa
forma temos todos os possiveis movimentos para um dado estado
do tabuleiro'''
def movePecas(tabuleiro2):
    podeMover=[]
    a=buscaVazio(tabuleiro2)
    q=a[1]
    b=avaliaTabuleiro(tabuleiro2)
    for z in b:
        c=z[1]
        if c[0] == q[0] and abs(c[1]-q[1])==1:
            #print('a',z[0])
            d=(str(z[0]))
            if d!='0':
                podeMover.append(d)
        if c[1] == q[1] and abs(c[0]-q[0])==1:
            #print('b',z[0])
            #print('c',abs(c[1]-q[1]))
            d=(str(z[0]))
            if d!='0':
                podeMover.append(d)
    return (podeMover)

#Checa qual o melhor movimento com base na distancia quarteirão.
'''levando em conta que todos os movimentos tem custo 1
ao final basta somar com o custo das distancias
quarteirão ao numero de movimentos, totalizando o custo total
essa função seleciona sempre o melhor movimento a ser executando
partindo dos movimentos possiveis para um dado estado do
tabuleiro, esse melhor movimento é sempre aquele com a menor
distância quarteirão'''
def melhorMovimento(tabuleiro3):
    menorCusto=[]
    Minimo=[]
    melhorMovimento=[]
    a=avaliaTabuleiro(tabuleiro3)
    y=movePecas(tabuleiro3)
    for b in a:
        c=b[2][1]
        d=c[1]
        e=(b[0],d)
        if b[0] in y:
            menorCusto.append(e)
    tam=len(menorCusto)
    t=5
    for z in range(0,tam):
        compara1= menorCusto[z][1]
        
        if compara1<=t:
            t=compara1
    Minimo.append(('a',t))
    for u in menorCusto:
        if u[1]==Minimo[0][1]:
            melhorMovimento.append(u)
            
    return(menorCusto,Minimo,melhorMovimento)
    
    
            
tabuleiroInicio=[[7,2,4],
                 [5,0,6],
                 [8,3,1]]
#Alguns Testes
'''u=avaliaTabuleiro(tabuleiroInicio)
a=u[0][2]
print(a[1])
for x in u:
    print(x)
a=movePecas(tabuleiroInicio)
o=melhorMovimento(tabuleiroInicio)
for x in o:
    print(x)
'''

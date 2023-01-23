from copy import deepcopy

'''teste=[[7,2,4],
       [5,0,6],
       [8,3,1]]'''

teste=[[7,2,4],
       [5,0,6],
       [8,3,1]]

#verifica sempre se o estado do tabuleiro é igual oa objetivo
#retorn um booleano
def checaObjetivo(tabuleiro):
    objetivo=[[0,1,2],[3,4,5],[6,7,8]]
    if tabuleiro==objetivo:
        return True
    else:
        return False


#encontra sempre onde está o vazio (zero)
#retorna a posição do zero no tabuleiro
def encontraVazio(tabuleiro):
    for x in range(0,3):
        for y in range(0,3):
            if tabuleiro[x][y]==0:
                return (x,y)


#encontra as posições para onde podemos mover o vazio.
#retorna as posições nas adjacências do zero
def paraOndeMoveVazio(tabuleiro):
    vazio=encontraVazio(tabuleiro)
    movePara=[]
    for x in range(0,3):
        for y in range(0,3):
            if tabuleiro[x][y]!=0:
                if  (x==vazio[0] and abs(y-vazio[1])==1) or (y==vazio[1] and abs(x-vazio[0])==1): 
                    movePara.append((x,y))
    return movePara


#distancia manhattan de uma peça
#retorna a distância Manhattan de uma peça no tabuleiro.
def distManhattan(numero,i,j):
    meta=[[0,1,2],[3,4,5],[6,7,8]]
    stop=False
    for x in range(0,3):
        for y in range(0,3):
            if meta[x][y]!= numero:
                stop=False
            else:
                stop=True
                distY=abs(x-i)
                distX=abs(y-j)
                distTotal=distX + distY
                return distTotal

def custo(tabuleiro):
    soma=0
    for x in range(0,3):
        for y in range(0,3):
            custo=distManhattan(tabuleiro[x][y],x,y)
            soma+=custo
    return soma

def geraEstados(tabuleiro):
    a=encontraVazio(tabuleiro)
    b=paraOndeMoveVazio(tabuleiro)
    estadosGerados=[]
    aux=deepcopy(tabuleiro)
    for x in b:
        aux=deepcopy(teste)
        c=aux[x[0]][x[1]]
        aux[x[0]][x[1]]=0
        aux[a[0]][a[1]]=c
        estadosGerados.append(aux)
    return estadosGerados

estadoInicial=[deepcopy(teste),custo(teste)]
B=[]
E=[]
B.append(estadoInicial)
stop=False
a=deepcopy(teste)
i=0
print(custo(a))
'''
while i<3:
    if B==[]:
        print('vish')
    no=B[0:]
    ultimo=no[-1]
    B=sorted(B, reverse=True)
    print(B)
    E.append(ultimo[0])
    if checaObjetivo(ultimo[0]):
        print('show')
        print(no)
        E.append(ultimo[0])
        stop=True
    
    for x in no:
        filho=geraEstados(x[0])
        for y in filho:
            if y not in B or y not in E:
                B.append([y,custo(y)])
            else:
                B[0]=[y,custo(y)] 
    i+=1
'''

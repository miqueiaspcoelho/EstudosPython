#Questão 1
N=['deee','deed','ddee','eddd','edde','eedd']#casos restringidos pelo problema

vizinhos = {
    #Possíveis estados
    'eeee':('deee','ddee','dede','deed'),
    'eeed':('deed','dded','dedd'),
    'eede':('ddde','dedd','dede'),
    'eedd':('dedd','dddd'),
    'edee':('ddee','ddde','dded'),
    'eded':('dded','dddd'),
    'edde':('ddde','dddd'),
    'eddd':('dddd',),
    'deee':('eeee',),
    'deed':('eeed','eeee'),
    'dede':('eede','eeee'),
    'dedd':('eedd','eeed','eede'),
    'ddee':('edee','eeee'),
    'dded':('eded','eeed','edee'),
    'ddde':('edde','eede','edee'),
    'dddd':('eddd','eedd','eded','edde'),
}

distancias = {
    #definimos o custo para cada passo como 1
    'eeee':(1,1,1,1),
    'eeed':(1,1,1),
    'eede':(1,1,1),
    'eedd':(1,1),
    'edee':(1,1,1),
    'eded':(1,1),
    'edde':(1,1),
    'eddd':(1,),
    'deee':(1,),
    'deed':(1,1),
    'dede':(1,1),
    'dedd':(1,1,1),
    'ddee':(1,1),
    'dded':(1,1,1),
    'ddde':(1,1,1),
    'dddd':(1,1,1,1),
}


def nosso_in(elemento,L):
    #A função retorna verdadeiro caso o nó já tenha sido explorado
    presente = False
    for i in range(len(L)):
        if elemento == L[i][0][-1]:
            presente = True
            break
    return presente

def objetivo(estado):
    return estado=='dddd'

estado_inicial = [['eeee'],0]

B = [] #fila de arnazenamento para busca em largura
E = [] #lista para armazenar os nós já visitados

B.append(estado_inicial)
achei = False
while not achei:
    if (len(B)==0):
        break
    print('b',B)
    no = B[0][:] #definimos o nó atual a ser explorado com os respectivos caminhos possíveis
    del B[0]
    E.append(no[0][-1])
    print('no',no)
    print('e',E)

    for vizinho in vizinhos[no[0][-1]]:
        print('aqui',no[0][-1])
        if not nosso_in(vizinho,B) and not vizinho in E and vizinho not in N:
            e = vizinhos[no[0][-1]].index(vizinho) #identifca o indice do nó atual, para identificação do custo
            d = distancias[no[0][-1]][e]  #o custo do caminho no nó atual
            if objetivo(vizinho):
                no[0].append(vizinho)
                no[1] += d
                achei = True
                break
            B.append([no[0] + [vizinho], no[1]+ d]) #adiciona o novo caminho atualizando o custo para chegar até este nó
            
    
if achei: 
    print(no)
else:
    print('Nao achei.')

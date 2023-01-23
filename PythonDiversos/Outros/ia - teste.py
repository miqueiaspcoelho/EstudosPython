#temos 4 variaveis, e cada uma pode estar na esquerda ou direita de um rio
#F- fazendeiro
#R- raposa
#C- galinha
#G- grãos
#cada variavel pode receber o valor E - esquerda ou D - direita.
#nós podemos ir para a direita ou ir para a esquerda
#Nosso estado inicial é: S= {E,E,E,E} ou seja, todo mundo na esquerda.
#Nosso estado objetivo (final) S={D,D,D,D}, todos na direita.
#Condições, não podemos deixar (C,G);(C,R). Só podemos levar o fazendeiro
#e outro item de cada vez.
#O custo para ir e voltar é unitário.

#gerador de espaços
L=['e','d']
R=[]
E=[]
i=1
for a in L:
    for b in L:
        for c in L:
            for d in L:
                aux=a+b+c+d
                R.append(aux)
vizinhos = {
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
    'eeee':(1,1,1,1),
    'eeed':(1,1,1),
    'eede':(1,1,1),
    'eedd':(1,1),
    'edee':(1,1,1),
    'eded':(1,1),
    'edde':(1,1),
    'eddd':(1),
    'deee':(1),
    'deed':(1,1),
    'dede':(1,1),
    'dedd':(1,1,1),
    'ddee':(1,1),
    'dded':(1,1,1),
    'ddde':(1,1,1),
    'dddd':(1,1,1,1),
}

#maneira de percorrer os caminhos
Erros=['eddd','deee','eedd','ddee','deed','edde']
objetivo='dddd'
'''Percorridos=[]
Erros=['eddd','deee','eedd','ddee','deed','edde']
Fails=[]
for x in caminhos.keys():
    tam=len(caminhos[x])
    print(x)
    if x in Erros:
        Fails.append(x)
    for y in range(0,tam):
        if x in Fails:
            print('erro=',x)
            break
        else:
            print(caminhos[x][y], 'tamanho=',tam)
    if x not in Fails:
        Percorridos.append(x)
    if x == objetivo:
        break

print(Fails,Percorridos)'''


def nosso_in(elemento,L):
    presente = False
    for i in range(len(L)):
        if elemento == L[i][0][-1]:
            presente = True
            break
    return presente

def objetivo(estado):
    return estado=='dddd'

estado_inicial = [['eeee'],0]

B = [] #fila
E = []

B.append(estado_inicial)
achei = False
while not achei:
  if (len(B)==0):
    break
  no = B[0][:]
  del B[0]
  E.append(no[0][-1])
  
  for vizinho in vizinhos[no[0][-1]]:
      if not nosso_in(vizinho,B) and not vizinho in E and vizinho not in Erros:
          e = vizinhos[no[0][-1]].index(vizinho)
          d = distancias[no[0][-1]][e]  
          if objetivo(vizinho):
            no[0].append(vizinho)
            no[1] += d
            achei = True
            break
          B.append([ no[0] + [vizinho], no[1]+ d  ])
          
  
if achei: 
  print (no)
else:
  print ('Nao achei.')


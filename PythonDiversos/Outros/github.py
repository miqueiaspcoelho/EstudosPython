def move(tab_original):
    """
    Checa possíveis movimentos (os nós)
    da árvore
    """
    movimentos = []
    tab = eval(tab_original)
    i = 0
    j = 0
    while 0 not in tab[i]: i += 1
    j = tab[i].index(0)


    if i<2:         #mover o 0 para baixo 
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]

    if i>0:         #mover o 0 para cima
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  
        movimentos.append(str(tab))
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  

    if j<2:         #mover o 0 para a direita
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j]

    if j>0:         #mover o 0 para a esquerda
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j]

    return movimentos

def h_misplaced(tabuleiro):
    """
    Implementa a heurística de 
    checar quantas peças estão 
    fora do lugar
    """
    misplaced = 0
    comparador = 1
    tab = eval(tabuleiro)
    for i in range(0,3):
        for j in range(0,3):
            if tab[i][j] != comparador:
                misplaced += 1
            comparador += 1
    return misplaced

def a_estrela(start,end):
    """
    Usa o A* para resolver
    o quebra-cabeça
    """
    explorado = []
    banco = [[h_misplaced(start),start]]
    while banco:
        i = 0
        for j in range(1,len(banco)):
            if (banco[i][0]) > (banco[j][0]):
               i = j
        caminho = banco[i]
        banco = banco[:i] + banco[i+1:]
        final = caminho[-1]
        if final in explorado: continue
        for movimento in move(final):
            if movimento in explorado: continue
            novo = [caminho[0] + h_misplaced(movimento) + h_misplaced(final)] + caminho[1:] + [movimento] 
            banco.append(novo)
        explorado.append(final)
        if final == end: break
    return caminho


tabuleiro = str([
                [7,3,4],
                [5,0,6],
                [8,3,1]
            ])

obj_final = str([
                [0,1,2],
                [3,4,5],
                [6,7,8]
            ])


print("Usando A*:")
for i in a_estrela(tabuleiro,obj_final):
    print(i, end="\n")

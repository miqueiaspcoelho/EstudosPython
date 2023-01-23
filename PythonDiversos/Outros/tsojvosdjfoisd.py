def percorre(lista):
        for x in range(0,len(lista)):
            print(lista[x])
class teste:
    def __init__(self,matriz):
        self.matriz=matriz
        self.insere=[]
    
    def inserir(self):
        a=percorre(self.matriz)   
rotas=[
    [0,54,38,79],
    [54,0,76,46],
    [38,76,0,71],
    [79,46,71,0]
]
a=teste(rotas)
a.percorre()
a.inserir()

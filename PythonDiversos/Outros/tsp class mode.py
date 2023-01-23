#BIBLIOTECA
import random as rd

#PARTE 1
class caixeiro:
    def __init__(self,matriz):
        self.matriz=matriz
        self.saidas=[]
        self.chegadas=[]
        self.caminho=[]
        self.custo=0
        self.inicio=rd.randrange(0,len(self.matriz))

#PARTE 2
    def soluction(self):
#PARTE 2.1  
        def MelhorRota(self,i):
            temp=10000
            rota=''
            for x in range(0,len(self.matriz)):
                if self.matriz[i][x]!=0 and self.matriz[i][x]<=temp:
                    if x not in self.saidas:
                        temp=self.matriz[i][x]
                        
                        rota=[i,x]
            return rota
#PARTE 2.2
        def Sai(matrizA):
            return matrizA[0]

        def Cheguei(matrizA):
            return matrizA[1]
#PARTE 2.3
        for x in range(0,len(self.matriz)-1):
            a=MelhorRota(self,self.inicio)
            SAIDA=Sai(a)
            CHEGADA=Cheguei(a)
            self.custo+=self.matriz[SAIDA][CHEGADA]

            if SAIDA not in self.saidas:
                self.saidas.append(SAIDA)

            if CHEGADA not in self.chegadas:
                self.chegadas.append(CHEGADA)

            self.inicio=CHEGADA
            
        u=self.chegadas[-1]
        v=self.saidas[0]
        custo_adicional=self.matriz[u][v]
        for x in range(0,len(self.saidas)):
            self.caminho.append(self.saidas[x])
        self.caminho.append(self.chegadas[-1])
        self.caminho.append(self.saidas[0])
        self.custo+=custo_adicional
#PARTE 3
    def exibir(self):
        print(' Saídas=',self.saidas,'\n',
              'Chegadas=',self.chegadas,'\n',
              'Caminho=',self.caminho,'\n',
              'Custo do Caminho',self.custo)

#PARTE 4
rotas=[
    [0,54,38,79],
    [54,0,76,46],
    [38,76,0,71],
    [79,46,71,0]
]

rotas1=[
    [0,9,10,15,17],
    [9,0,11,7,15],
    [10,11,0,14,6],
    [15,7,14,0,16],
    [17,15,6,16,0]
]

a=caixeiro(rotas)
b=caixeiro(rotas1)

a.soluction()
b.soluction()

b.exibir()
a.exibir()


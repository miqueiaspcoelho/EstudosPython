class pilha:
    def __init__(self):
        self.itens= []
    def vazia (self):
        return self.itens==[]
    def empilhar (self, item):
        self.itens.append(item)
    def desempilhar (self):
        self.itens.pop()
    def topo (self):
        print (self.itens[len(self.itens)-1])
    def tamanho (self):
        return len(self.itens)
    def imprimir(self):
        auxiliar = self.itens[::-1]
        for tudo in auxiliar:
            print (tudo)
    def soma(self):
        soma=0
        for tudo in self.itens:
            soma=soma+tudo
        print ('Soma:',soma)
#-------------------------------------------------------------------
class fila:
    def __init__(self):
        self.itens= []
    def vazia (self):
        return self.itens==[]
    def enfileirar (self, item):
        self.itens.insert(0,item)
    def desenfileirar (self):
        print (self.itens.pop())
    def frente (self):
        print( self.itens[-1])
    def tamanho (self):
        return len(self.itens)
    def imprimir(self):
        auxiliar = self.itens[::-1]
        for tudo in auxiliar:
            print (tudo)
    def soma(self):
        soma=0
        for tudo in self.itens:
            soma=soma+tudo
        print ('Soma:',soma)
#------------------------------------------------------------------
class no:
    def __init__(self,inidado):
        self.dado=inidado
        self.proximo= None
    def pegadado(self):
        return self.dado
    def pegaproximo(self):
        return self.proximo
    def botadado (self, novodado):
        self.dado=novodado
    def botaproximo (self, novoproximo):
        self.proximo = novoproximo
#------------------------------------------------------------------
class listanaoordenada:
    def __init__(self):
        self.inicio= None
    def vazia(self):
        return self.inicio==None
    def inserir (self,item):
        temp= no(item)
        temp.botaproximo(self.inicio)
        self.inicio=temp
    def buscar(self, item):
        atual= self.inicio
        encontrou = False
        while atual != None and not encontrou:
            if atual.pegadado()==item:
                encontrou= True
            else:
                atual= atual.pegaproximo()
        return encontrou
    def tamanho (self):
        atual = self.inicio
        conta= 0
        while atual != None:
            conta = conta +1
            atual= atual.pegaproximo()
        return conta
    def imprimir (self):
        atual= self.inicio
        while atual != None:
            print(str (atual.pegadado()))
            atual = atual.pegaproximo()

    def remover (self, item):
        previo= None
        atual= self.inicio
        encontrou= False
        while atual != None and not encontrou:
            if atual.pegadado()==item:
                encontrou= True
                atual= atual.pegaproximo()
                previo= previo.botaproximo(atual)
            else:
                previo=atual
                atual=atual.pegaproximo()
    def somapar(self):
        soma=0
        atual= self.inicio
        print('soma inicial=0')
        while atual != None:
            recebe= int(atual.pegadado())
            atual = atual.pegaproximo()
            if recebe%2==0:
                print('Número pares somados:',recebe)
                soma=soma+recebe
        if soma==0:
            print('Não há números pares')      
        return soma
    
    def maior(self):
        maior=0
        atual= self.inicio
        while atual!= None:
            recebe = int(atual.pegadado())
            atual= atual.pegaproximo()
            if recebe>maior:
                maior=recebe
        return maior

    def uniao(self,item):
        compara='´´´'
        atual= self.inicio
        lista=[]
        while atual!= None:
            recebe = float(atual.pegadado())
            atual= atual.pegaproximo()
            if str(recebe)!=compara:
                compara=recebe
                lista.append(compara)
        
        compara='´´´'
        atual= item.inicio
        lista1=[]
        while atual!= None:
            recebe = float(atual.pegadado())
            atual= atual.pegaproximo()
            if str(recebe)!=compara:
                compara=recebe
                lista1.append(compara)
        
        conjunto= lista + lista1
        conjunto=conjunto[::-1]
        print('O conjunto união é: ',conjunto)
        novalistauniao=listanaoordenada()
        for elementos in conjunto:
            novalistauniao.inserir(elementos)
        print('Os elementos que formam a nova lista encadeada são: ')
        novalistauniao.imprimir()
        print('O nome da nova lista é: novalistauniao\n')
        
    def intersecao(self,item):
        compara='´´´'
        atual=self.inicio
        lista=[]
        while atual!= None:
            recebe = float(atual.pegadado())
            atual = atual.pegaproximo()
            if str(recebe)!=compara:
                compara=recebe
                lista.append(compara)
        compara='´´´'
        atual=item.inicio
        lista1=[]
        while atual!= None:
            recebe = float(atual.pegadado())
            atual= atual.pegaproximo()
            if str(recebe)!= compara:
                compara=recebe
                lista1.append(compara)
        conjunto = lista + lista1
        conjunto=conjunto[::-1]
        quantidade=0
        intersecao=[]
        i=0
        for elementos in conjunto:
            x=conjunto[i]
            for numeros in conjunto:
               if x==numeros:
                   quantidade+=1
            if quantidade>=2 and x not in intersecao:
                intersecao.append(x)
            quantidade=0
            i+=1
        print('O conjunto interseção é: ',intersecao)
        novalistaintersecao=listanaoordenada()
        for elementos in intersecao:
            novalistaintersecao.inserir(elementos)
        print('Os elementos que formam a nova lista encadeada são: ')
        novalistaintersecao.imprimir()
        print('O nome dessa nova lista é: novalistaintersecao\n')

    def diferenca(self,item):
               
        compara='´´´'
        atual=self.inicio
        lista=[]
        while atual!= None:
            recebe = float(atual.pegadado())
            atual = atual.pegaproximo()
            if str(recebe)!=compara:
                compara=recebe
                lista.append(compara)
        compara='´´´'
        atual=item.inicio
        lista1=[]
        while atual!= None:
            recebe = float(atual.pegadado())
            atual= atual.pegaproximo()
            if str(recebe)!= compara:
                compara=recebe
                lista1.append(compara)
        conjunto = lista + lista1
        conjunto=conjunto[::-1]
        quantidade=0
        intersecao=[]
        for elementos in conjunto:
            for numeros in conjunto:
               if elementos==numeros:
                   quantidade+=1
            if quantidade>=2 and elementos not in intersecao:
                intersecao.append(elementos)
            quantidade=0
                  
        if intersecao != []:
            for elementos in intersecao:
                conjunto.remove(elementos)
        
        for numeros in lista1:
            if numeros in conjunto:
                conjunto.remove(numeros)
        print('O conjunto diferença é:',conjunto)
        novalistadiferenca=listanaoordenada()
        for elementos in conjunto:
            novalistadiferenca.inserir(elementos)
        print('Os elementos que formam a nova lista encadeada são: ')
        novalistadiferenca.imprimir()
        print('O nome dessa nova lista é: novalistadiferenca\n')
        
    def semrepetidos(self):
        compara='´´´'
        atual=self.inicio
        lista=[]
        lista1=[]
        while atual!= None:
            recebe = float(atual.pegadado())
            atual = atual.pegaproximo()
            if str(recebe)!=compara:
                compara=recebe
                lista.append(compara)
        lista=lista[::-1]
        for elementos in lista:
            if elementos not in lista1:
                lista1.append(elementos)
        self.inicio=None
        for elementos in lista1:
            self.inserir(elementos)  
        print('Tirando as repetições a nova lista fica:')
        self.imprimir()

            
        
#1------------------------------------------------------------
# ATIVIDADE
'''
def somapar(self):
        soma=0
        atual= self.inicio
        while atual != None:
            recebe= int(atual.pegadado())
            atual = atual.pegaproximo()
            if recebe%2==0:
                soma=soma+recebe
        return soma
'''
'''
lista= listanaoordenada()
lista.inserir(1)
lista.inserir(3)
lista.inserir(3)
lista.inserir(77)
lista.inserir(5)
lista.inserir(9)
lista.inserir(7)
lista.inserir(5)
lista.inserir(5)
lista.inserir(15)
lista.inserir(25)
lista.inserir(25)
print('A soma é:',lista.somapar())
'''
#2--------------------------------------------------------------
'''
fila=fila()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
fila.imprimir()
# F
# F
# V
# F
# V
'''
#3--------------------------------------------------------------
'''
class decolagem:
    def __init__(self):
        self.itens=[]
    def inserir(self):
        tam=int(input('Quantos aviões?'))
        for tudo in range(0,tam):
            lista=[]
            aviao=str(input('Nome:'))
            
            numero= str(input('Número:'))
            lista.append(aviao)
            lista.append(numero)
            tupla=tuple(lista)
            self.itens.append(tupla)
        print(self.itens)
    def primeiro(self):
        print('pode decolar:',self.itens[0])
        self.itens.pop(0)
        
    def espera(self):
        for tudo in self.itens:
            print('Voo em espera:',tudo[0])
    def quantos(self):
        print('Voos aguardando decolagem:', len(self.itens))

esse=decolagem()
esse.inserir()
esse.quantos()
esse.primeiro()
esse.espera()
'''
#4--------------------------------------------------------------
'''
pilha=pilha()
pilha.empilhar(10)
pilha.empilhar(5)
pilha.empilhar(3)
pilha.empilhar(40)
pilha.desempilhar()
pilha.empilhar(11)
pilha.empilhar(4)
pilha.empilhar(7)
pilha.desempilhar()
pilha.desempilhar()
pilha.imprimir()
pilha.soma()
'''
#soma=29
#5--------------------------------------------------------------
'''
def maior(self):
        maior=0
        atual= self.inicio
        while atual!= None:
            recebe = float(atual.pegadado())
            atual= atual.pegaproximo()
            if recebe>maior:
                maior=recebe
        return maior

lista= listanaoordenada()
lista.inserir(1)
lista.inserir(2)
lista.inserir(3000)
lista.inserir(4)
lista.inserir(5)
lista.inserir(6)
lista.inserir(7)
lista.inserir(8)
lista.inserir(9)
lista.inserir(10)
lista.inserir(20)
lista.inserir(22)
print('O maior número é: ',lista.maior())
'''
#6-

'''
lista=[1,2,3]
lista1=[4,5,6]
conjunto= lista + lista1
conjunto= set(conjunto)
print(conjunto)
'''
'''
a=listanaoordenada()
b=listanaoordenada()
a.inserir(100)
a.inserir(2)
a.inserir(2)
a.inserir(1)
a.inserir(5)

b.inserir(99)
b.inserir(74)
b.inserir(86)

a.imprimir()
b.imprimir()
a.uniao(b)
a.intersecao(b)
a.diferenca(b)
'''
#-------------------------------------------------
#7-
'''
a=listanaoordenada()
a.inserir(1)
a.inserir(1)
a.inserir(3)
a.semrepetidos()
'''

#--------------------------------------------------
# ESTUDANDO

'''    
casa = listanaoordenada()
casa.inserir(1)
casa.inserir(2)
casa.inserir(3)
print('o tamanho é: ',casa.tamanho())
casa.remover(1)
print('o tamanho é: ',casa.tamanho())


             
        
    
      

temp= no('casa')
print(temp.pegadado())
print(temp.pegaproximo())
temp.botadado('rua')
print(temp.pegadado())
print(temp.pegaproximo())



pilha= pilha()
fila=fila()
'''

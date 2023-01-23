'''
def fat (m):

    if m == 1:

        return 1

    else: 

        return m * fat (m-1)

    

def somatorio2 (n):

    if n == 1 or n==0:

        return n

    else:

        return fat(n)/n + somatorio2(n-1)


def fatorial(n):
    if n==1 or n==0:
        return 1
    else:
        return fatorial(n-1) * n


def soma(n):
    if n==0:
        return False
    if n==1:
        return 1
    else:
        return fatorial(n)/n + soma(n-1)



'''
#1
#letra A dá valores negativos quando coloco números pares, não sei o poquê.
def soma2(n):
    if n==1:
        return 1
    else:
        return -1 * soma2(n-1) + 1 /n


#letra B
def soma3(n):
    if n<=3:
        return False
    if n==4:
        return 2*n + 6
    else:
        return soma3(n-1) + n*2

#5
class no:

    def  __init__(self,dado):
        self.esq=None
        self.dir=None
        self.dado= dado
        
class arvore:
    
    def __init__(self):
        self.raiz=None
        
    def pegaraiz(self):
        return self.raiz

    def pegaraizvalor(self):
        if self.raiz!=None:
            return self._pegaraiz(self.raiz)
    
    def _pegaraiz(self,node):
        return node.dado
    
    
    def pegaevalor(self):
        if self.raiz!=None:
            return self._pegae(self.raiz)
    
    def _pegae(self,node):
        if node!=None:
            node=node.esq
        return node.dado
    
    
    def pegadvalor(self):
        if self.raiz!=None:
            return self._pegad(self.raiz)
    
    def _pegad(self,node):
        if node!=None:
            node=node.dir
        return node.dado

    def maior(self):
        if self.raiz!=None:
            return self._maiore(self.raiz)
    def _maiore(self,node):
        if node.esq!=None:
            node=node.esq
        return self._caidireita(node)
    def _caidireita(self,node):
        if node.dir!=None:
            node.dir=self._caidireita(node.dir)
        else:
            print(node.dado)
            return node.dado

    def inserir(self,val):
        if (self.raiz == None):
            self.raiz = no(val)
        else:
            self._inserir(val,self.raiz)
            
    def _inserir(self,val,node):
        if(val < node.dado):
            if(node.esq != None):
                self._inserir(val,node.esq)
            else:
                node.esq = no(val)
        else:
            if (node.dir != None):
                self._inserir(val,node.dir)
            else:
                node.dir = no(val)

    

    def imprimirpre(self):
        if(self.raiz!=None):
            self._imprimirpre(self.raiz)


    def imprimirem(self):
        if (self.raiz!=None):
            self._imprimirem(self.raiz)


    def imprimirpos(self):
        if (self.raiz!=None):
            self._imprimirpos(self.raiz)


    def _imprimirpre(self,node):
        if (node!=None):
            print (str(node.dado))
            self._imprimirpre(node.esq)
            self._imprimirpre(node.dir)


    def _imprimirem(self,node):
        if (node!=None):
            self._imprimirem(node.esq)
            print (str(node.dado))
            self._imprimirem(node.dir)


    def _imprimirpos(self,node):
        if (node!=None):
            self._imprimirpos(node.esq)
            self._imprimirpos(node.dir)
            print (str(node.dado))


    def icognita(self):
        if (self.raiz != None):
            print  (self._icognita(self.raiz))
            
    def _icognita(self,node):
        aux_esq=0
        aux_dir=0
        if node.esq != None:
            aux_esq = self._icognita(node.esq)
        if node.dir != None:
            aux_dir = self._icognita(node.dir)
        if (node.esq != None) or (node.dir != None):
            return  1 + aux_esq + aux_dir
        else:
            return 0

    def imprimir_folhas(self):
        if (self.raiz != None):
            self._imprimirfolhas(self.raiz)
    def _imprimirfolhas(self,node):
        if node.esq != None:
            self._imprimirfolhas(node.esq)
        if node.dir != None:
            self._imprimirfolhas(node.dir)
        if (node.esq==None) and (node.dir==None):
            print(str(node.dado))

    def buscar(self,val):
        if self.raiz==None:
            return 'vazia'
        else:
            return self._buscar(val,self.raiz)

    def _buscar(self,val,node):
        if(val < node.dado):
            if(node.esq != None):
                print(val,node.dado)
                node.dado=self._buscar(val,node.esq)
                
        if(val>node.dado):
            if (node.dir != None):
                print(val,node.dado)
                node.dado=self._buscar(val,node.dir)
                
        if (val==node.dado):
            return val 

    def pares(self):
        if (self.raiz!=None):
            self._pares(self.raiz)
    def _pares(self,node):
        if (node!=None):
            self._pares(node.esq)
            self._pares(node.dir)
            if node.dado%2==0:
                print (str(node.dado))

    def altura(self):
        if self.raiz!=None:
            return self._altura(self.raiz)
        else:
            return 0
    def _altura(self,node):
        hesq=0
        hdir=0
        if node.esq != None:
            hesq= self._icognita(node.esq)
        if node.dir != None:
            hdir = self._icognita(node.dir)
        if (node.esq != None) or (node.dir != None):
            if hesq >=hdir:
                return hesq +1
            if hdir > hesq:
                return hdir +1
        else:
            return 0

    def doisfilhos(self):
        if self.raiz!=None:
            self._doisfilhos(self.raiz)
        else:
            return 'vazia'
    def _doisfilhos(self,node):
        if node.esq != None:
            self._doisfilhos(node.esq)
        if node.dir != None:
            self._doisfilhos(node.dir)
        if (node.esq!=None) and (node.dir!=None):
            print(str(node.dado))
        

    def umfilho(self):
        if self.raiz!=None:
            self._umfilho(self.raiz)
        else:
            return 'vazia'
    def _umfilho(self,node):
        
        if node.esq!=None:
            self._umfilho(node.esq)
            
        if node.dir!=None:
            self._umfilho(node.dir)

        if node.esq==None:
            if node.dir!=None:
                d=False
            self._umfilho(node.dir)
            
        
        
t=arvore()
t.inserir(15)
t.inserir(20)
t.inserir(9)
t.inserir(5)
t.inserir(10)
print(t.maior())







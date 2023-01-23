class Dado:
    def __init__(self):
        self.dado=[]
    def Inserir(self):
        p=int(input("Quantos números '1' foram jogados: "))
        o=int(input("Quantos números '2' foram jogados: "))
        u=int(input("Quantos números '3' foram jogados: "))
        y=int(input("Quantos números '4' foram jogados: "))
        t=int(input("Quantos números '5' foram jogados: "))
        r=int(input("Quantos números '6' foram jogados: "))
        for i in range(p):
            self.dado.append(1)
        for i in range(o):
            self.dado.append(2)
        for i in range(u):
            self.dado.append(3)
        for i in range(y):
            self.dado.append(4)
        for i in range(t):
            self.dado.append(5)
        for i in range(r):
            self.dado.append(6)
    def média(self):
        media=0
        for x in range(len(self.dado)):
            media+=self.dado[x]
        print('Média',media/len(self.dado))
    def mediana1(self):
        L=[4,5,4,3,3,6,4,4,2,5,5,6,4,6,6,5,1,6,1,1,6,5,1,2,1,3,2,1,6,4,5,3,4,
           2,4,1,5,4,5,5,4,1,2,3,4,3,3,1,5,2,3,3,6,6,5,3,6,6,2,3,6,5,2,4,5,2,
           5,2,1,6,5,2,2,6,4,1,4,4,5,1,2,2,1,6,6,1,5,6,2,2,4,1,2,4,5,5,2,6,2,
           4,1,2,2,4,1,3,2,5,4,5,3,6,1,6,4,5,6,6,1,4,3,2,2,3,2,3,5,3,4,4,3,1,
           6,5,4,5,2,1,5,4,6,5,2,1,6,5,4,1,4,5,5,6,5,3,6,5,6,2,2,5,4,2,3,6,5,
           6,2,1,4,1,1,2,2,3,1,3,5,2,6,2,3,5,2,2,1,2,3,6,3,3,4,6,1,6,2,1,5,5,
           6,3,6,3,6,3,5,3,6,3,1,6,2,6,5,4,4,1,6,2,4,3,2,5,4,4,2,4,5,5,1,1,3,
           3,1,4,3,5,3,3,6,5,5,2,1,1,6,5,2,1,5,3,2,5,3,5,6,6,4,2,1,5,2,1,2,2,
           2,1,1,2,3,5]
        A=len(L)
        if A%2==0:
            a=(A-2)/2
            b=a+1
            a=int(a)
            b=int(b)
            c=L[a]
            d=L[b]
            print('Termo:',a+1,'=',c)
            print('Termo:',b+1,'=',d)
        mediana=(c+d)/2
        print('Mediana ordenada por ordem de lançamanto:',mediana)
        
    def mediana(self):
        L=[4,5,4,3,3,6,4,4,2,5,5,6,4,6,6,5,1,6,1,1,6,5,1,2,1,3,2,1,6,4,5,3,4,
           2,4,1,5,4,5,5,4,1,2,3,4,3,3,1,5,2,3,3,6,6,5,3,6,6,2,3,6,5,2,4,5,2,
           5,2,1,6,5,2,2,6,4,1,4,4,5,1,2,2,1,6,6,1,5,6,2,2,4,1,2,4,5,5,2,6,2,
           4,1,2,2,4,1,3,2,5,4,5,3,6,1,6,4,5,6,6,1,4,3,2,2,3,2,3,5,3,4,4,3,1,
           6,5,4,5,2,1,5,4,6,5,2,1,6,5,4,1,4,5,5,6,5,3,6,5,6,2,2,5,4,2,3,6,5,
           6,2,1,4,1,1,2,2,3,1,3,5,2,6,2,3,5,2,2,1,2,3,6,3,3,4,6,1,6,2,1,5,5,
           6,3,6,3,6,3,5,3,6,3,1,6,2,6,5,4,4,1,6,2,4,3,2,5,4,4,2,4,5,5,1,1,3,
           3,1,4,3,5,3,3,6,5,5,2,1,1,6,5,2,1,5,3,2,5,3,5,6,6,4,2,1,5,2,1,2,2,
           2,1,1,2,3,5]
        L=sorted(L)
        A=len(L)
        if A%2==0:
            a=(A-2)/2
            b=a+1
            a=int(a)
            b=int(b)
            c=L[a]
            d=L[b]
        mediana=(c+d)/2
        print('Mediana ordenada por ordem crescente:',mediana)

        print('A quantidade total de amostras foi:',len(self.dado))
    def moda(self):
        self.dado.sort()
        l={}
        L={}
        p=int(self.dado.count(1))
        o=int(self.dado.count(2))
        i=int(self.dado.count(3))
        u=int(self.dado.count(4))
        y=int(self.dado.count(5))
        t=int(self.dado.count(6))
        lista=[p,o,i,u,y,t]
        l['1']=p
        l['2']=o
        l['3']=i
        l['4']=u
        l['5']=y
        l['6']=t
        L[p]='1'
        L[o]='2'
        L[i]='3'
        L[u]='4'
        L[y]='5'
        L[t]='6'
        print(l)
        m=max(l.values())
        R=lista.count(m)
        if R>1:
            print('Alguns números se repetem a mesma quantidade de vezes')
        else:
            print('\nModa:',L[m])
    def media_quadratica(self):
        soma=0
        for todos in self.dado:
            soma=soma+(todos)**2
        media=soma/len(self.dado)
        media=media**0.5
        print('Média quadrática',media)
    
    def frequência(self):
        p=self.dado.count(1)
        o=self.dado.count(2)
        i=self.dado.count(3)
        u=self.dado.count(4)
        y=self.dado.count(5)
        t=self.dado.count(6)
        print("\n A frequencia de '1' é: ",p)
        print(" A frequencia de '2' é: ",o)
        print(" A frequencia de '3' é: ",i)
        print(" A frequencia de '4' é: ",u)
        print(" A frequencia de '5' é: ",y)
        print(" A frequencia de '6' é: ",t)
    def frequencia_relativa(self):
        p=self.dado.count(1)
        o=self.dado.count(2)
        i=self.dado.count(3)
        u=self.dado.count(4)
        y=self.dado.count(5)
        t=self.dado.count(6)
        A=len(self.dado)
        print("\n A frequência relativa de 1:",(p/A))
        print(" A frequência relativa de 2:",(o/A))
        print(" A frequência relativa de 3:",(i/A))
        print(" A frequência relativa de 4:",(u/A))
        print(" A frequência relativa de 5:",(y/A))
        print(" A frequência relativa de 6:",(t/A))
        print("\nPercentual de 1 =",round(((p/A)*100),5),'%')
        print("Percentual de 2 =",round(((o/A)*100),5),'%')
        print("Percentual de 3 =",round(((i/A)*100),5),'%')
        print("Percentual de 4 =",round(((u/A)*100),5),'%')
        print("Percentual de 5 =",round(((y/A)*100),5),'%')
        print("Percentual de 6 =",round(((t/A)*100),5),'%')
    def pqtqueda(self):
        queda=int(input("\nQuantas vezes o dado caiu da mesa? "))
        pqt=(queda*100)/(len(self.dado))
        print('Porcentagem de queda em relação ao total:',round(pqt,5),'%')
class Moeda:
    def __init__(self):
        self.dado=[]
    def Inserir(self):
        cara=int(input("\nQuantos vezes saiu CARA?: "))
        coroa=int(input("Quantas vezes saiu COROA?: "))
        for i in range(cara):
            self.dado.append('cara')
        for i in range(coroa):
            self.dado.append('coroa')
    def amostras(self):
        T=len(self.dado)
        print('\nTotal de amostras: ',T)
    def moda(self):
        cara=self.dado.count('cara')
        coroa=self.dado.count('coroa')
        if cara>coroa:
            print('Moda: ','CARA =',cara)
        if cara<coroa:
            print('Moda: ','COROA =',coroa)
        if cara==coroa:
            print('Caíram em mesma quantidade, não há moda')
    def frequencia(self):
        cara=self.dado.count('cara')
        coroa=self.dado.count('coroa')
        print('\nFrequência (CARA)=', cara)
        print('Frequência (COROA)=',coroa)
    def frerelativa(self):
        cara=self.dado.count('cara')
        coroa=self.dado.count('coroa')
        A=len(self.dado)
        print('\nFrequência relativa (CARA) =', (cara/A))
        print('Frequência relativa (COROA) =', (coroa/A))
        print('\nPercentual (CARA) =', round(((cara/A)*100),5),'%')
        print('Percentual (COROA) =', round(((coroa/A)*100),5),'%')

D=Dado()
D.Inserir()
D.mediana()
D.mediana1()
D.media_quadratica()
D.média()
D.moda()
D.frequência()
D.frequencia_relativa()


M=Moeda()
M.Inserir()
M.amostras()
M.moda()
M.frequencia()
M.frerelativa()

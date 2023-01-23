#IMPORTANDO AS BIBLIOTECAS A SEREM UTILIZADAS
import matplotlib.pyplot as plt
import numpy as np

#VALORES DE VENDA DO DOLAR NO MÊS DE OUTUBRO
#Pares ordenados com o dia e o valor correspondente.
'''Pontos=[(1,4.1740),(2,4.1546),(3,4.1012),(4,4.0610),(5,4.0610),
(6,4.0610),(7,4.0688),(8,4.0868),(9,4.0954),(10,4.1145),
(11,4.1060),(12,4.1060),(13,4.1060),(14,4.1263),(15,4.1488),
(16,4.1714),(17,4.1457),(18,4.1376),(19,4.1376),(20,4.1376),
(21,4.1319),(22,4.0858),(23,4.0721),(24,4.0089),(25,4.0133),
(26,4.0133),(27,4.0133),(28,3.9793),(29,3.9946),(30,4.0186),
(31,4.0041)]'''

Pontos=[(1,5.5296),(2,5.5296),(3,5.5296),(4,5.5826),(5,5.6838),(6,5.7336),
(7,5.6002),(8,5.6864),(9,5.6864),(10,5.6864),(11,5.7337),(12,5.8391),
(13,5.7443),(14,5.5884),(15,5.5634),(16,5.5634),(17,5.5634),(18,5.629),
(19,5.5845),(20,5.6573),(21,5.5468),(22,5.5076),(23,5.5076),(24,5.5076),
(25,5.5263),(26,5.4945),(27,5.5324),(28,5.6579),(29,5.7036),(30,5.7036),
(31,5.7036),(32,5.7919),(33,5.7636),(34,5.6967),(35,5.6843),(36,5.6843),
(37,5.6843),(38,5.6843),(39,5.6573),(40,5.6257),(41,5.5858),(42,5.5811),
(43,5.6439),(44,5.6439),(45,5.6439),(46,5.6576),(47,5.7058),(48,5.693),
(49,5.6228),(50,5.6322),(51,5.6322),(52,5.6322),(53,5.5744),(54,5.526),
(55,5.526),(56,5.4964),(57,5.4781),(58,5.4781),(59,5.4781),(60,5.456),
(61,5.4418),(62,5.3999)]

tam=len(Pontos)
MB=[]
F=[]
C=0
#Laços para organizar as iterações
for x in range (0,tam):
        
    for j in range (x+1,tam):
        '''print(Pontos[j][1])'''
        m=((Pontos[j][1])-(Pontos[x][1]))/((Pontos[j][0])-(Pontos[x][0]))
        b=(Pontos[x][1])+ (m*(Pontos[x][0])*(-1))
        tupla=(m,b)
        MB.append(tupla)
        f=0
        #Testando cada m e b obtido em cada uma das funções.
        for z in range (0,tam):
                      
            f=f + abs((m*(Pontos[z][0])) + b - (Pontos[z][1]))
        F.append(f)
        C=f
        #Comparando para ver com qual m e b obtemos o minimo da função.
        for t in range (0,len(F)):
            if C>=F[t]:
                u=t
                C=F[t]
#Imprimindo os resultados obtidos
print('Numero de iterações efetuadas=',len(MB),'\n')
print('Ponto onde a função assume mínimo=',MB[u],'encontrado na iteração',u+1,'\n')
print('Mínimo da função=',C,'\n')
print('Reta de melhor ajuste: y=',MB[u][0],'x  +', MB[u][1])

#Plotando o gráfico
X=[]
Y=[]
for x in range (0,len(Pontos)):
    X.append(Pontos[x][0])
    Y.append(Pontos[x][1])
x = np.linspace(min(X)-2,max(X)+2,num=1000)
y = x
plt.xlim(-1,max(X)+1)
plt.ylim(min(Y)-0.2,max(Y)+0.2)
plt.xlabel('DIA')
plt.ylabel('VALOR DO DOLAR')
plt.grid(True)
plt.title('VALORES DO DOLAR (OUTUBRO DE 2019)')
plt.plot(x,((y*MB[u][0])+MB[u][1]),'b-', drawstyle='default') 
plt.scatter(X, Y, marker="o", color='red')
plt.show()


'''
a=len(MB)
for x in range (0,a):
    b=MB[x][0]
    b=str(b)
    b=b.replace('.',',')
    c=MB[x][1]
    c=str(c)
    d=F[x]
    d=str(d)
    d=d.replace('.',',')
    c=c.replace('.',',')
    print('M=',b,' ','B=',c,'  F(M,B)',d)
print(a)
'''     
           
        
        
            
        

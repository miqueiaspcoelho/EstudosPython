#IMPORTANDO AS BIBLIOTECAS NECESSÁRIAS
import matplotlib.pyplot as plt
import numpy as np

#DADOS DA COTAÇÃO DO DÓLAR

dados=[(1,5.5296),(2,5.5296),(3,5.5296),(4,5.5826),(5,5.6838),(6,5.7336),
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

#TERMOS DA MATRIZ NORMAL (M pertencem à matriz A e N  à matriz B)

M00=len(dados)

M10=0
M01=0
M11=0

N00=0
N01=0

#EFETUANDO OS SOMATÓRIOS
for dado in dados:
    
    M10=M10 + dado[0]
    M11=M11 + (dado[0])**2
    
    N00=N00 + dado[1]
    N01=N01 + (dado[0] * dado[1])

M01=M10

#DETERMINANTE DA MATRIZ
det=(M00*M11) - (M01**2)

#ENCONTRANDO O COEFIENTE ANGULAR E LINEAR DA RETA
if det!=0:
    b= ((N01*M00) - (M01*N00))/det
    a=(N00 - (M10*b))/M00

#CÁLCULO DO ERRO QUADRÁTICO
EQS=0
for dado in dados:
    EQS=EQS+(dado[1]-(a+b*dado[0]))**2

EQ=EQS**0.5


#EXIBINDO OS RESULTADOS
print('Matriz A')
print('|',M00,' ',M10,'|\n|',M01,' ',M11,'|')

print('Matriz B')
print('|',N00,'|\n|',N01,'|')

print('det A = ',det)

print('a=',a,' b=',b)
if b>0:
    print('reta: ',a,'+',b,'*x')
else:
    print('reta: ',a,'',b,'*x')

print('Erro quadrático= ',EQ)

#PLOTANDO O GRÁFICO
X=[]
Y=[]
for x in range (0,len(dados)):
    X.append(dados[x][0])
    Y.append(dados[x][1])
x = np.linspace(min(X)-2,max(X)+2,num=1000)
plt.xlim(-1,max(X)+1)
plt.ylim(min(Y)-0.2,max(Y)+0.2)

plt.xlabel('DIA')
plt.ylabel('VALOR DO DOLAR')
plt.grid(True)
plt.title('VALORES DO DOLAR 26/02/2021 a 28/04/2021')


plt.plot(x,(a+(x*b)),'b-', drawstyle='default') 
plt.scatter(X, Y, marker="o", color='red')
plt.show()



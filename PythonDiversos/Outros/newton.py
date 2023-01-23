import matplotlib.pyplot as plt
import numpy as np
#função f
def f(x):
    return (((x**3) + (2*(x**2)) - x + (37/500)))

#derivada de f
def derivadaf(x):
    return ((3*(x**2)) + (4*x - 1))

#newton

'''aqui eu mudei algumas coisas, ao invés de obtermos apenas 1 único valor,
vamos retornar uma lista de valores que vai ser composta por
uma lista de valores x, bem como seus respectivos f(x),
vamos usar esses valores para plotar o grafico'''

def newton(f,derivadaf,xo,erro,iteracoes):
    listax=[]
    listaf=[]
    
    listax.append(xo)
    listaf.append(f(xo))
    
    if abs(f(xo)) <=erro:
        return [listax,listaf]
    else:
        k=0
        while k<=iteracoes:
            x1=xo-f(xo)/derivadaf(xo)

            listax.append(x1)
            listaf.append(f(x1))
            
            if abs(f(x1))<=erro:
                return [listax,listaf]
            xo=x1
            k+=1
    return None

a=newton(f,derivadaf,1,0.001,10) #newton(função,derivada,xo,erro,iterações)

print(a[0]) #VALORES X OBTIDOS
print(a[1]) #VALORES DE F(X)OBTIDOS

#lógica só pra achar o melhor valor
MenorY=min(a[1])
valorY=a[1]

aux=valorY.index(MenorY)

valorX=a[0]
MelhorX=valorX[aux]

print(MelhorX,MenorY) #Melhor resposta obtida.

'''usei a biblioteca numpy para gerar 100 números entre intervalos,
usei isso pra gerar valores pra função e também pra gerar eixos X,Y
para melhor visualização'''

X=np.linspace(-0.1,1,num=100) #Gerando o eixo x
Y=np.linspace(-0.1,4,num=100) #Gerando o eixo y

'''Para plotar um grafico, o parâmetro plot recebe alguns argumentos,
os principais são: um valor para x e outro para y
plt.plot([lista de valores para x],'[lista de valores para y]'),
sem esses parâmetros o gráfico não é desenhado'''

plt.plot(X*0,Y,'r') #Plotando o eixo x (cor=vermelha)
plt.plot(X,X*0,'r') #plotando o eixo y (cor=vemelha)


'''Cada valor na lista X está sendo aplicado em f, dessa forma montamos
um gráfico para f e podemos analisar f em relação aos nossos valores
obtidos'''

plt.plot(X,(((X**3) + (2*(X**2)) - X + (37/500))),'b--') #função (cor=azul, tipo=tracejada)

plt.plot(a[0],a[1],'o') #plotando x,f(x) estão como ponto ('o')

plt.show() #exibindo o a imagem.
    
    


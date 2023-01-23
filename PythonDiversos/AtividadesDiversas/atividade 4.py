#Dada umalista L de números inteiros,
 #escreva uma função que imprima
 #os índices de todas as ocorrências
 #de um número especificado.
def vamosla4(l=[]):

    t=int(input('Quantos números tem a lista?'))
    for a in range(0,t):
        b=int(input('Digite o número: '))
        l.append(b)
    s=[]
    r=int(input('Qual número deseja saber as posições na lista? '))
    print([a for a, j in enumerate(l) if j == r])
         
    
l=[]
vamosla4(l)

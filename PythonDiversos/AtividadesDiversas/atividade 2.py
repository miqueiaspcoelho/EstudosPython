#Dada umalista L de números inteiros,
#escreva uma função que imprima os itens de L
#de trás para frente,semutilizar reverse().

def vamosla2(l=[]):
    t=int(input('Quantos elementos deseja colocar na lista?'))
    for a in range (1,t+1):
        f=int(input('Digite o número:'))
        l.append(f)
        print(l)
    print(l[::-1])
    
    

        
l=[]
vamosla2(l)

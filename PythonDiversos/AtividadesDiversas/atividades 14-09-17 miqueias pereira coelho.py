#1
#Dada uma lista L de números inteiros, escreva uma
#função retorne uma lista P contendo todos os itens
#de L acrescidos em 10%.

def vamosla(l=[]):
    t=int(input('Quantos elementos deseja colocar na lista?'))
    for a in range (0,t):
        f=int(input('Digite o número:'))
        l.append(f)
        print(l)
    s=[]
    for a in l:
        a=((a*10)/100)+a
        s.append(a)
    print(s)

l=[]
vamosla(l)


#2
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


#3
#Dada umalista L de números inteiros,
#escreva uma função que retorne uma lista P
#contendo os itens de L sem repetição
def vamosla3(l=[]):

    t=int(input('Quantos números tem a lista?'))
    for a in range(0,t):
        b=int(input('Digite o número: '))
        if b not in l:

            l.append(b)
        
                
        
        
    print(l)
  
   
    


l=[]
vamosla3(l)


#4
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



#5
 #Dada umalista L de números inteiros,
 #escreva uma função que retorne uma lista P
 #com os valores ordenados de P,
 #agrupados em números pares primeiro e ímparesdepois.

def vamosla5(l=[]):

    t=int(input('Quantos números tem a lista?'))
    s=[]
    p=[]
    for a in range(0,t):
        b=int(input('Digite o número: '))
        
        if b%2==0:
            s.append(b)
            
        else:
            p.append(b)
            
    l.extend(s)
    l.extend(p)
    print(l)
        


l=[]
vamosla5(l)


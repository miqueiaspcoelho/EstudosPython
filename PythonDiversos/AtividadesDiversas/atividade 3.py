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

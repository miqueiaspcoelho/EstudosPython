#Faça um programa que leia duas listas com 10 elementos cada.
#Gere uma terceira lista de 20 elementos, cujos valores deverão
#ser compostos pelos elementos intercalados das duas outras listas.
def vamosla6(l=[],s=[]):

    print('A lista tem 10 elementos o professor quem disse')
    for a in range(0,10):
        b=int(input('Digite o número: '))
        l.append(b)
    print(l)
    
    print('Essa outra aqui  tem 10 elementos também')
    for a in range(0,10):
        c=int(input('Digite o número: '))
        s.append(c)
    print(s)
        
  
    
    


l=[]
s=[]

vamosla6(l,s)

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

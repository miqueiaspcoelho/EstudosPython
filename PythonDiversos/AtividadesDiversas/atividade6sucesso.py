def vamos2(u=[],l=[],s=[]):
    
    print('Duas listas, com 10 elementos cada')
    for a in range(0,10):
        b=int(input('Digite um número: '))
        l.append(b)
    print(l)
    for a in range(0,10):
        t=int(input('Digite um número: '))
        s.append(t)
    print(s)
    y=len(l)
    x=len(s)

    z=y+x
   
    print(z)
    v=0
    a=0
  
    
    for p in range(0,10):
      
    
        for a  in l:                        
                
            if v==0:
                u.append(a)
                l.remove(a)
                v=v+1
                    
                        
        for a in s:
           
            
            if v==1:
                u.append(a)
                s.remove(a)
                v=v-1
        
                   
                
    print(u)

l=[]
u=[]
s=[]
vamos2(u,l,s)

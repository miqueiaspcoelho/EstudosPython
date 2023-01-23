Pontos=[(-1,2),(-2,4),(5,0),(-4,11)]
tam=len(Pontos)
C=[]
C1=[]
Q=[]
for x in range (0,tam):
    a=1
    for j in range (0,tam):
        b=0
        if j!=x:
            a=a*(Pontos[x][0] - Pontos[j][0])
    b=0
    c=1
    #errado
    for y in range(x+1,tam):
        
        if x!=y:
            b=b+c*(-Pontos[x][0]*-Pontos[y][0])
            c=b
    
    C1.append(b)
    #errado até aqui.
    q=Pontos[x][1]/a
    C.append(a)
    Q.append(q)
    
                    
print(C1)
print(C)
            
'''
b=b*((-Pontos[x][0]) + (-Pontos[j][0]))
            c=(-Pontos[x][0]) * (-Pontos[j][0])
'''

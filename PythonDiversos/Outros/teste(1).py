#transforma números em binários
binario=[]
c=[]
'''
for x in range(2,10):
    if x>1:
        print('x=',x)
        a=x
        a=int(a/2)
        b=x%2
        print('resto antes de while=',b)
        print('a antes de while=',a)
        if a==1:
            c=str(b)+  str(a)
        if a!=1:
            c=str(b)
        while a!=1:
            b=a%2
            a=int(a/2)
            c= c + str(b)
            print('resto depois de while=',b)
            if a==1:
                c= c + str(a)
                print('a depois de while=',a)
            
        print('terminou')
        print(c[::-1])
    binario.append(c)
print(binario)
'''
Io=1
If=21
for x in range(Io,If):
    if x>1:
        a=x
        a=int(a/2)
        b=x%2
        if a==1:
            c=str(b)+  str(a)
        if a!=1:
            c=str(b)
        while a!=1:
            b=a%2
            a=int(a/2)
            c= c + str(b)
            if a==1:
                c= c + str(a)
        c=c[::-1]
        binario.append(c)
print(binario)
################################################################3

l=[]
skol=3.5
glacial=2.5
r=''
while r!='n':
    m=float(input('Digite o preço do mocotó: '))
    a=float(input('Digite a quantidade de skol: '))
    b=float(input('Digite a quantidade de glacial: '))
    s=a*skol
    g=b*glacial
    t=s+g+m
    l.append(t)
    print(l)
    r=str(input('Deseja continuar?(n/s) ')).lower()
print(l)
soma=sum(l)
print('total',soma)
    


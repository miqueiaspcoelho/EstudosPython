print('Calculadora')
a=float(input('Número: '))
b= float(input('Número: ')); 
s= str(input('Adição(+)\nSubtração(-)\nMultiplicação(*)\nDivisão(/)\n'))
z=a+b
y=a-b
k=a*b
p=a/b

if s=='+':
    z=a+b
    print(z)

if s=='-':
    y=a-b
    print(y)

if s=='*':
    k=a*b
    print(k)

if s=='/':
    p=a/b
    print(p)

t=str(input('Deseja continuar?(sim, não)\n')).lower()
if t=='não':
    quit()
if t=='sim' or t=='claro':
    while True:
        print('Vamos continuar')
        if s=='+':
            j=float(input('Mais um número para continuar somando:\n'))
            z=z+j
            print(z)
        if s=='-':
            h=float(input('Mais um número para continuar subtraindo:\n'))
            y=y-h
            print(y)
        if s=='*':
            m=float(input('Mais um número para continuar multiplicando:\n'))
            k=k*m
            print(k)
        if s=='/':
            u=float(input('Mais um número para continuar dividindo:\n'))
            p=p/u
            print(p)
            

def equ(a,b,c,):
    delta= (b**2)-(4*a*c)
    if delta <0:
        print('Não há solução no conjunto dos números reais')
    else:
        x1=((-1*b)+(delta**0.5))/2*a
        x2=((-1*b)-(delta**0.5))/2*a
        print('Valor de x1:',x1,'\nValor de x2:',x2)
    return
print('Resolvendo equações do segundo grau:')
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
c=int(input('Digite o valor de c:'))
equ(a,b,c)

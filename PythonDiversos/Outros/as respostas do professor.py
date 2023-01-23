qt1=0
qt2=0
qt3=0
qtd=int(input('Dados:'))
soma=0
for n in range (1,qtd+1):
    temp=float(input('Informe a temperatura:'))
    soma=soma+temp
    if temp>=35:
        qt1=qt1+1
    elif temp>=25 and temp <=34.9:
        qt2=qt2+1
    else:
        qt3=qt3+1
media=soma/qtd
p1=qt1/qtd*100
p2=qt2/qtd*100
p3=qt3/qtd*100
print('Média das temperaturas',media)
print('Percentual de dias com temperaturas maiores ou iguais a 35',p1)
print('Percentual de dias com temperaturas entre 25 e 34,9',p2)
print('Percentual de dias com temperaturas menores que 25',p3)

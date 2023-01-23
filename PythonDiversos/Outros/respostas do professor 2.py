x=float(input('Digite o valor de x:'))
soma=0
sinal=1
for n in range(1,21):
    termo=((x**n)/n)*sinal
    soma=soma+termo
    sinal=sinal*-1
print('O valor de log(1+x) é:',soma)

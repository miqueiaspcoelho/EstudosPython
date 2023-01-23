n= int(input('De quantos dias você tem os dados de temperatura: '))
q1=0
q2=0
q3=0
temp=0
for a in range(0,n):
    e=float(input('Qual a temperatura deste dia? '))
    temp=temp + e
    if e<25:
        q1=q1+1
    if e>=25 and  e<=34.9:
        q2=q2+1
    if e>=35:
        q3=q3+1
print('percentuais')
p1= (100*q1)/n
print('O percentual das temperaturas menores que 25 graus é: ',p1)
p2 = (100*q2)/n
print(' O percentual das temperaturas entre 25 graus e 34.9 é: ',p2)
p3 = (100*q3)/n
print('O percentual das temperaturas maiores ou iguais a 35 graus é: ',p3)

media=(temp)/n
print('Média das temperaturas: ',media)

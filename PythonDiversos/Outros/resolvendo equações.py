#Programa para resolver equações do primeiro e do segundo grau.


#Parte 1, definir se o usuário quer uma equação do primeiro ou segundo grau.
print('A sua equação é do primeiro ou do segundo grau?')

f= str(input()).lower()

#Se for do primeiro grau o computador vai calcular a equação.
if f=='primeiro':
    print('Vamos resolver a equação!!!!')
    while True:
        
        a= str(input('Digite o valor de: A '))
        if a=='0':
            print('Algo de errado não está certo, vamos tentar novamente.')
            continue
        b=str(input('Digite o valor de: B '))
        print('Esta é a sua equação?', a,'x +', b,)

        j= str(input()).lower()
        if j=='sim':
            break
        else:
            print('Vamos tentar mais uma vez')
            continue
    a= float(a)
    b= float(b)
    resposta= (-(b/a))
    print('Este é o valor de x: x=', resposta)
    print('Deseja algo mais? Posso descansar? Diz que sim, EU MEREÇO DESCANSAR, FALA SIM!!! ')
    m=str(input()).lower()
    if m=='sim':
        exit()

#Se for do segundo grau ele vai calcular a equação do segundo grau.
if f=='segundo':
    print('Resolva aqui as suas equações do segundo grau!!!')
    while True:
        a= str(input('Digite o valor de: A '))
        if a=='0':
            print('Valor de A inválido, melhor rever o valor de A, vamos lá. ')
            continue
            
        b= str(input('Digite o valor de: B '))
        c =str(input('Digite o valor de: C '))
        
        print('Esta é a sua equação?', a,'x**2 +', b,'* +', 'x', c )
        x= str(input()).lower()

        if x== 'sim':
            break
        else:
            print('Vamos tentar novamente.')
            continue
a = float(a)
b = float(b)
c= float(c)

delta= (b**2 - 4 * a * c)
print('Valor de delta', delta)
if delta==0:
    raiz= -b/(2*a)
    print('Duas raizes iguais:', raiz, raiz)
if delta > 0:
    raiz1= (-b+(delta**0.5))//(2*a)
    raiz2= (-b-(delta**0.5))//(2*a)
    print('Primeira raiz, x1=', raiz1,'. Segunda raiz, x2', raiz2)
if delta < 0:
    print('Não há solução no conjunto dos números reais,delta igual:', delta)
    print('Por hoje é só')
print('Deseja algo mais? Posso descansar? EI DIZ QUE SIM, NUNCA TE PEDI NADA.')
m=str(input()).lower()
if m=='sim':
    exit()


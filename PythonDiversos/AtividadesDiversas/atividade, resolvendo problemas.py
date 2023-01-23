#para checar se a pessoa pode dirigir.

print('Vamos ver se você pode dirigir. ')
ano_atual= int(input('Em que ano estamos? '))
nascimento= int(input('Em que ano você nasceu? '))
idade = ano_atual - nascimento
if idade<0:
    print('Coleguinha você é um viajante do tempo, em',ano_atual,'você ainda não nasceu')
elif idade<= 17:
    print('Que pena, ainda não pode dirigir, você só tem: ', idade)
else:
    print('Agora é só sucesso muleke, pode dirigir\n', idade)

# para ver qual número é maior.
print('Vamos ver qual o maior número dos três')
a= int(input('Digite um número: '))
b= int(input('Digite um número: '))
c= int(input('Digite um número: '))

if a>b and a>c:
       print('O maior número é: ',a)
elif b>a and b>c:
       print('O maior número é: ',b)
elif c>b and c>a:
    print('O maior número é: ',c)
elif a==b==c:
    print('São todos iguais')


#receber dois números inteiros e dizer qual o maior.
print('Vamos ver qual o maior dos dois números')
a= int(input('Digite um número: '))
b= int(input('Digite um número: '))
if a>b:
    print('O maior número é:',a)
elif b>a:
    print('O maior número é: ',b)
else:
    print('Os números são iguais')
    
#verificar se os números formam um triângulo e se sim qual o tipo.
print('Quais as medidas do lado?')
while True:
    a = int(input('Digite o primeiro lado: '))
    b = int(input('Digite o segundo lado: '))
    c = int(input('Digite o terceiro lado: '))
    if a+b>c and a+c>b and b+c>a:
        print('De fato existe esse triângulo, pois atende à condição de existência')
        break
    else:
        print('Vamos tentar mais uma vez')
        continue
if a==b==c:
    print('Triângulo equilátero')
if a==b or a==c or b==c:
    print('Triângulo isóceles')
if a!=b!=c:
    print('Triângulo escaleno')

#calcula o salário e o desconto, encima do salário bruto.
print('Vamos ver quanto é o seu salário final.')
salario= float(input('Digite seu salário bruto: '))
if salario<=800:
    desconto=salario*0.08
    print('Valor a ser descontado: ',desconto)
    print('Salário final: ', salario - desconto)
elif salario>800 and salario<1600:
    desconto=salario*0.11
    print('Valor a ser descontado: ',desconto)
    print('Salário final: ', salario - desconto)
elif salario>1600 and salario<4500.01:
    desconto=salario*0.14
    print('Valor a ser descontado: ',desconto)
    print('Salário final: ',salario - desconto)
else:
    desconto=salario*0.27
    print('Valor a ser descontado: ',desconto)
    print('Salário final: ', salario - desconto)


# Elabore um script que leia o nome completo
#de uma pessoa e imprima o prenome e o sobrenome
u=str(input('Digite seu nome completo: '))
u=u.split()
print(u[0],u[-1])

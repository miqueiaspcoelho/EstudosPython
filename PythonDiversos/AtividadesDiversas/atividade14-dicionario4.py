#4 - Suponha um dicionário D de estudantes,
#como definida no exemplo abaixo,
#onde cada par consiste do nome do estudante e das notas do mesmo.
#Escreva uma função chamada “aprovados” que receba
#como entrada o dicionário D
#e imprima o nome dos alunos aprovados.
#Um aluno é aprovado quando todas as suas notas são maiores que 7.
#Por exemplo, aprovados(D) deverá imprimir Denise.

dic={'Alano':(7.5,8.0,6.5),'Denise':(9.0,8.5,9.5),'Ana':(3.5,1.0,6.5)}
while True:
    pesquisar=str(input('Digite o nome de um aluno: ')).capitalize()
    if pesquisar not in dic:
        print('Não encontramos esse nome, por favor, tente novamente. ')
        continue
    else:
        break

a=dic[pesquisar]
b=len(a)
posi=0
pontos=0
for todos in range(0,b):
    
    if a[posi] >= 7:
        pontos=pontos+1
        posi+=1
    else:
        pontos=pontos-1
if pontos ==3:
    print('Estudante aprovado')
else:
    print('Estudante reprovado')


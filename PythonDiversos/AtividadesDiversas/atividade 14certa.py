#4 - Suponha um dicionário D de estudantes,
#como definida no exemplo abaixo,
#onde cada par consiste do nome do estudante e das notas do mesmo.
#Escreva uma função chamada “aprovados” que receba
#como entrada o dicionário D
#e imprima o nome dos alunos aprovados.
#Um aluno é aprovado quando todas as suas notas são maiores que 7.
#Por exemplo, aprovados(D) deverá imprimir Denise.

dic={'Alano':(7.5,8.0,6.5),'Denise':(9.0,8.5,9.5),'Ana Paula':(3.5,1.0,6.5)}
com=(7,7,7)
for todos in dic:    
    if (dic[todos][0]) > (com[0]) and (dic[todos][1]) > (com[1]) and (dic[todos][2]) > (com[2]):
        print(todos,',',dic[todos],'= aprovado(a)')
    else:
        print(todos,',',dic[todos],'= reprovado(a)')


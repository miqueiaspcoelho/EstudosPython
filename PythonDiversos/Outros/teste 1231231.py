def vamosladic(dic={}):
    com=(7,7,7)
    for todos in dic:    
        if (dic[todos][0]) > (com[0]) and (dic[todos][1]) > (com[1]) and (dic[todos][2]) > (com[2]):
            print(todos,',',dic[todos],'= aprovado(a)')
        else:
            print(todos,',',dic[todos],'= reprovado(a)')
dic={}
tam=int(input('Quantos alunos tem a lista: '))
for tudo in range(0,tam):
    aluno=str(input('Nome do aluno: '))
    nota1=float(input('Digite a primeira nota: '))
    nota2=float(input('Digite a segunda nota: '))
    nota3=float(input('Digite a terceira nota: '))
    notas=tuple(nota1)
    dic[nome]=notas

vamosladic(dic)

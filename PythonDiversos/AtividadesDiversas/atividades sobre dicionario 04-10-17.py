#1 - Crie um programa que, usando dicionário,
#crie uma agenda de tamanho fornecido inicialmente pelo usuário.
#Leia os dados (nome, telefone)
#de todos os contatos do usuário de forma que a
#agenda fique completa e por fim imprima todos os contatos.
#Por fim, faça uma pesquisa pelo nome e apresente o telefone
tamanho=int(input('Qual o tamanho da sua agenda? '))
dicionario={}
for agenda in range(0,tamanho):
    contato=str(input('Digite o nome do seu contato: '))
    numero=int(input('Digite o número do contato: '))
    dicionario[contato]=numero
print('Seus contatos e os respectivos números:\n',dicionario)

while True:
    busca=str(input('Qual contato deseja buscar? '))
    if busca in dicionario:
        print(dicionario[busca])
        pergunta=str(input('Buscar outro contato?(s/n) ')).lower()
        if pergunta =='s':
            continue
        else:
            break
        
    else:
        print('Contato não está na lista')
        pergunta=str(input('Pesquisar novamente?(s/n) ')).lower()
        if pergunta == 's':
            continue
        else:
            break
print('Isso é tudo pessoal')



#2- A seguinte tabela contém tradução de algumas palavras
 #em português para a língua dos piratas
 #Escreva um programa que pede que o usuário
 #digite uma frase em português e imprima a
 #tradução da frase para a língua dos piratas.

dic={'com':'',',':',','.':'.','o':'th\'','banheiro':'head','meu':'me','oi':'avast','é':'be','senhor':'matey','hotel':'fleabag inn','estudante':'swabbie',
     'garoto':'matey',' ':' ','madame':'proud beauty',
     'professor':'foul blaggart','restaurante':'galley','seu':'yer'
     
     ,'licença':'arr','estudantes':'swabbies','são':'be','advogado':'foul blaggart'}

print('\t\tEscreva uma frase com as palavras abaixo: \n\n'
      '\tsenhor, hotel, estudante, garoto, madame\n'
      '\tprofessor, restaurante, seu, com licença\n'
      '\testudantes, são, advogado, o, banheiro\n'
      '\t\t      meu, oi, é.\n\n')

pes=str(input('Vamos traduzir para a lígua dos piratas!!\n ')).lower()
pes=pes.split()
quantidade=len(pes)
posi=0
tradu=''
esp=' '
for todos in range(0,quantidade):
      trad=dic[(pes[posi])]
      tradu=tradu+esp+trad
      posi+=1
tradu=tradu.strip()
print(tradu.capitalize())      






#3- Escreva um programa que leia uma string do teclado
#e retorne uma tabela com a frequência
#com que cada letra aparece na string.
#Ignore se as letras são maiúsculas ou minúsculas.

palavra=str(input('Digite algo: ')).lower()
palavra.split()
vazio=''
for letras in palavra:
    if letras not in vazio:
        vazio=vazio+letras
dic={}
posi=0
for letras in palavra:
    a=palavra.count(letras)
    if letras not in dic:
        dic[letras]=a


for items in dic:

    print(vazio[posi],' ', dic[items])
    posi+=1






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


        


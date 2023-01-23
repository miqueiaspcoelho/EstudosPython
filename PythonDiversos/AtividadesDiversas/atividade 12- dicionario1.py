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

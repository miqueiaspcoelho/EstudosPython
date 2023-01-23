listalivros=[]
listaequipamentos=[]
listafuncionarios=[]
listadisciplinas=[]

def menu_inicial():
    print("Escolha um item: ")
    print("[1] LIVRO")
    print("[2] EQUIPAMENTO")
    print("[3] FUNCIONÁRIO")
    print("[4] DISCIPLINA CURSADA")
    opcao_ = int(input("Opção: "))
    return opcao_

def menu_livro():

    print("Digite a funcionalidade desejada: ")
    print("[1] LISTAR LIVROS")
    print("[2] LOCALIZAR LIVRO PELO CÓDIGO")
    print("[3] ADICIONAR LIVRO")
    print("[4] EXCLUIR LIVRO")
    print("[5] ALTERAR LIVRO")
    print("[6] RETORNAR AO MENU PRINCIPAL")
    opcao = int(input("Opção: "))
    if opcao==3:
        class livro:
            #cadastrar livro
            def __init__(self):
                print('LIVROS')
                b=str(input('Nome:'))
                c=str(input('Codigo:'))
                d=str(input('Editora:'))
                e=str(input('Ano:'))
                self.nome=b
                self.codigo=c
                self.editora=d
                self.ano=e
        a=livro()
        #joga livro na lista
        listalivros.append(a)
        r=int(input('Menu inicial(1)\nMenu livros(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_livro()
    if opcao==1:
        #imprime todos os livros da lista
        i=0
        for x in range(len(listalivros)):
            y=listalivros[x]
            print(y.nome,y.codigo,y.editora,y.ano)
            i=1
        if i==0:
            print('Não há livros cadastrados.')
        r=int(input('Menu inicial(1)\nMenu livros(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_livro()
    if opcao==2: 
        #localizar pelo codigo
        u=str(input('digite o codigo:'))
        i=0
        for x in range(len(listalivros)):
            o=listalivros[x]
            if o.codigo==u:
                print(o.nome,o.codigo,o.editora,o.ano)
                i=1
            
        if i==0:
            print('Livro não encontrado.')
        r=int(input('Menu inicial(1)\nMenu livros(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_livro()
    if opcao==4:
        #excluir livro
        u=str(input('Código:'))
        i=0
        for x in range(len(listalivros)):
            j=listalivros[x]
            if j.codigo==u:
                listalivros.remove(j)
                i=1
                break
        if i==0:
            print('Livro não encontrado')
        print('Total de livros na lista:',len(listalivros))
        r=int(input('Menu inicial(1)\nMenu livros(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_livro()
    if opcao==5:
        #alterar livro
        u=str(input('Código:'))
        for x in range(len(listalivros)):
            k=listalivros[x]
            if k.codigo==u:
                k.nome=str(input('Novo nome:'))
                k.codigo=str(input('Novo código:'))
                k.editora=str(input('Nova editora:'))
                k.ano=str(input('Novo ano de publicação:'))
        r=int(input('Menu inicial(1)\nMenu livros(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_livro()
    #voltar ao menu inicial
    if opcao==6:
        menu_inicial()

###################################################################################
def menu_equipamento():

    print("Digite a funcionalidade desejada: ")
    print("[1] LISTAR EQUIPAMENTO")
    print("[2] LOCALIZAR EQUIPAMENTO PELO CÓDIGO")
    print("[3] ADICIONAR EQUIPAMENTO")
    print("[4] EXCLUIR EQUIPAMENTO")
    print("[5] ALTERAR EQUIPAMENTO")
    print("[6] RETORNAR AO MENU PRINCIPAL")
    opcao = int(input("Opção: "))
    if opcao==3:
        class equipamento:
            #cadastrar equipamento
            def __init__(self):
                print('EQUIPAMENTOS')
                b=str(input('Nome:'))
                c=str(input('Codigo:'))
                d=str(input('Fabricante:'))
                e=str(input('valor:'))
                self.nome=b
                self.codigo=c
                self.fabricante=d
                self.valor=e
        a=equipamento()
        #joga equipamento na lista
        listaequipamentos.append(a)
        r=int(input('Menu inicial(1)\nMenu equipamentos(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_equipamento()
    if opcao==1:
        #imprime todos os equipamentos da lista
        i=0
        for x in range(len(listaequipamentos)):
            y=listaequipamentos[x]
            print(y.nome,y.codigo,y.fabricante,y.valor)
            i=1
        if i==0:
            print('Não há equipamentos cadastrados.')
        r=int(input('Menu inicial(1)\nMenu equipamentos(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_equipamento()
    if opcao==2: 
        #localizar pelo codigo
        u=str(input('Digite o codigo:'))
        i=0
        for x in range(len(listaequipamentos)):
            o=listaequipamentos[x]
            if o.codigo==u:
                print(o.nome,o.codigo,o.fabricante,o.valor)
                i=1
            
        if i==0:
            print('Equipamento não encontrado.')
        r=int(input('Menu inicial(1)\nMenu equipamentos(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_equipamento()
    if opcao==4:
        #excluir equipamento
        u=str(input('Código:'))
        i=0
        for x in range(len(listaequipamentos)):
            j=listaequipamentos[x]
            if j.codigo==u:
                listaequipamentos.remove(j)
                i=1
                break
        if i==0:
            print('Livro não encontrado')
        print('Total de equipamentos na lista:',len(listaequipamentos))
        r=int(input('Menu inicial(1)\nMenu equipamentos(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_equipamento()
    if opcao==5:
        #alterar equipamento
        u=str(input('Código:'))
        for x in range(len(listaequipamentos)):
            k=listaequipamentos[x]
            if k.codigo==u:
                k.nome=str(input('Novo nome:'))
                k.codigo=str(input('Novo código:'))
                k.editora=str(input('Novo fabricante:'))
                k.ano=str(input('Novo valor:'))
        r=int(input('Menu inicial(1)\nMenu equipamentos(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_equipamento()
    #voltar ao menu inicial
    if opcao==6:
        menu_inicial()



##################################################################################
def menu_funcionario():

    print("Digite a funcionalidade desejada: ")
    print("[1] LISTAR FUNCIONÁRIOS ")
    print("[2] LOCALIZAR FUNCIONÁRIOS PELO CÓDIGO")
    print("[3] ADICIONAR FUNCIONÁRIO")
    print("[4] EXCLUIR FUNCIONÁRIO")
    print("[5] ALTERAR FUNCIONÁRIO")
    print("[6] RETORNAR AO MENU PRINCIPAL")
    opcao = int(input("Opção: "))
    if opcao==3:
        class funcionario:
            #cadastrar equipamento
            def __init__(self):
                print('FUNCIONÁRIOS')
                b=str(input('Nome:'))
                c=str(input('Codigo:'))
                d=str(input('Profissão:'))
                e=str(input('Salário:'))
                self.nome=b
                self.codigo=c
                self.profissao=d
                self.salario=e
        a=funcionario()
        #joga funcionario na lista
        listafuncionarios.append(a)
        r=int(input('Menu inicial(1)\nMenu funcionários(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_funcionario()
    if opcao==1:
        #imprime todos os funcionarios da lista
        i=0
        for x in range(len(listafuncionarios)):
            y=listafuncionarios[x]
            print(y.nome,y.codigo,y.profissao,y.salario)
            i=1
        if i==0:
            print('Não há funcionários cadastrados.')
        r=int(input('Menu inicial(1)\nMenu funcionários(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_funcionario()
    if opcao==2: 
        #localizar pelo codigo
        u=str(input('Digite o codigo:'))
        i=0
        for x in range(len(listafuncionarios)):
            o=listafuncionarios[x]
            if o.codigo==u:
                print(o.nome,o.codigo,o.profissao,o.salario)
                i=1
            
        if i==0:
            print('Funcionário não encontrado.')
        r=int(input('Menu inicial(1)\nMenu funcionários(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_funcionario()
    if opcao==4:
        #excluir funcionários
        u=str(input('Código:'))
        i=0
        for x in range(len(listafuncionarios)):
            j=listafuncionarios[x]
            if j.codigo==u:
                listafuncionarios.remove(j)
                i=1
                break
        if i==0:
            print('Funcionário não encontrado')
        print('Total de funcionários na lista:',len(listafuncionarios))
        r=int(input('Menu inicial(1)\nMenu funcionários(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_funcionario()
    if opcao==5:
        #alterar funcionario
        u=str(input('Código:'))
        for x in range(len(listafuncionarios)):
            k=listafuncionarios[x]
            if k.codigo==u:
                k.nome=str(input('Nome:'))
                k.codigo=str(input('Novo código:'))
                k.editora=str(input('Nova profissão'))
                k.ano=str(input('Novo salário:'))
        r=int(input('Menu inicial(1)\nMenu funcionários(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_funcionario()
    #voltar ao menu inicial
    if opcao==6:
        menu_inicial()



#############################################################################
def menu_disciplina():

    print("Digite a funcionalidade desejada: ")
    print("[1] LISTAR DISCIPLINAS ")
    print("[2] LOCALIZAR DISCIPLINAS PELO CÓDIGO")
    print("[3] ADICIONAR DISCIPLINA")
    print("[4] EXCLUIR DISCIPLINA")
    print("[5] ALTERAR DISCIPLINA")
    print("[6] RETORNAR AO MENU PRINCIPAL")
    opcao = int(input("Opção: "))
    if opcao==3:
        class disciplina:
            #cadastrar disciplina
            def __init__(self):
                print('DISCIPLINAS')
                b=str(input('Nome:'))
                c=str(input('Codigo:'))
                d=str(input('Período:'))
                e=str(input('Nota final:'))
                self.nome=b
                self.codigo=c
                self.periodo=d
                self.nota=e
        a=disciplina()
        #joga disciplina na lista
        listadisciplinas.append(a)
        r=int(input('Menu inicial(1)\nMenu disciplinas(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_disciplina()
    if opcao==1:
        #imprime todas as disciplinas da lista
        i=0
        for x in range(len(listadisciplinas)):
            y=listadisciplinas[x]
            print(y.nome,y.codigo,y.periodo,y.nota)
            i=1
        if i==0:
            print('Não há disciplinas cadastrados.')
        r=int(input('Menu inicial(1)\nMenu disciplinas(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_disciplina()
    if opcao==2: 
        #localizar pelo codigo
        u=str(input('Digite o codigo:'))
        i=0
        for x in range(len(listadisciplinas)):
            o=listadisciplinas[x]
            if o.codigo==u:
                print(o.nome,o.codigo,o.periodo,o.nota)
                i=1
            
        if i==0:
            print('Disciplina não encontrada.')
        r=int(input('Menu inicial(1)\nMenu disciplinas(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_disciplina()
    if opcao==4:
        #excluir disciplinas
        u=str(input('Código:'))
        i=0
        for x in range(len(listadisciplinas)):
            j=listadisciplinas[x]
            if j.codigo==u:
                listadisciplinas.remove(j)
                i=1
                break
        if i==0:
            print('Disciplina não encontrada')
        print('Total de dsiciplinas na lista:',len(listadisciplinas))
        r=int(input('Menu inicial(1)\nMenu funcionários(2)'))
        if r==1:
            menu_inicial()
        if r==2:
            menu_disciplina()
    if opcao==5:
        #alterar disciplina
        u=str(input('Código:'))
        for x in range(len(listadisciplinas)):
            k=listadisciplinas[x]
            if k.codigo==u:
                k.nome=str(input('Novo nome:'))
                k.codigo=str(input('Novo código:'))
                k.editora=str(input('Novo período'))
                k.ano=str(input('Nova nota:'))
        r=int(input('Menu inicial(1)\nMenu disciplinas(2)'))
    
        if r==1:
            menu_inicial()
        
        if r==2:
            menu_disicplina()
    #voltar ao menu inicial
    if opcao==6:
        menu_inicial()



##############################################################################
while True:
    b=menu_inicial()
    if b==1:
       menu_livro()
    if b==2:
       menu_equipamento()    
    if b==3:
       menu_funcionario()
    if b==4:
       menu_disciplina()





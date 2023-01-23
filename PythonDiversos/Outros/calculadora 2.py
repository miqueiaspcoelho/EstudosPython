print('\tCalculadora que é só sucesso, para os cursos de A a Z, até Farmácia.:D\n')
#Operação inicial, dentro do laço para ser refeita caso o usuário queira.
while True:
    a=float(input('Número: '))
    s=str(input('(+)\n(-)\n(*)\n(/)\n'))
    b=float(input('Número: '))
    if s=='+':
        w=a+b
        print(w)
    if s=='-':
        w=a-b
        print(w)
    if s=='*':
        w=a*b
        print(w)
    if s=='/':
        w=a/b
        print(w)
#Retornar para o início ou continuar.    
    e=str(input('Prosseguir?\n')).lower()
    if e=='não':
        u=str(input('Recomeçar?\n')).lower()
        if u=='sim':
            continue
        if u=='não':
            print('O programa será encerrado. Fiquei feliz por ajudar. Volte sempre!!!!')
            quit()
    if e=='sim' or e=='claro':

#Laço que possibilita operações diferentes com resultados que cumulativos.
#Basta usar o incremento da variável.
        while True:
            s=str(input('(+)\n(-)\n(*)\n(/)\n'))
            if s=='+':
                z=float(input('Novo número: '))
                w=w+z
                print(w)
            if s=='-':
                z=float(input('Novo número: '))
                w=w-z
                print(w)
            if s=='*':
                z=float(input('Novo número: '))
                w=w*z
                print(w)
            if s=='/':
                z=float(input('Novo número: '))
                w=w/z
                print(w)
            e=str(input('Continuar?\n')).lower()
            if e=='não' or e=='fechar':
                break
            if e=='sim' or e=='claro':
                continue

    u=str(input('Apagar tudo e ''RECOMEÇAR'' ou ''FINALIZAR'' o programa?\n')).lower()
    if u=='recomeçar':
        continue
    if u=='finalizar' or u=='finalizar':
        quit()
            
        

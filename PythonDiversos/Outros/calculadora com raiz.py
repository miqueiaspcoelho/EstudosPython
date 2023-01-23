print('Pra galerinha que estuda 5 anos pra perguntar: da oi da tim senhor(a)?\n')
#Operação inicial, dentro do laço para ser refeita caso o usuário queira.
while True:
    s=' '
    s=str(input('Raiz quadrada ou outras operações?(raiz/outras)\n')).lower()
    
    if s=='raiz':
        print('Vamos calcular a raiz quadrada de um número!\n')
        while True:
            u=float(input('Número: '))
            p=u**0.5
            
            print((round(p,3)))
            y=str(input('Calcular uma nova raiz?\n'))
            if y=='sim':
                continue
            if y=='não':
                break

    if s=='outras':
        print('Vamos fazer outras operações então')
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
            e=str(input('Deseja prosseguir?(SIM/NÃO).\n')).lower()
            if e=='não':
                break
                
            if e=='sim' or e=='claro':

#Laço que possibilita operações diferentes com resultados cumulativos.
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
                    e=str(input('Continuar?(sim/não)\nSe optar por SIM ele prossegue.\n'
                                    'Se optar por NÃO você pode finalizar ou retornar ao inicio do programa.\n')).lower()
                    if e=='não':
                        u=str(input('Limpar tudo?(sim/não)\nSIm= pedir novos valores.\n'
                                    'NÃO= ENCERRAR TUDO')).lower()
                        if u=='sim':
                            print(w)
                            break
                        if u=='não':
                            print(w)
                            quit()
                    if e=='não' or e=='fechar':
                        break
                    if e=='sim' or e=='claro':
                        continue
    
    u=str(input('Apagar tudo e ''RECOMEÇAR'' ou ''FINALIZAR'' o programa?\n')).lower()
    if u=='recomeçar':
        continue
    if u=='finalizar' or u=='finalizar':
        quit()
                    
                

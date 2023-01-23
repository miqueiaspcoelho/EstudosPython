print('Questão 15, o jogo da velha.\n')

a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9

pontos=0
pontos2=0

print(a,'|',b,'|',c)
print('----------')
print(d,'|',e,'|',f)
print('----------')
print(g,'|',h,'|',i)

muda=1

velha=[]
lista=[1,2,3,4,5,6,7,8,9]

jogadas1=[]
jogadas2=[]

linha1=[1,2,3]
linha2=[1,4,7]
linha3=[1,5,9]
linha4=[4,5,6]
linha5=[7,8,9]
linha6=[2,5,8]
linha7=[3,6,9]
linha8=[3,5,7]

tam=len(lista)

for todos in range(len(lista)):

    if lista==velha:
        print('Deu velha, SOL LÁ MENTOS!!!kkkkk')
        break
    
    if muda==1 and tam>0:
        jogador1=int(input('JOGADOR 1 (O): '))
        if jogador1 in lista:
            if jogador1==1:
                a='O'
            if jogador1==2:
                b='O'
            if jogador1==3:
                c='O'
            if jogador1==4:
                d='O'
            if jogador1==5:
                e='O'
            if jogador1==6:
                f='O'
            if jogador1==7:
                g='O'
            if jogador1==8:
                h='O'
            if jogador1==9:
                i='O'

        if jogador1 not in lista:
            print('\nPosição ocupada(ou não existe), tente novamente.\n')
            print(a,'|',b,'|',c)
            print('----------')
            print(d,'|',e,'|',f)
            print('----------')
            print(g,'|',h,'|',i)
            continue
        
        jogadas1.append(jogador1)
        jogadas1=sorted(jogadas1)
        
        print('\n')
        print(a,'|',b,'|',c)
        print('----------')
        print(d,'|',e,'|',f)
        print('----------')
        print(g,'|',h,'|',i,'\n')

        if 1 in jogadas1:
            todos=jogadas1[0:3]

            if todos==linha1:
                pontos=3
            if todos==linha2:
                pontos=3
            if todos==linha3:
                pontos=3
            
        if 3 in jogadas1:
            todos=jogadas1[0:3]

            if todos==linha1:
                pontos=3
            if todos==linha7:
                pontos=3
            if todos==linha8:
                pontos=3
            
        if 2 in jogadas1:
            todos=jogadas1[0:3]

            if todos==linha1:
                pontos=3
            if todos==linha6:
                pontos=3

        if 4 in jogadas1:
            todos=jogadas1[0:3]
            
            if todos==linha2:
                pontos=3
            if todos==linha4:
                pontos=3
                
        if 5 in jogadas1:
            todos=jogadas1[0:3]
            
            if todos==linha3:
                pontos=3
            if todos==linha4:
                pontos=3
            if todos==linha6:
                pontos=3
            if todos==linha8:
                pontos=3
                
        if 6 in jogadas1:
            todos=jogadas1[0:3]
            
            if todos==linha4:
                pontos=3
            if todos==linha7:
                pontos=3
            
        if 7 in jogadas1:
            todos=jogadas1[0:3]
            
            if todos==linha2:
                pontos=3
            if todos==linha5:
                pontos=3
            if todos==linha8:
                pontos=3
            
        if 8 in jogadas1:
            todos=jogadas1[0:3]
            
            if todos==linha5:
                pontos=3
            if todos==linha6:
                pontos=3
            
        if 9 in jogadas1:
            todos=jogadas1[0:3]
            
            if todos==linha3:
                pontos=3
            if todos==linha5:
                pontos=3
            if todos==linha7:
                pontos=3
        
        lista.remove(jogador1)
        
        tam=len(lista)

        if pontos==3:
            print('JOGADOR 1(O) VENCEU!!! Agora é ao infinito e além.')
            break
        if pontos2==3:
            print('JOGADOR 2(X) VENCEU!!! Show de bola, agora é só sucesso.')
            break
        
        muda-=1
            
    if muda==0 and tam>0:
        jogador2=int(input('JOGADOR 2 (X): '))

        
        if jogador2 in lista:
            if jogador2==1:
                a='X'
            if jogador2==2:
                b='X'
            if jogador2==3:
                c='X'
            if jogador2==4:
                d='X'
            if jogador2==5:
                e='X'
            if jogador2==6:
                f='X'
            if jogador2==7:
                g='X'
            if jogador2==8:
                h='X'
            if jogador2==9:
                i='X'

        if jogador2 not in lista:
            print('\nPosição ocupada(ou não existe), tente novamente.\n')
            print(a,'|',b,'|',c)
            print('----------')
            print(d,'|',e,'|',f)
            print('----------')
            print(g,'|',h,'|',i,'\n')
            continue
        
        jogadas2.append(jogador2)
        jogadas2=sorted(jogadas2)
        
        print('\n')
        print(a,'|',b,'|',c)
        print('------------')
        print(d,'|',e,'|',f)
        print('------------')
        print(g,'|',h,'|',i,'\n')

        if 1 in jogadas2:
            todos=jogadas2[0:3]

            if todos==linha1:
                pontos2=3
            if todos==linha2:
                pontos2=3
            if todos==linha3:
                pontos2=3

        if 3 in jogadas2:
            todos=jogadas2[0:3]

            if todos==linha1:
                pontos2=3
            if todos==linha7:
                pontos2=3
            if todos==linha8:
                pontos2=3
            
        if 2 in jogadas2:
            todos=jogadas2[0:3]
            
            if todos==linha1:
                pontos2=3
            if todos==linha6:
                pontos2=3

        if 4 in jogadas2:
            todos=jogadas2[0:3]
            
            if todos==linha2:
                pontos2=3
            if todos==linha4:
                pontos2=3
                
        if 5 in jogadas2:
            todos=jogadas2[0:3]
            
            if todos==linha3:
                pontos2=3
            if todos==linha4:
                pontos2=3
            if todos==linha6:
                pontos2=3
            if todos==linha8:
                pontos2=3
                
        if 6 in jogadas2:
            todos=jogadas2[0:3]

            if todos==linha4:
                pontos2=3
            if todos==linha7:
                pontos2=3
            
        if 7 in jogadas2:
            todos=jogadas2[0:3]
            
            if todos==linha2:
                pontos2=3
            if todos==linha5:
                pontos2=3
            if todos==linha8:
                pontos2=3
            
        if 8 in jogadas2:
            todos=jogadas2[0:3]
            
            if todos==linha5:
                pontos2=3
            if todos==linha6:
                pontos2=3
            
        if 9 in jogadas2:
            todos=jogadas2[0:3]
            
            if todos==linha3:
                pontos2=3
            if todos==linha5:
                pontos2=3
            if todos==linha7:
                pontos2=3        
        
        lista.remove(jogador2)
        
        tam=len(lista)
        if pontos==3:
            print('JOGADOR 1(O) VENCEU!!! Tu é bom(boa) mesmo.')
            break
        if pontos2==3:
            print('JOGADOR 2(X) VENCEU!!! Mitar é a alma do negócio.')
            break
      
        muda+=1
    
print('Acabou o jogo.')

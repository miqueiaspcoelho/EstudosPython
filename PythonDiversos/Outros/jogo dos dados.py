from random import*

a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]
c=[1,2,3,4,5,6]
d=[1,2,3,4,5,6]

Ca=1000
print('Cada jogada custa 4 reais!!\n')
print('Possíveis valores que podem sair:\n\n'
      '4 | 5 | 6 | 7 | 8 |\n'
      '9 | 10 | 11 | 12 |13\n'
      '14| 15 | 16 | 17 |18\n'
      '19| 20 | 21 | 22 | 23\n'
      '24\n')
aposta=4
saldo=0
cont=0
contg=0
prossiga=0
while prossiga < 1:
    h=''
    while h=='':
        p=int(input('Em qual soma deseja dar seu palpite?\n'))
        if p<4 or p>24:
            print('O valor digitado não consta nas possíveis somas.\n')
            h=''
        else:
            break        
    A=choice(a)
    B=choice(b)
    C=choice(c)
    D=choice(d)
    e=A+B+C+D
    print('A soma sorteada foi:',e,'\n')
    if e==p:
        contg+=1
        print('Ganhou!!!!')
        if e==24 or e==4:
            saldo+=(512-aposta)
            Ca-=512
        if e==23 or e==5 or e==22:
            saldo+=(128-aposta)
            Ca-=128
        if e==6 or e==7:
            saldo+=(32-aposta)
            Ca-+32
        if e==21 or e==20:
            saldo+=(32-aposta)
            Ca-=32
        if e==8:
            saldo+=(32-aposta)
            Ca-=32
        if e==19 or e==9:
            saldo+=(8-aposta)
            Ca-=8
        if e==18 or e==10:
            saldo+=(8-aposta)
            Ca-=8
        if e==11:
            saldo+=(8-aposta)
            Ca-=8
        if e==17 or e==16:
            saldo+=(2-aposta)
            Ca-=2
        if e==12 or e==13:
            saldo+=(2-aposta)
            Ca-=2
        if e==15:
            saldo+=(2-aposta)
            Ca-=2
        if e==14:
            saldo+=(0.5-aposta)
            Ca-=0.5
            
        z=''
        while z=='':
            q1=str(input('Deseja continuar? (s/n) ')).lower()
            if q1=='n':
                z=0
                prossiga=1
                break
            if q1=='s':
                z=0
                prossiga=0
                continue
            else:
                print('Digitou errado, tente novamente!\n')
                z=''
            
                
    else:
        Ca+=4
        saldo-=4
        z=''
        while z=='':
            q=str(input('Deseja continuar? (s/n) ')).lower()
            if q=='n':
                z=0
                prossiga=1
                break
            if q=='s':
                z=0
                prossiga=0
                continue
            else:
                print('Digitou errado, tente novamente!')
                z=''
        
            
    cont+=1
print('\nQuantidade de vezes que a pessoa ganhou=',contg,'\n'
      'Quantidade de vezes jogadas=',cont,'\n'
      'Saldo do jogador=',saldo,'\n'
      'Saldo da banca=',Ca)

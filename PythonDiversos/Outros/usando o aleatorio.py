print('O que estudar com base nos dias da semana')
import random
dia=str(input('Dia da semana(segunda,terça...)\n')).lower()

if dia=='sábado':
    print('Se não tiver prova descanse, faz bem')

if dia=='domingo':
    print('Relaxe, a semana foi muito corrida, vá à Igreja'
          'durma, jogue bola')

if dia!='sábado' and dia!='domingo':    
    dia=random.randint(-1,5)
    if dia==1:
        print('mtm,port,fundamentos')
           
    if dia==2:
        print('quimica,desenho')
           
    if dia==3:
        print('cts,quimica experimental')
           
    if dia==4:
        print('fundamentos, mtm')
           
    if dia==5:
        print('desenho,quimica')
            
    if dia==0:
        print('descansar')
           
    if dia==-1:
        print('descansar')
          


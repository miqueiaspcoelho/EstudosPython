import pyautogui as pt
import pyperclip
from time import sleep
from datetime import datetime


#pega a última mensagem
def UltimaMensagem():
    sleep(3)
    ponteiro = pt.moveTo(500,616, duration=0.5)
    sleep(3)
    pt.tripleClick()
    pt.hotkey('ctrl','c')
    mensagem= pyperclip.paste()
    mensagem=mensagem.lower()
    sleep(3)
    pt.click(500,616)
    pt.typewrite(['esc'])
    if mensagem != '' or mensagem != None:
        return mensagem
    else:
        return 'Esperando resposta do contato'
#checa nova mensagem
def NovaMensagem():
    sleep(3)
    ponteiro=pt.locateOnScreen ('C:/Users/mique/Desktop/botTeste/NovaMensagem.PNG', confidence=0.65)
    if ponteiro !=None:
        print(ponteiro)
        move=pt.moveTo(ponteiro[0],ponteiro[1])
        sleep(3)
        pt.click()
        return 'Nova mensagem'
    else:
        return 'Não há novas mensagens'

    
#checa o horário atual
def Horario():
    hora=datetime.now()
    hora=hora.strftime('%H:%M')
    if hora[0:2] >= '5' and hora[0:2] < '12':
        return 1
    if hora[0:2] >= '12' and hora[0:2] < '18':
        return 2
    if hora[0:2] >= '18' and hora[0:2] <= '23':
        return 3
    else:
        return 0
    return hora

#escreve a mensagem de resposta
def Mensagens(texto):
    nome=''
    if texto != None or texto!='':
        if texto =='#jaquero':
            sleep(3)
            ponteiro = pt.locateOnScreen ('C:/Users/mique/Desktop/botTeste/Referencia.PNG', confidence=0.6)
            sleep(1)
            if ponteiro != None:
                move= pt.moveTo(int(ponteiro[0])+200, ponteiro[1], duration=0.25)
                sleep(1)
                pt.click()
                if Horario()==1:
                    pt.typewrite('Bom dia, sou Valenthina a assistente virtual da Loja da Yas. Seu nome:',interval=0.01)
                    sleep(1)
                    pt.typewrite(['\n'])
                    texto=''
                    while texto=='' or texto==None:
                        texto= UltimaMensagem()
                        sleep(2)
                    nome = texto
                if Horario()==2:
                    pt.typewrite('Boa tarde, sou Valenthina a assistente virtual da Loja da Yas. Seu nome:',interval=0.01)
                    sleep(1)
                    pt.typewrite(['\n'])
                    texto=''
                    while texto=='' or texto==None:
                        texto= UltimaMensagem()
                        sleep(2)
                    nome= texto
                if Horario()==3:
                    pt.typewrite('Boa noite, sou Valenthina a assistente virtual do Brecho da Yas. Seu nome:',interval=0.01)
                    sleep(1)
                    pt.typewrite(['\n'])
                    texto=''
                    while texto=='' or texto==None:
                        texto= UltimaMensagem()
                        sleep(2)
                    nome= texto
                if Horario()==0:
                    pt.typewrite('Boa madrugada. Sou *Valenthina* a assistente virtual do Brecho da Yas. No momento a chefe ta dormindo, retorne amanha :)',
                                 interval=0.01)
                    sleep(1)
                    pt.typewrite(['\n'])
                    exit()
        if texto!='#jaquero':
            ponteiro = pt.locateOnScreen ('C:/Users/mique/Desktop/botTeste/Referencia.PNG', confidence=0.6)
            sleep(1)
            if ponteiro != None:
                move= pt.moveTo(int(ponteiro[0])+200, ponteiro[1], duration=0.25)
                sleep(1)
                pt.click()
                nome=nome.title()
                pt.typewrite(nome+ ' ja comprou na nossa loja antes: (S tecle 0 ou N tecle 1)',interval=0.01)
                sleep(1)
                pt.typewrite(['\n'])
                texto=''
                while texto=='' or texto==None:
                    texto= UltimaMensagem()
                    sleep(2)
                if texto=='0':
                    ponteiro = pt.locateOnScreen ('C:/Users/mique/Desktop/botTeste/Referencia.PNG', confidence=0.6)
                    sleep(1)
                    if ponteiro != None:
                        move= pt.moveTo(int(ponteiro[0])+200, ponteiro[1], duration=0.25)
                        sleep(1)
                        pt.click()
                        pt.typewrite('Vou passar para a chefe, foi um prazer, bye.',interval=0.01)
                        sleep(1)
                        pt.typewrite(['\n'])
                if texto=='1':
                    ponteiro = pt.locateOnScreen ('C:/Users/mique/Desktop/botTeste/Referencia.PNG', confidence=0.6)
                    sleep(1)
                    if ponteiro != None:
                        move= pt.moveTo(int(ponteiro[0])+200, ponteiro[1], duration=0.25)
                        sleep(1)
                        pt.click()
                        pt.typewrite('Vou te dar algumas informações antes de passar para a chefe: ',interval=0.01)
                        pt.typewrite('*infos*, bye.',interval=0.01)
                        sleep(1)
                        pt.typewrite(['\n'])
                    
    else:
        return texto

#ficar continuamente checando novas mensagens
    

#checando onde o mouse está e qual a cor do local
def ChecaMouse():
    while True:
        posXY = pt.position()
        print(posXY,pt.pixel(posXY[0],posXY[1]))
        sleep(3)
        if posXY[0]==0:
            break
#print(UltimaMensagem())
#print(NovaMensagem())
#print(Horario())
print(Mensagens(UltimaMensagem()))
#ChecaMouse()

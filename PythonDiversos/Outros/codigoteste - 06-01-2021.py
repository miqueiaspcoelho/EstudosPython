import pyautogui as pt
import pyperclip
from time import sleep
from datetime import datetime
import keyboard 

class Cliente:
    def __init__(self):
        self.Nome=None
        self.Numero=None

   
#Pega a última mensagem da conversa que estiver aberta no momento.
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
        return 0
    

    
#Checa o horário atual
def Horario():
    hora=datetime.now()
    hora=hora.strftime('%H:%M')
    if hora[0:2] >= '5' and hora[0:2] < '12':
        return [1,'Bom dia']
    if hora[0:2] >= '12' and hora[0:2] < '18':
        return [2,'Boa tarde']
    if hora[0:2] >= '18' and hora[0:2] <= '23':
        return [3,'Boa noite']
    else:
        return [0,'Boa madrugada']

    
#Mensagens
        
    #Mensagem de saudação de acordo com o horário e perguntando o nome do cliente.
def Saudacao(estado):
    if estado[0]==1:
        saudacao=estado[1]+' sou Valenthina a assistente virtual da Loja da Yas. Qual seu nome?'
        return saudacao
    if estado[0]==2:
        saudacao=estado[1]+' sou Valenthina a assistente virtual da Loja da Yas. Qual seu nome?'
        return saudacao
    if estado[0]==3:
        saudacao=estado[1]+' sou Valenthina a assistente virtual da Loja da Yas. Qual seu nome?'
        return saudacao
    if estado[0]==0:
        saudacao=estado[1]+' sou Valenthina a assistente virtual da Loja da Yas. Qual seu nome?'
        return saudacao
    
    #Perguntando se é a primeira ver na loja ou não.
def Pergunta(Nome):
    pergunta=Nome+' já comprou na nossa loja antes?\n*Sim-0*\n*Não-1*'
    return pergunta

    #Passando informações para o cliente, se já comprou-0 passa uma info, se não-1, passa outra info.
def InfoCliente(estado):
    if estado=='0':
        informacoes='Já conhece a loja e nossas formas de pagamento, obrigado por vir novamente.'
        return informacoes
    if estado=='1':
        informacoes='*conta:* 1298391238\n*formas de pagamento:*\ndebito,crédito,boleto,especie.'
        return informacoes

    
#Clicar no whatsweb no campo para responder dentro de uma conversa
def ClickResponde():
    ponteiro = pt.locateOnScreen ('C:/Users/mique/Desktop/botTeste/Referencia.PNG', confidence=0.6)
    if ponteiro != None:
        move= pt.moveTo(int(ponteiro[0])+200, ponteiro[1], duration=0.25)
        sleep(1)
        pt.click()

    else:
        ClickResponde()

    #Envia a mensagem. Colamos a mensagem, que vai ser selecionada e depois apertamos enter.
def Enviar(mensagem):
    pt.hotkey('ctrl','v')
    sleep(1)
    pt.typewrite(['\n'])
    return mensagem

#Checa se chegou uma nova mensagem.
def NovaMensagem():
    sleep(3)
    ponteiro=pt.locateOnScreen ('C:/Users/mique/Desktop/botTeste/NovaMensagem.PNG', confidence=0.65)
    if ponteiro !=None:
        move=pt.moveTo(ponteiro[0],ponteiro[1])
        sleep(3)
        pt.click()
        return 1
    else:
        return 0


#ficar continuamente checando novas mensagens (Lógica do programa).
'''
sleep(3)
lista=[]
ativado=-1
while True:
    Nome=''
    cliente=Cliente()
    posXY = pt.position()
    if posXY[0]==0:
        break
    else:
        a=NovaMensagem()
        if a==1:
            b=UltimaMensagem()
            if b=='#jaquero':
                c=Saudacao(Horario())
                ClickResponde()
                sleep(1)
                pyperclip.copy(c)
                c=pyperclip.paste()
                Enviar(c)
                sleep(1)
                        
                if c!=None:
                    while Nome=='':
                        Nome=UltimaMensagem()
                        Nome=Nome.title()
                        sleep(1)
                    cliente.Nome=Nome
                    lista.append(cliente.Nome)
                    d=Pergunta(Nome)
                    sleep(1)
                    ClickResponde()
                    sleep(1)
                    pyperclip.copy(d)
                    d=pyperclip.paste()
                    Enviar(d)
                    sleep(1)
                    e=''
                    while e=='':
                        e=UltimaMensagem()
                        sleep(1)
                    f=InfoCliente(e)
                    sleep(1)
                    ClickResponde()
                    sleep(1)
                    pyperclip.copy(f)
                    f=pyperclip.paste()
                    Enviar(f)
                    sleep(5)
    
print(lista)
'''
#checando onde o mouse está e qual a cor do local
'''def ChecaMouse():
    while True:
        posXY = pt.position()
        print(posXY,pt.pixel(posXY[0],posXY[1]))
        sleep(3)
        if posXY[0]==0:
            break
'''
#print(UltimaMensagem())
#print(NovaMensagem())
#print(Horario())
#print(Mensagens(UltimaMensagem()))
#ChecaMouse()
        
'''
class teste:
    def __init__(self):
        self.Nome=''
    def ColocaNome(self):
        self.Nome=input(str('Digite um nome:'))
    

i=0
while i<4:
    a=teste()
    b=a.ColocaNome()
    print(b)
    i+=1
'''
ativado=0
while True:
    if keyboard.is_pressed('f2'):
        ativado=1
        print(ativado)
        for x in range(0,12):
            print(x)
            sleep(2)
    if keyboard.is_pressed('f4'):
        ativado=0
        print(ativado)
        for x in range(12,24):
            print(x)
            sleep(2)

import pyautogui as pt
import pyperclip
from time import sleep
from datetime import datetime
import keyboard
import PySimpleGUI as sg

class Cliente:
    def __init__(self):
        self.Nome=None
        self.Numero=None

   
#Pega a última mensagem da conversa que estiver aberta no momento.
def UltimaMensagem():
    sleep(3)###
    ponteiro = pt.moveTo(500,616, duration=0.5)
    sleep(3)###
    pt.tripleClick()
    pt.hotkey('ctrl','c')
    mensagem= pyperclip.paste()
    mensagem=mensagem.lower()
    sleep(3)###
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
        sleep(1)#
        pt.click()

    else:
        ClickResponde()

    #Envia a mensagem. Colamos a mensagem, que vai ser selecionada e depois apertamos enter.
def Enviar(mensagem):
    pt.hotkey('ctrl','v')
    sleep(1)#
    pt.typewrite(['\n'])
    return mensagem

#Checa se chegou uma nova mensagem.
def NovaMensagem():
    sleep(1)#
    ponteiro=pt.locateOnScreen ('C:/Users/mique/Desktop/botTeste/NovaMensagem.PNG', confidence=0.65)
    if ponteiro !=None:
        move=pt.moveTo(ponteiro[0],ponteiro[1])
        sleep(3)###
        pt.click()
        return 1
    else:
        return 0

#Interruptor
ativador=0
def OnOff():
    global ativador
    if keyboard.wait('f2')!= True and ativador==0:
        #keyboard.is_pressed('f2')
        ativador=1
        return ativador
    else:
        ativador=0
        return ativador


#Finaliza o programa se ele já está pausado. Quebra o loop interno.
def Stop():
    posXY= pt.position()
    return posXY[0]

#Mostra pop up na tela com o estado do programa. Se está rodando ou não.
def PopUpEstado(parametro):
    if parametro==1:
        return  sg.popup('Estado do Programa','\tRodando',auto_close= True ,auto_close_duration= 2, no_titlebar= True)
    else:
        return  sg.popup('Estado do Programa','\tPausado',auto_close= True ,auto_close_duration= 2, no_titlebar= True)

#(Lógica do programa).' 
'''
O programa fica checando novas mensagens, se achar ele cria uma fila, ou seja, quem mandar mensagem primeiro
vai ser atendido primeiro. O próximo só é atendido quando o anterior terminar.

---Em breve vou tentar implementar:
1- Função espera (sempre que uma pessoa demorar uma quantidade X de tempo ele finaliza o atendimento devido
a demora e vai para o próximo).

2- Melhorar a função nova mensagem (Descer e subir a página para checar mensagens).

3- Talvez uma função que pega o número e joga em um banco de dados com o nome do cliente.
Usando banco de dados, sqlite.

---Itens implementados:
1- 10-01-2020 -> Pop Up pra exibir o estado do programa para o usuário. Rodando ou Pausado.
2- 09-01-2020 -> Chave OnOff para checar se f2 foi ou não apertado e dependendo da condição ativa ou desativa o programa.
3- 09-01-2020 -> Quebra o loop interno, basta posicionar o cursor todo para a esquerda e esperar 2 segundos
depois é só apertar f2 e o programa é pausado.
'''

lista=[]
while True:
    if OnOff() == 1:
        print('ativado')
        PopUpEstado(1)
        while True:
            Nome=''
            cliente=Cliente()
            sleep(1)#
            
            if Stop()==0:
                break
            
            else:
                
                sleep(1)#
                if Stop()==0:
                    break
                
                sleep(1)#
                a=NovaMensagem()

                sleep(1)#               
                if Stop()==0:
                    break

                sleep(1)#
                if a==1:
                    if Stop()==0:
                        break
                    
                    sleep(1)#
                    b=UltimaMensagem()

                    sleep(1)#
                    if Stop()==0:
                        break

                    sleep(1)#
                    if b=='#jaquero':
                        if Stop()==0:
                            break

                        sleep(1)#
                        c=Saudacao(Horario())

                        sleep(1)#
                        if Stop()==0:
                            break

                        sleep(1)#
                        ClickResponde()

                        sleep(1)#
                        if Stop()==0:
                            break
                        
                        pyperclip.copy(c)
                        c=pyperclip.paste()
                        
                        sleep(1)#
                        if Stop()==0:
                            break
                        
                        Enviar(c)

                        sleep(1)#
                        if Stop()==0:
                            break
                                
                        if c!=None:

                            sleep(1)#
                            if Stop()==0:
                                break
                            
                            while Nome=='':
                                sleep(1)#
                                if Stop()==0:
                                    break
                                
                                Nome=UltimaMensagem()

                                sleep(1)#
                                if Stop()==0:
                                    break
                                
                                Nome=Nome.title()
                                
                            cliente.Nome=Nome
                            lista.append(cliente.Nome)

                            sleep(1)#
                            if Stop()==0:
                                break
                            
                            d=Pergunta(Nome)

                            sleep(1)#
                            if Stop()==0:
                                break
                            
                            ClickResponde()

                            sleep(1)#
                            if Stop()==0:
                                break
                            
                            pyperclip.copy(d)
                            d=pyperclip.paste()

                            sleep(1)#
                            if Stop()==0:
                                break
                            
                            Enviar(d)
                            sleep(1)
                            if Stop()==0:
                                break
                            e=''
                            while e=='':
                                
                                sleep(1)#
                                if Stop()==0:
                                    break
                                
                                e=UltimaMensagem()
                                
                                sleep(1)#
                                if Stop()==0:
                                    break
    
                            f=InfoCliente(e)

                            sleep(1)#
                            if Stop()==0:
                                break
                            
                            ClickResponde()

                            sleep(1)#
                            if Stop()==0:
                                break
                            
                            pyperclip.copy(f)
                            f=pyperclip.paste()

                            
                            Enviar(f)
                            
                            sleep(1)#
                            if Stop()==0:
                                break
                else:
                    pass
                
    else:
        print('pausado')
        PopUpEstado(0)
        sleep(2)#
        
        if Stop()==0:
            print('programa finalizado')
            print(lista)
            sleep(1)#
            exit()
            
        else:
            pass
            


#checando onde o mouse está e qual a cor do local
'''def ChecaMouse():
    while True:
        posXY = pt.position()
        print(posXY,pt.pixel(posXY[0],posXY[1]))
        sleep(3)
        if posXY[0]==0:
            break
'''
#Testes anteriores.
#print(UltimaMensagem())
#print(NovaMensagem())
#print(Horario())
#print(Mensagens(UltimaMensagem()))
#ChecaMouse()
        
'''
#Classe de teste
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
#Testando algumas funções da biblioteca keyboard.

# record all keyboard clicks until esc is clicked
#events = keyboard.record('esc')
# play these events
#keyboard.play(events)
# print all typed strings in the events
#print(list(keyboard.get_typed_strings(events)))
#keyboard.on_release(lambda tecla: print(tecla.name,tecla.scan_code,tecla.time))


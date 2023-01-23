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
esta_topo=0

def NovaMensagem():
    global esta_topo
    sleep(1)#
    if pt.position()[0]==0:
            return -1
        
    ponteiro=pt.locateOnScreen ('C:/Users/mique/Desktop/botTeste/NovaMensagem.PNG', confidence=0.65)
    if ponteiro !=None:
        move=pt.moveTo(ponteiro[0],ponteiro[1])
        sleep(3)###
        pt.click()
        return 1
    else:
        final=None
        while final==None and ponteiro==None:
            ponteiro=pt.locateOnScreen ('C:/Users/mique/Desktop/botTeste/NovaMensagem.PNG', confidence=0.65)
            if ponteiro !=None:
                move=pt.moveTo(ponteiro[0],ponteiro[1])
                sleep(3)###
                if pt.position()[0]==0:
                    return -1
                pt.click()
                esta_topo=0
                return 1
            else:
                pt.scroll(-100)
                final=pt.locateOnScreen ('C:/Users/mique/Desktop/botTeste/Final.PNG', confidence=0.7)
        
        topo=None
        while topo==None and ponteiro==None:
            ponteiro=pt.locateOnScreen ('C:/Users/mique/Desktop/botTeste/NovaMensagem.PNG', confidence=0.65)
            if ponteiro !=None:
                move=pt.moveTo(ponteiro[0],ponteiro[1])
                sleep(3)###
                if pt.position()[0]==0:
                    return -1
                pt.click()
                esta_topo=0
                return 1
            else:
                pt.scroll(100)
                topo=pt.locateOnScreen ('C:/Users/mique/Desktop/botTeste/Topo.PNG', confidence=0.8)
                if topo!= None and esta_topo==0:
                    pt.moveTo(topo[0],topo[1])
                    sleep(3)#
                    if pt.position()[0]==0:
                        return -1
                    pt.click()
                    print('clicou')
                    esta_topo=1
                    
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


#Inatividade:

def ChecaInatividade():
    global temp_inicio
    if abs(int(temp_inicio) - int(datetime.now().strftime('%M'))) >= 2:
        if pt.position()[0]==0:
            return 1
        return 0
    else:
        if pt.position()[0]==0:
            return 1
        #sleep(12)
        return 1



#(Lógica do programa).' 
'''
O programa fica checando novas mensagens, se achar ele cria uma fila, ou seja, quem mandar mensagem primeiro
vai ser atendido primeiro. O próximo só é atendido quando o anterior terminar.

---Em breve vou tentar implementar BACK-END:
1- Ao atender o critério de inatividade, informar ao usuário antes de finalizar o atendimento.
Informar que para reiniciar basta mandar a mensagem de inicio após um certo tempo.

2- Banco de dados com as informações do usuário e dados dos produtos, para fazer um atendimento
completo ao cliente.

3- Talvez uma função que pega o número e joga em um banco de dados com o nome do cliente.
Usando banco de dados, sqlite.

---Itens implementados BACK-END:
1- 10-01-2021 -> Pop Up pra exibir o estado do programa para o usuário. Rodando ou Pausado.
2- 09-01-2021 -> Chave OnOff para checar se f2 foi ou não apertado e dependendo da condição ativa ou desativa o programa.
3- 09-01-2021 -> Quebra o loop interno, basta posicionar o cursor todo para a esquerda e esperar 2 segundos
depois é só apertar f2 e o programa é pausado.
4- 13-01-2021 -> Melhorar a função nova mensagem (Descer e subir a página para checar mensagens).
5- 15-01-2021 -> 1- Inatividade por demora de resposta do cliente. Se demora 2 minutos a responder o atendimento encerra.

---Em breve vou tentar implementar FRONT-END:
---Itens implementados FRONT-END:

'''
'''
lista=[]
retornar_inicio=0
while True: #LAÇO GERAL 1
    
    if OnOff() == 1:
        print('ativado')
        PopUpEstado(1)
        while True:#LAÇO GERAL 2
            retornar_inicio=0
            pt.moveTo(100,200,duration=0.25)
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
                            temp_inicio=datetime.now().strftime('%M')
                            sleep(1)#
                            if Stop()==0:
                                break
                            
                            while Nome=='':
                                sleep(1)#
                                if Stop()==0:
                                    
                                    break
                                
                                Nome=UltimaMensagem()
                                retornar_inicio=1
                                if ChecaInatividade() == 0:
                                    retornar_inicio=0
                                    print(abs(int(temp_inicio) - int(datetime.now().strftime('%M'))))
                                    print('desconectado por inatividade')
                                    break
                                
                                Nome=Nome.title()

                            
                            if retornar_inicio==1:
                                
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
                                
                                sleep(1)#
                                
                                if Stop()==0:
                                    break
                                e=''
                                
                                temp_inicio=datetime.now().strftime('%M')
                                while e=='':
                                    
                                    sleep(1)#
                                    if Stop()==0:
                                        break
                                    
                                    e=UltimaMensagem()
                                    retornar_inicio=1
                                    if ChecaInatividade()== 0:
                                        retornar_inicio=0
                                        print('desconectado por inatividade')
                                        break
                                    
                                    
                                    sleep(1)#
                                    if Stop()==0:
                                        break
                                    
                                if retornar_inicio==1:
        
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
#sleep(2)
#pt.scroll(1000)
#pt.keyDown('pgup')


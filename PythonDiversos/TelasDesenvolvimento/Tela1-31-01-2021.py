import PySimpleGUI as sg

class TELA:
    def __init__(self):
        #layout
        layout=[
            [sg.Text('Estabelecimento:'),sg.Input(key='estabelecimento',size=(40,0))],
            [sg.Text('Nome Assistente:'),sg.Input(key='nome_assistente',size=(40,0))],
            [sg.Text('PIX:'),sg.Input(key='pix',size=(40,0))],
            [sg.Text('Conta Corrente'),sg.Input(key='conta_corrente')]
            [sg.Button('Enviar')],
            [sg.Output(size=(45,10))]
            ]
        
        #janela
        self.janela=sg.Window('Tela teste',layout,finalize=True)
        #self.janela.Maximize()

    def Iniciar(self):
        while True:
            self.button,self.values= self.janela.read()
            estabelecimento=self.values['estabelecimento'].title()
            nome_assistente=self.values['nome_assistente'].title()
            pix=self.values['pix']
            print(f'Estabelecimento: {estabelecimento}')
            print(f'Assistente Virtual: {nome_assistente}')
            print(f'Chave PIX: {pix}')
            tela.janela.FindElement('estabelecimento').Update('')
            tela.janela.FindElement('nome_assistente').Update('')
            tela.janela.FindElement('pix').Update('')
            if event == sg.WIN_CLOSED:
                break
        self.janela.Close()


tela=TELA()
tela.Iniciar()


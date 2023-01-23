import PySimpleGUI as sg

class TELA_PRODUTO:
    def __init__(self):
        #layout
        layout=[
            [sg.Text('Descrição: '),sg.Input(key='descricao_produto',size=(40,0))],
            [sg.Text('Tamanho: '),sg.Input(key='tamanho_produto',size=(3,0)),sg.Text('Preço: '),sg.Input(key='preco_produto',size=(3,0))],
            [sg.Button('Cadastrar')],
            [sg.Output()]
            ]
            
        #janela
        self.janela=sg.Window('CADASTRO DOS PRODUTOS',layout,finalize=True)

    def Iniciar(self):
        while True:
            self.event,self.values = self.janela.read()

            descricao_produto=self.values['descricao_produto']
            tamanho_produto=self.values['tamanho_produto']
            preco_produto=self.values['preco_produto']

            print(f'Descrição: {descricao_produto}')
            print(f'Tamanho: {tamanho_produto}')
            print(f'Preço: {preco_produto}')

            self.janela.FindElement('descricao_produto').Update('')
            self.janela.FindElement('tamanho_produto').Update('')
            self.janela.FindElement('preco_produto').Update('')

            if self.event==sg.WIN_CLOSED:
                break
        self.janela.Close()

tela_produto=TELA_PRODUTO()
tela_produto.Iniciar()

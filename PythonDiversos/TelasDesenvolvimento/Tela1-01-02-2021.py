import PySimpleGUI as sg
import sqlite3 


class TELA_USUARIO:
    def __init__(self):
        #layout
        frame_layout_conta_corrente=[
            [sg.Text('Titular: '),sg.Input(key='nome_titular_corrente')],
            [sg.Text('Agência: '),sg.Input(key='agencia_corrente')],
            [sg.Text('Número da Conta: '),sg.Input(key='n_conta_corrente')],
            ]
        frame_layout_conta_poupanca=[
            [sg.Text('Titular: '),sg.Input(key='nome_titular_poupanca')],
            [sg.Text('Agência: '),sg.Input(key='agencia_poupanca')],
            [sg.Text('Operação: '),sg.Input(key='operacao')],
            [sg.Text('Número da Conta: '),sg.Input(key='n_conta_poupanca')]
            ]
        
        layout=[
            [sg.Text('Estabelecimento:'),sg.Input(key='estabelecimento',size=(40,0))],
            [sg.Text('Nome Assistente:'),sg.Input(key='nome_assistente',size=(40,0))],
            [sg.Text('PIX:'),sg.Input(key='pix',size=(40,0))],
            [sg.Frame('CONTA CORRENTE',frame_layout_conta_corrente)],
            [sg.Frame('CONTA POUPANÇA',frame_layout_conta_poupanca)],
            [sg.Button('CADASTRAR',key='CADASTRAR')],
            [sg.Output(size=(45,10))]
            ]
        
        #janela
        self.janela=sg.Window('INFORMAÇÕES DO USUÁRIO',layout,finalize=True)
        #self.janela.Maximize()

    def Iniciar(self):
        conexcao= sqlite3.connect('teste2.db')
        cursor=conexcao.cursor()
        cursor.execute("""
            select exists (select 1 from Usuario)
            """
            )

        for linha in cursor.fetchall():
            if linha[0]==1:
                self.janela.FindElement('CADASTRAR').Update(disabled=True)

                cursor.execute("""select * from Usuario;""")
                for linha in cursor.fetchall():
                    print(linha)


                cursor.execute("""select * from Conta_Corrente; """)
                for linha in cursor.fetchall():
                    print(linha)

                cursor.execute("""select * from Conta_Poupanca; """)
                for linha in cursor.fetchall():
                    print(linha)
                
                conexcao.close()
        while True:
            self.event,self.values= self.janela.read()
                                     
            estabelecimento=self.values['estabelecimento'].title()
            nome_assistente=self.values['nome_assistente'].title()
            pix=self.values['pix']
            
            nome_titular_corrente=self.values['nome_titular_corrente'].title()
            agencia_corrente=self.values['agencia_corrente']         
            n_conta_corrente=self.values['n_conta_corrente']
                                     
            nome_titular_poupanca=self.values['nome_titular_poupanca'].title()
            agencia_poupanca=self.values['agencia_corrente']
            n_conta_poupanca=self.values['n_conta_corrente']
            operacao=self.values['operacao']
            
            print(f'Estabelecimento: {estabelecimento}')
            print(f'Assistente Virtual: {nome_assistente}')
            
            print(f'Chave PIX: {pix}')
            
            print('\nCONTA CORRENTE')
            print(f'Titular: {nome_titular_corrente}')
            print(f'Agência: {agencia_corrente}')
            print(f'Número da Conta: {n_conta_corrente}')

            print('\nCONTA POUPANÇA')
            print(f'Titular: {nome_titular_poupanca}')
            print(f'Agência: {agencia_poupanca}')
            print(f'Número da Conta: {n_conta_poupanca}')
            print(f'Operação: {operacao}')
                  
            self.janela.FindElement('estabelecimento').Update('')
            self.janela.FindElement('nome_assistente').Update('')
            self.janela.FindElement('pix').Update('')
            self.janela.FindElement('nome_titular_corrente').Update('')
            self.janela.FindElement('agencia_corrente').Update('')
            self.janela.FindElement('n_conta_corrente').Update('')

            self.janela.FindElement('nome_titular_poupanca').Update('')
            self.janela.FindElement('agencia_poupanca').Update('')
            self.janela.FindElement('n_conta_poupanca').Update('')
            self.janela.FindElement('operacao').Update('')

            
            #fechar janela
            if self.event == sg.WIN_CLOSED:
                self.janela.Close()
                break

            #botão cadastrar
            if self.event=='CADASTRAR':
                self.janela.FindElement('CADASTRAR').Update(disabled=True)
                conexcao= sqlite3.connect('teste2.db')
                cursor=conexcao.cursor()
                cursor.execute(
                    """
                    insert into Usuario (Estabelecimento,Nome_Assistente,Pix) values
                    (?,?,?);
                    """, (estabelecimento,nome_assistente,pix)
                    )
                conexcao.commit()

                cursor.execute (
                    """
                    insert into Conta_Corrente (Titular_Corrente,Agencia_Corrente,Numero_Corrente) values
                    (?,?,?);
                    """,(nome_titular_corrente,agencia_corrente,n_conta_corrente)
                    )
                conexcao.commit()

                cursor.execute(
                    """
                    insert into Conta_Poupanca (Titular_Poupanca,Agencia_Poupanca,Numero_Poupanca,Operacao) values
                    (?,?,?,?);
                    """,(nome_titular_poupanca,agencia_poupanca,n_conta_poupanca,operacao)
                    )
                conexcao.commit()
                
                conexcao.close()
                print('Dados cadastrados com Sucesso!!!')
 
                

        


tela_usuario=TELA_USUARIO()
tela_usuario.Iniciar()


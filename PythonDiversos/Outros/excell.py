#BIBLIOTECA PARA TRABALHAR COM EXCEL (XLRD)

#BIBLIOTECA MATH PARA CÁLCULOS

#BIBLIOTECA XLSXWRITER EDITA OU CRIA OU ESCREVE DOCUMENTO DO EXCEL
#NÃO USEI A XLSXWRITER, PORÉM ELA TEM FUNCIONALIDADES LEGAIS, E É SÓ
#COLOCAR O NOME DELA NA INTERNET QUE APARECE TODA A DOCUMENTAÇÃO, É BEM
#LEGAL.

import xlrd
import xlsxwriter
import math as mt

#PRIMEIRA FUNÇÃO. abre o arquivo que desejado
#e pega a folha (sheet)=j e coluna desejada=n.
#função que usa 3 parametros, str e dois int.
#retorna os valores da coluna especificada
def pegaPlanilha(arquivo_xlsx,j,n):
    arquivo=xlrd.open_workbook(arquivo_xlsx,'rb')
    planilha=arquivo.sheet_by_index(j)
    lista_valores_coluna=planilha.col_values(n)
    return lista_valores_coluna

''' parte que ignora valores vazios, parte adicional
    pula todos os valores '' de uma tabela, pra ser usada
    basta colocar dentro do pegaPlanilha, fazendo alguns pequenos
    ajustes.
    for x in lista_valores:
        if x!='':
            print(x)
'''

#SEGUNDA FUNÇÃO. faz o cálculo com os valores
#retornados da função 1.
#o contador do for começa do 1, para excluir o titulo da tabela
def main(lista_valores_coluna):
    F=[]
    L=lista_valores_coluna
    C=float(input('comprimento:'))
    E=float(input('modulo elasticidade:'))
    I=float(input('momento de inercia:'))
    m=1000
    for i in range (1, len(L)):
        f=((L[i]**2)/(2*(mt.pi)*(C**2)))*(((E*I)/m)**0.5)
        F.append(f)
    return F

#a=pegaPlanilha('planilhateste.xlsx',0,2)
#a vai receber tudo que estive na planilha indicada e na coluna indicada
#b=main(a)
#b vai pegar esses valores e calcular a frequencia
#depois é só printar b.
#print(b)


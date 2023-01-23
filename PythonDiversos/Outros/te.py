#bibliotecas
import xlrd
import xlsxwriter
import math as mt

#função para carregar planilha
'''A função tem como parâmetros o nome do arquivo.extensão do arquivo,
nesse caso é xlsx(documento em formato de planilha do excel, a sheet,
ou seja, a folha dentro da planilha e por fim a coluna
'''

def pegaPlanilha(arquivo_xlsx,j,n):
    arquivo=xlrd.open_workbook(arquivo_xlsx,'rb') #carrega o arquivo
    planilha=arquivo.sheet_by_index(j) #carrega a sheet do arquivo
    lista_valores_coluna=planilha.col_values(n) #pega a coluna indicada
    return lista_valores_coluna

#chamamos a função e passamos os parâmetros
#pegaPlanilha('nome-do-arquivo.extensão',nº da folha(sheet), nº coluna)
'''IMPORTANTE: pra organizar é melhor usar uma variável para cada coluna,
se quero pegar a coluna de datas crio uma variável e chamo a função,
se quero pegar a coluna de vazões médias crio uma variável e chamo a função.
Dessa forma o código fica mais organizado e fica melhor trabalhar com os dados
'''
data=pegaPlanilha('Vazoes.xlsx',0,2) #pega coluna datas
aux_data=[]

vazao=pegaPlanilha('Vazoes.xlsx',0,8) #pega coluna vazão média
#substituindo , por / nas datas.
for z in data:
    z=z.replace(',','/')
    aux_data.append(z)

#print pra ver se está tudo ok.
print(aux_data[14::])
#print(vazao[14::])

'''Com os temos entre chaves digo de onde até onde quero pra imprimir
os valores da lista vaz. Neste caso estou pegando de 14 até o final (::),
fiz isso pra excluir o titulo da coluna e as colunas vazias
'''

############################################################################
'''IMPORTANTE: salvar o código e planilha(as) no mesmo diretório
no computador, ou seja, na mesma pasta.
Não usar a extensão .csv pode acontecer erros na função,
salvar em arquivo padrão do excel.
'''

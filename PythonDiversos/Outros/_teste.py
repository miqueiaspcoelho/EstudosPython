#bibliotecas
import xlrd
import xlsxwriter
import math as mt

#função para carregar planilha
def pegaPlanilha(arquivo_xlsx,j,n):
    arquivo=xlrd.open_workbook(arquivo_xlsx,'rb')
    planilha=arquivo.sheet_by_index(j)
    lista_valores_coluna=planilha.col_values(n)
    return lista_valores_coluna

#tamanho de uma coluna na planilha
tam=(len((pegaPlanilha('obitos2.xlsx',0,0))))

#algumas colunas contendo informações do sexo, idade, cidade)
coluna=pegaPlanilha('obitos2.xlsx',0,0)
sexo=pegaPlanilha('obitos2.xlsx',0,0)
age=pegaPlanilha('obitos2.xlsx',0,1)
city=pegaPlanilha('obitos2.xlsx',0,3)

#contando quantos masculino e quantos feminino usando a função nativa count
M=sexo.count('MASCULINO')
F=sexo.count('FEMININO')


#cada individuo é uma tupla de 3 alementos
for x in range(0,tam):
    pessoa=(sexo[x],age[x],city[x])
    print(pessoa)

#alguns dados relevantes, como a quantidade de homens e mulheres e a media
#deles na população geral
print('homens=',M,'=',round((M*100/tam),3),'%',
      '\n','mulheres=',F,'=',round((F*100/tam),3),'%')

#carregando a planilha dos obitos
coluna1=pegaPlanilha('covid19_ma.csv.xlsx',0,4)
L=[]
obitos=[]

#contando as cidades, adicionando em forma de tupla, cidade e casos de morte
#assumindo que cada vez que uma cidade aparece é um óbito.
for x in coluna1:
    if x not in L:
        tupla=(x,coluna1.count(x))
        L.append(x)
        obitos.append(tupla)

#printando os resultados.
for x in obitos:
    print(x)

    
        



    

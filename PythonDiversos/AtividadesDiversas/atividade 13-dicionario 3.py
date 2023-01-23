#3- Escreva um programa que leia uma string do teclado
#e retorne uma tabela com a frequência
#com que cada letra aparece na string.
#Ignore se as letras são maiúsculas ou minúsculas.

palavra=str(input('Digite algo: ')).lower()
palavra.split()
vazio=''
for letras in palavra:
    if letras not in vazio:
        vazio=vazio+letras
dic={}
posi=0
for letras in palavra:
    a=palavra.count(letras)
    if letras not in dic:
        dic[letras]=a


for items in dic:

    print(vazio[posi],' ', dic[items])
    posi+=1
        

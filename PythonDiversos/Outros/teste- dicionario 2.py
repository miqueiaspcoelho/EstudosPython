#2- A seguinte tabela contém tradução de algumas palavras
 #em português para a língua dos piratas
 #Escreva um programa que pede que o usuário
 #digite uma frase em português e imprima a
 #tradução da frase para a língua dos piratas.

dic={'com':'',',':',','.':'.','o':'th\'','banheiro':'head','meu':'me','oi':'avast','é':'be','senhor':'matey','hotel':'fleabag inn','estudante':'swabbie',
     'garoto':'matey',' ':' ','madame':'proud beauty',
     'professor':'foul blaggart','restaurante':'galley','seu':'yer'
     
     ,'licença':'arr','estudantes':'swabbies','são':'be','advogado':'foul blaggart'}

print('\t\tEscreva uma frase com as palavras abaixo: \n\n'
      '\tsenhor, hotel, estudante, garoto, madame\n'
      '\tprofessor, restaurante, seu, com licença\n'
      '\testudantes, são, advogado, o, banheiro\n'
      '\t\t      meu, oi, é.\n\n')

pes=str(input('Vamos traduzir para a lígua dos piratas!!\n ')).lower()
pes=pes.split()
quantidade=len(pes)
posi=0
tradu=''
esp=' '
for todos in range(0,quantidade):
      trad=dic[(pes[posi])]
      tradu=tradu+esp+trad
      posi+=1
tradu=tradu.strip()
print(tradu.capitalize())      

    

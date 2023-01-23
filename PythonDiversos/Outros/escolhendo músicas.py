from random import randrange

print('ESCOLHEDOR DE MÚSICAS\n')

Musicas=['Eu me rendo (2)','Força jovem (2)','Galileu (2)',
'Jesus em tua presença','Efésios 6','Ele vive',
'Porque Ele vive','1000 graus','Eu sou teu',
'Quero conhecer Jesus (2)','Ousado amor','Se eu me humilhar',
'Grandes coisas','Pra sempre','Tudo que eu sou','Eu sou',
'Som da liberdade','Teu Santo Nome','Atos 2',
'Vem com Josué','O nosso general é Cristo','Apaixonado',
'Morada','Ele é exaltado','Hosana',
'Ele chegou','Lugar seguro','Até que Ele venha ',
'Identidade','Colisão','Vai valer a pena',
'Pra valer a pena','Te agradeço 1','Te agradeço 2',
'Sublime','Acredito','Vitória no deserto',
'Somente um Deus assim','Rendição','Vem Senhor Jesus',
'Coração valente','Rendido estou','Me ajude a melhorar', 
'Lindo és','Diante de ti','Oceans ',
'Deus é Deus','Vim para adorar-te','E se',
'Rei Meu','Santo Espírito','Nova criatura', 
'Creio que tu és a cura','Poder pra salvar','Ninguém explica Deus',
'Nada além de ti','Em teus braços','Todas As coisas ',
'Teu amor não falha','Morada','Novo']

Escolhidas=[]
Tocadas=[]
r=int(input('Quantas músicas vai precisar? '))
q=int(input('Quantas músicas foram tocadas? '))
for x in range(0,q):
    t=str(input('Música tocada:')).lower()
    Tocadas.append(t)

e=0
while e==0:
    a=randrange(0,60)
    if Musicas[a].lower() not in Tocadas:
        if Musicas[a].lower() not in Escolhidas:
            Escolhidas.append(Musicas[a].lower())
    if len(Escolhidas)==r:
        e=1
tam=len(Escolhidas)
print('\n Músicas da semana.\n')
for x in range (0,tam):
    print((x+1),'.',Escolhidas[x].title())

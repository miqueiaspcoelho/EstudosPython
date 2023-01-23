# o problema é como ir trocando sem alterar as que foram trocadas anteriormente
# o python tem a função pront str.replace(caractera, caractere que vai substituir)
#acredito que dê para fazer usando ela, mas aqui trouxe de uma forma usando laço de repetição for
# a ideia para resolver o problema é sempre subtituir pela próxima do alfabeto
#para tal precisamos manipular uma variável do tipo texto.

#passo 1- pensar um forma de trabalhar com ela como se cada caractere fosse um elemento único.
#(nos remete à ideia de lista)

#passo 2- evitar que as que foram trocadas anteriormente sejam trocadas novamente.
#para isso vamos precisar de duas variáveis para manipular as strings
# uma para servir de concatenador e a outra para receber elementos e ser concatenada.


#passo 3 - compara cada elemento da nossa string. se tal elemento for igual a 'a' adicione a uma outra variável,
#a que irá ser concatenada, o elemento 'b' e jogue na variável que recebe a concatenação

#passo 4- definir comparações adicionais como: comparar espaços, víruglas, pontuações, para que caso
#sejam colocada na função, permaneçam intactas em nosso valor de saída

#observação- para evitar erros, dentro da função sempre transformamos a entrada em letras minúsculas

def vamola(l):
    l=l.lower()
    lista=[]
    for tudo in range(len(l)):
        lista.append(l[tudo])
    a=''
    c=''
    for tudo in range(len(lista)):
        b=lista[tudo]
        if b==' ':
            c=' '
        if b=='a':
            c='b'
        if b=='b':
            c='c'
        if b=='c':
            c='d'
        if b=='d':
            c='e'
        if b=='e':
            c='f'
        if b=='f':
            c='g'
        if b=='g':
            c='h'
        if b=='h':
            c='i'
        if b=='i':
            c='j'
        if b=='j':
            c='k'
        if b=='k':
            c='l'
        if b=='l':
            c='m'
        if b=='m':
            c='n'
        if b=='n':
            c='o'
        if b=='o':
            c='p'
        if b=='p':
            c='r'
        if b=='q':
            c='r'
        if b=='r':
            c='s'
        if b=='s':
            c='t'
        if b=='t':
            c='u'
        if b=='u':
            c='w'
        if b=='w':
            c='x'
        if b=='x':
            c='y'
        if b=='y':
            c='z'
        if b=='z':
            c='a'
        if b==',':
            c=','
        if b=='!':
            c='!'
        if b=='.':
            c='.'
        if b=='é':
            c='é'
        if b=='í':
            c='í'
        if b=='ã':
            c='ã'
        if b=='ç':
            c='ç'
        if b=='õ':
            c='õ'
        if b=='ê':
            c='ê'
        if b==';':
            c=';'
        a=a+c
    print('Antes\n ',l)
    print('Depois\n',a)
vamola('Deus é bom o tempo todo e o tempo todo e tempo todo, DEUS é bom!!!!!!!!  ')

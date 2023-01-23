#Dada uma lista L de números inteiros, escreva uma
#função retorne uma lista P contendo todos os itens
#de L acrescidos em 10%.

def vamosla(l=[]):
    t=int(input('Quantos elementos deseja colocar na lista?'))
    for a in range (0,t):
        f=int(input('Digite o número:'))
        l.append(f)
        print(l)
    s=[]
    for a in l:
        a=((a*10)/100)+a
        s.append(a)
    print(s)

l=[]
vamosla(l)

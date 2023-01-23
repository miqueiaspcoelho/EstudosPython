dic={'Alano':(7.5,8.0,6.5),'Denise':(9.0,8.5,9.5),'Ana':(3.5,1.0,6.5)}
dic2={}
lista=[]
compara=(7,)

lugar=0
lugarnaposicao=0
pontos=0



for todos in dic:
    recebe=dic[todos]
    lista.append(recebe)
    print(lista)
    
tamanho=len(lista)
print(tamanho)

for tudo in range(0,tamanho):
    posicao=lista[lugar]
    for tudo in len(posicao):
        recebe3=posicao[0]
        if recebe3>=7:
            print('1')
        else:
            print('2')
    
    

    print('posição           lugar')
    print(posicao,' ',lugar)
    lugar+=1

'''
    for tudo in posicao:
            recebe2=posicao[lugarnaposicao]
            print(recebe2,posicao,lugarnaposicao)
            if recebe2>compara:
                pontos+=1
            print(pontos)
            if recebe2>=7:
                    pontos-=1
    
    lugarnaposicao+=1
                       
print(pontos,lugar,lugarnaposicao)


             
           
if pontos==3:
    print('funcionou')
else:
    print('funcionou3')
    
    print(posicao)
    lugar+=1
    
for tudo in range(0,1):
    recebe2=posicao[lugarnaposicao]

    print(recebe2)

if recebe2>=compara:
    print('funcionou')
else:
    print('funcinou 2')

'''    

print('Meus primeiros passos')
while True:
    d=int(input('Distância aqui, em metros: '))
    t=int(input('Tempo aqui, em segundos: '))
    vm= d/t
    print('Esta é a velocidade média do corpo:',vm)

    r=str(input('Deseja um novo cálculo? '))
    if r=='sim':
        continue
    if r=='não':
        break
print('Até a próxima')

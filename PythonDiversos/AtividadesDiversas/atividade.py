'''for a in range (50,151):
    c=(5/9)*(a-32)
    print(a, 'farenheit =', (round(c,2)), 'celsius')
'''
a=int(input('Quantos alunos são?'))
qtm=0
qtf=0
for i in range (0,a):
    s=str(input('Sexo: (m/f) ')).lower()
    idade=int(input('Quantos anos você tem?'))
    idade=idade+idade
    if s== 'm':
        qtm=qtm+1
    if s=='f':
        qtf=qtf+1

    if qtf==0:
        print('não houve pessoas do sexo feminino')
        
    if qtm ==0:
        print('não houve pessoas do sexo masculino')
        
        
    

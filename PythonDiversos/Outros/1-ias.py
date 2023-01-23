#MEMÓRIA TEM 1000 ESPAÇOS, ESCREVER EM BINÁRIO
MEMORIA=['0000100020003000400050006000700080009000','1100220033004400550066007700880099000000','1110222033304440555066607770888099900000',
         '1111222233334444555566667777888899990000']

#listas de teste
lir=[]
libr=[]
lmar=[]
lmbr=[]
#REGISTRADORES
start=-1
pc_count=0
mbr_count=0
PC='0'
MAR=''
MBR=''
IBR=''
IR=''
#FUNÇÃO QUE INICIA  
def inicio (letra):
    letra=letra.lower()
    if letra=='y':
        start=1
        return start
    if letra.lower()=='n':
        exit()
    if letra !='y' or letra != 'n':
        start=0
        return start

#registrador de endereço de memória 12 bits
#pega endereço
def mar ():
    MAR=PC
    return MAR

#registrador de buffer de memória 40 bits
#pega uma palavra ou instrução da memória
def mbr (x):
    if x==0:
        IBR=MBR[20:40]
        return IBR
    if x==1:
        IR=MBR[0:8]
        return IR
    if x==2:
        MAR=MBR[8:20]
        return MAR
    if x==3:
        IR=MBR[20:28]
        return IR
    if x==4:
        MAR=MBR[28:40]
        return MAR
#registrador de buffer de instrução
#pega próxima instrução a ser executada 20 bits
def ibr(y):
    if y==0:
        IR=IBR[0:8]
        return IR
    if y==1:
        MAR=IBR[8:20]
        return MAR

#registrador de instrução opcode 8 bits
#'o que fazer'
def ir():
    return IR

ask=input(str('y-inicia, n-fecha'))
if inicio(ask)==1:
    while pc_count< len(MEMORIA):
        if MBR=='':
            print('MBR VAZIO',)
            MAR=mar()
            MBR=MEMORIA[int(MAR)]

            if IR=='':
                print('1')
                IBR=mbr(0)
                IR=mbr(1)
                MAR=mbr(2)
                print(IR)
                IR=''
                
            if IR!='':
                print('2')
                IR=mbr(3)
                MAR=mbr(4)
                lir.append(IR)
                lmar.append(MAR)
                print(IR)
                IR=''
            
        mbr_count=mbr_count+1


        if MBR!='':
            print('MBR CHEIO')
            print('3')
            
            IR=ibr(0)
            MAR=ibr(1)
            print(IR)
            pc_count=int(PC)+1
            PC=str(pc_count)
            IR=''

        mbr_count=mbr_count+1
            
        if mbr_count==2:
            MBR=''
            mbr_count=0

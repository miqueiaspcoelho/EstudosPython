import numpy as np
#DECIMAL PARA BCD
L=['109']
for x in L:
    c=''
    for y in x:
        c=c+np.binary_repr(int(y),width=4)+'.'
    #print(x,'=',c)

#BCD PARA DECIMAL
L1=['10000000','001000110111','001101000110',
    '010000100001','011101010100','100000000000',
    '100101111000','0001011010000011','1001000000011000',
    '0110011001100111']
L2=[]
for x in L1:
    r=x[::-1]
    L2.append(r)

for x in L2:
    i=0
    soma=0
    b=''
    for y in range(0,len(x)):
        if i<3:
            inteiro=int(x[y])
            soma=soma+inteiro*2**i
            i+=1
        else:
            inteiro=int(x[y])
            soma=soma+inteiro*2**i
            b=str(soma)+b
            soma=0
            i=0
    #print((x[::-1]),'=',b)

L3=['10','13','18','21','25','36',
   '44','57','69','98','125','156']
#for x in L3:
 #   print(x,'=',np.binary_repr(int(x)))


#soma BCD
L1=['010101100001','011100001000']
L2=[]
for x in L1:
    r=x[::-1]
    L2.append(r)

for x in L2:
    i=0
    soma=0
    b=''
    for y in range(0,len(x)):
        if i<3:
            inteiro=int(x[y])
            soma=soma+inteiro*2**i
            i+=1
        else:
            inteiro=int(x[y])
            soma=soma+inteiro*2**i
            b=str(soma)+b
            soma=0
            i=0
    print((x[::-1]),'=',b)

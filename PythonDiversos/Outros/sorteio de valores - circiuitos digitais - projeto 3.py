import random as rd
lista=['0000','0001','0010','0011',
       '0100','0101','0110','0111',
       '1000','1001','1010','1011',
       '1100','1101','1110','1111']

for x in range(0,20):
    print(rd.choice(lista))


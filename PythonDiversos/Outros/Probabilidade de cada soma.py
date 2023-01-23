p4=0
p5=0
p6=0
p7=0
p8=0
p9=0
p10=0
p11=0
p12=0
p13=0
p14=0
p15=0
p16=0
p17=0
p18=0
p19=0
p20=0
p21=0
p22=0
p23=0
p24=0
for x in range(1,7):
    a=x
    for y in range(1,7):
        b=y
        for z in range(1,7):
            c=z
            for t in range(1,7):
                d=t
                print(a,' ',b,' ',c,' ',d)
                s=a+b+c+d
                if s==4:
                    p4+=1
                if s==5:
                    p5+=1
                if s==6:
                    p6+=1
                if s==7:
                    p7+=1
                if s==8:
                    p8+=1
                if s==9:
                    p9+=1
                if s==10:
                    p10+=1
                if s==11:
                    p11+=1
                if s==12:
                    p12+=1
                if s==13:
                    p13+=1
                if s==14:
                    p14+=1
                if s==15:
                    p15+=1
                if s==16:
                    p16+=1
                if s==17:
                    p17+=1
                if s==18:
                    p18+=1
                if s==19:
                    p19+=1
                if s==20:
                    p20+=1
                if s==21:
                    p21+=1
                if s==22:
                    p22+=1
                if s==23:
                    p23+=1
                if s==24:
                    p24+=1
n=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
l=[p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24]
print(l,'\n')
for tudo in range(0,21):
    prob=l[tudo]/1296
    print('Probabilidade da soma ser', n[tudo],'=',prob)

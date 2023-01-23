a=[(1,10),(5,7)]

def chama(l):
    def m (l):
        b=[]
        for item in l:
            b.append(max(item) - min(item))
        L2=sorted(l,key=m)
        print(L2)
chama(a)

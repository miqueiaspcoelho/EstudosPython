x=float(input('Log na base "e" de 1+ (seu numero).\n'))

x=x-1

i=1
log=0
n=0
y=0
for u in range (1,20 +1):
    n=n+1
    y=y+1
    log=(log+(x**n)/y*i)
    i=i*(-1)

print(log)

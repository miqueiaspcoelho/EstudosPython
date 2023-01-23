while True:
    a=int(input('   digite o coeficiente a'))
    if a==0:
        print(' tente novamente')
        continue
    if a!=0:
        break

b=int(input('   digite o coeficiente b'))
c=int(input('    digite o coefiente c'))

D=(b*b)-(4*a*c)
x1=((-b)+(D**0.5))/2*a
x2=((-b)-(D**0.5))/2*a
print (x1,x2)

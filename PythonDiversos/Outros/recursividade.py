def soma(n,b):
    if n==0 and b==0:
        return 1
    if n==0:
        return 0
    if b==0:
        return 1
    if n==1:
        return 1
    else:
        print(n,b,' ',n**b)
        return (soma(n-1,b) + (n**b))
print(soma())



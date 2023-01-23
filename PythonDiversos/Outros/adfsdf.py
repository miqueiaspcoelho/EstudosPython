def soma2(n):
    if n==1:
        return 1
    else:
        return -1 * soma2(n-1) + 1 /n

def soma3(n):
    if n<=3:
        return False
    if n==4:
        return 2*n + 6
    else:
        return soma3(n-1) + n*2
print(soma3(3))

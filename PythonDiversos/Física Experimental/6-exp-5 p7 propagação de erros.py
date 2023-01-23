print('Bola branca(foi lançada somente da posição 1)\n')
lb=[1.28,1.28,1.28]
tb=[0.137908,0.26301,0.408107]
yi=0.12
xi=0.15
sen=0.5
cos=((3**0.5)/2)
v0=[]
tq=sum(tb)/3
acel=[]
for tudo in range(0,3):
    z=xi+lb[tudo]
    vo=(lb[tudo]+xi)/(cos*(tb[tudo]))
    print('vo',vo)
    a=(yi+(vo*sen*(tb[tudo])))/(((tb[tudo])**2)/2)

    deltavo=((1/(cos*(tb[tudo])))**2)*((0.005)**2)
    deltavo1=((z/(cos*((tb[tudo])**2)))**2)*((0.000001)**2)
    deltavo2=(((z/((tb[tudo])*(cos**2)))*sen)**2)*((0.5)**2)
    DVO= (deltavo + deltavo1 + deltavo2)**0.5

    deltag=((2/((tb[tudo])**2))**2)*((0.005)**2)
    deltag1=((sen/((tb[tudo])/2))**2)*((DVO)**2)
    deltag2=(((vo/((tb[tudo])/2))*cos)**2)*((0.5)**2)
    deltag3=((((4*yi)/((tb[tudo])**3))+(((2*vo)*sen)/(tb[tudo])**2))**2)*((0.000001)**2)
    DG= (deltag + deltag1 + deltag2 + deltag3)**0.5
    print('Aceleração de queda=',a,' ','Propagação de erro=',DG,'\n')


    acel.append(a)
    
    v0.append(vo)
m=sum(v0)/3
deltavo=((1/(cos*tq))**2)*((0.005)**2)
deltavo1=((z/(cos*(tq**2)))**2)*((0.000001)**2)
deltavo2=(((z/(tq*(cos**2)))*sen)**2)*((0.5)**2)

DVO= (deltavo + deltavo1 + deltavo2)**0.5


deltag=((2/(tq**2))**2)*((0.005)**2)
deltag1=((sen/(tq/2))**2)*((DVO)**2)
deltag2=(((m/(tq/2))*cos)**2)*((0.5)**2)
deltag3=((((4*yi)/(tq**3))+((2*m*sen)/tq**2))**2)*((0.000001)**2)

DG= (deltag + deltag1 + deltag2 + deltag3)**0.5
print('Propagação de erro tomando uma média das velocidades= '
      'e tempo de queda',DG)

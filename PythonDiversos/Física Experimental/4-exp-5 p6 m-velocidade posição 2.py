yi=0.12
xi=0.15
z=0.15+2.26
sen=0.5
cos=((3**0.5)/2)
v0=[]
lv=[2.26,2.26,2.26]
tv=[1.427087,0.954714,0.932392]
tq=sum(tv)/3
acel=[]
for tudo in range(0,3):

    vo=(lv[tudo]+xi)/(cos*(tv[tudo]))
    a=(yi+(vo*sen*(tv[tudo])))/(((tv[tudo])**2)/2)

    deltavo=((1/(cos*(tv[tudo])))**2)*((0.005)**2)
    deltavo1=((z/(cos*((tv[tudo])**2)))**2)*((0.000001)**2)
    deltavo2=(((z/((tv[tudo])*(cos**2)))*sen)**2)*((0.5)**2)
    DVO= (deltavo + deltavo1 + deltavo2)**0.5

    deltag=((2/((tv[tudo])**2))**2)*((0.005)**2)
    deltag1=((sen/((tv[tudo])/2))**2)*((DVO)**2)
    deltag2=(((vo/((tv[tudo])/2))*cos)**2)*((0.5)**2)
    deltag3=((((4*yi)/((tv[tudo])**3))+(((2*vo)*sen)/(tv[tudo])**2))**2)*((0.000001)**2)
    DG= (deltag + deltag1 + deltag2 + deltag3)**0.5
    print('vo',vo)
    print('Aceleração de queda=',a,' ','Propagação de erro=',DG,'\n')


    acel.append(a)
    
    v0.append(vo)
m=sum(v0)/3
print('Média das velocidades de lançamento da posição 2=',m,'m/s\n')

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





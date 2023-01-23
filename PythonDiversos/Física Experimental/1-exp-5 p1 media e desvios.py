lv=[1.28,1.15,1.15]
mlv=sum(lv)/3
tv=[0.110028,0.388501,0.364801]
mtv=sum(tv)/3

lb=[1.28,1.28,1.28]
mlb=sum(lb)/3
tb=[0.137908,0.26301,0.408107]
mtb=sum(tb)/3

dva=0
dvt=0
dba=0
dbt=0

for tudo in range(0,3):
    a=(lv[tudo]-mlv)**2
    b=(tv[tudo]-mtv)**2
    c=(lb[tudo]-mlb)**2
    d=(tb[tudo]-mtb)**2
    
    dva+=a
    dvt+=b
    dba+=c
    dbt+=d
    
vdesvioa=(dva/3)**0.5
vdesviot=(dvt/3)**0.5
bdesvioa=(dba/3)**0.5
bdesviot=(dbt/3)**0.5


print('Posição 1\n\n'
      'Bola verde\n'
      'Média dos alcances=',mlv,'\n'
      'Média dos tempos=',mtv,'\n'
      'Desvio padrão dos alcances=',dva,'\n'
      'Desvio padrão dos tempos=',dvt,'\n\n'
      'Bola branca\n'
      'Média dos alcances=',mlb,'\n'
      'Média dos tempos=',mtb,'\n'
      'Desvio padrão dos alcances=',dba,'\n'
      'Desvio padrão dos tempos=',dbt,'\n')

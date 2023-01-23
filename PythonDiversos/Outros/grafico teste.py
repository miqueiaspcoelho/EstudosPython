import matplotlib.pyplot as plt
'''
cidades=['Imperatriz','São José de Ribamar',
         'Timon','Caxias','Codó','Paço do Lumiar',
         'Açailândia','Bacabal','Balsas',
         'Barra do Corda','Santa Inês',
         'Pinheiro','Chapadinha','Santa Luzia']
'''
'''
plt.plot([53276.5,89875.5,126474.5,163073.5,199672.5,236271.5,272870.5],[0,7,2,4,0,1,0], color='g',alpha=0.4)
plt.axis([50000,280000,0,7])
plt.ylabel('Habitantes')
plt.title('População')
plt.grid(False)
plt.show()
'''
'''
população=[254569,176418,167619,	
162657,120810,156216,	
111339,103359,94779,
87135,88013,82374,78965,71576]	

plt.hist(população,bins=5,width=20000, color='g',alpha=0.4)
plt.ylabel('Habitantes')
plt.title('População')
plt.grid(False)
plt.show()
'''
'''
população=[254569,176418,167619,	
162657,120810,156216,	
111339,103359,94779,
87135,88013,82374,78965,71576,]


plt.bar([71576,108175,144774,181373,217972],[7,2,4,0,1],color='r',width=10000)
plt.ylabel('Habitantes')
plt.title('População')
plt.grid(False)
plt.show()
'''
'''
população=[254569,176418,167619,	
162657,120810,156216,	
111339,103359,94779,
87135,88013,82374,78965,71576,]	

plt.boxplot(população)
plt.ylabel('Habitantes')
plt.title('População')
plt.grid(True)
plt.show()
'''

'''
veiculos=[140297,33095,43323,
50213,31452,22676,
38228,36615,48452,
26791,30128,21823,
19593,11756]

plt.boxplot(veiculos)
plt.ylabel('Veículos')
plt.title('Total de Veículos')
plt.grid(True)
plt.show()
'''
'''
densidade=[180.79,419.82,89.18,
30.12,27.06,855.84,17.92,
59.43,6.36,15.92,202.76,
51.67,22.59,13.55]

plt.boxplot(densidade)
plt.ylabel('Habitantes / km^2')
plt.title('Densidade Demográfica')
plt.grid(True)
plt.show()
'''
'''
matriculasfundamental=[
40697,23753,27221,28012,
22486,16784,19946,17749,
17083,18374,16830,14320,
15951,14377]

plt.boxplot(matriculasfundamental)
plt.ylabel('Estudantes matriculados')
plt.title('Matrículas no Ensino Fundamental')
plt.grid(True)
plt.show()
'''
'''
matriculasmedio=[
12359,3768,6051,6974,
5361,4171,4963,5068,
4343,4583,5614,4882,
3406,2867]

plt.boxplot(matriculasmedio)
plt.ylabel('Estudantes matriculados')
plt.title('Matrículas no Ensino Médio')
plt.grid(True)
plt.show()
'''
'''
docentesfundamental=[
1761,1007,1344,1619,
1283,717,851,898,
870,1298,934,951,
766,747]

plt.boxplot(docentesfundamental)
plt.ylabel('Docentes')
plt.title('Docentes do Ensino Fundamental')
plt.grid(True)
plt.show()
'''
'''
docentesmedio=[
793,284,576,607,
321,330,310,349,
257,253,278,273,
184,165]

plt.boxplot(docentesmedio)
plt.ylabel('Docentes')
plt.title('Docentes do Ensino Médio')
plt.grid(True)
plt.show()
'''
'''
rendimentopercapita=[
23565.19,9840.73,8153.60,
9027.54,7338.15,6081.98,
18483.99,9928.92,28539.09,
6412.21,13745.37,8378.27,
7143.68,6590.89]

plt.boxplot(rendimentopercapita)
plt.ylabel('Renda per capita média')
plt.title('Rendimento Domiciliar Per Capita')
plt.grid(True)
plt.show()
'''
'''
idh=[
0.731,0.708,0.649,0.624,
0.595,0.724,0.672,0.651,
0.687,0.606,0.674,0.637,
0.601,0.550]

plt.boxplot(idh)
plt.ylabel('IDH')
plt.title('Índice de Desenvolvimento Humano')
plt.grid(True)
plt.show()
'''
'''
trabalhadores=[
60667,19897,13263,15328,
9622,7505,21080,9750,
18152,4920,11867,5385,
5106,3452]

plt.boxplot(trabalhadores)
plt.ylabel('Pessoas')
plt.title('Pessoas em Trabalhos Formais')
plt.grid(True)
plt.show()
'''
'''
rendimentodostrabalhos=[
1874,1686.60,1780.30,1592.90,
1686.60,1592.90,3092.10,1686.60,
1874,1311.80,1686.60,1780.30,
1780.30,2061.40]

plt.boxplot(rendimentodostrabalhos)
plt.ylabel('Reais $')
plt.title('Rendimento médio Aproximado dos Trabalahos Formais')
plt.grid(True)
plt.show()

'''

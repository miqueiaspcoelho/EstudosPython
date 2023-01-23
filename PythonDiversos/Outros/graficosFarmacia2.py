#importando as bibliotecas

import math
import matplotlib.pyplot as plt
import numpy as np

#tpsa (área superfical polar)
tpsa=[40.46,20.23,29.46,53.35,42.35,33.37,33.37,40.46,22.13,
      53.35,29.46,40.46,20.23,29.46,38.70,22.13,33.12,
      53.35,42.35,65.48,40.46]

#logp (coeficiente de partição)
logp=[3.67,4.83,4.21,3.32,3.60,3.90,3.64,3.35,4.83,3.10,3.96,3.88,4.81,3.95,
      3.38,4.96,4.96,3.50,3.49,2.78,3.68]

#atividade biológica.
gpcr=[0.37,0.34,0.29,0.44,0.36,0.32,0.31,0.22,0.30,0.28,0.45,0.23,0.35,0.29,0.36,0.27,0.36,0.29,0.40,0.24,0.34]
gpcr2=[37,34,29,44,36,32,31,22,30,28,45,23,35,29,36,27,36,29,40,24,34]

#interação para aplicação de log nas abscissas.
ltpsa=[]
for x in range(0,21):
    log=math.log(tpsa[x],10)
    ltpsa.append(log)

#gráfico (tpsa X atividade biológica (gpcr)).
plt.plot(ltpsa,gpcr2)
plt.xlabel('Tpsa na forma de log de base 10')
plt.ylabel('GPCR (receptores da proteína G)')
plt.show()

'''
#gráfico de logp (coeficiente de partição) X atividade biológica (gpcr)
plt.plot(logp,gpcr2)
plt.xlabel('Logp (coeficiente de partição)')
plt.ylabel('GPCR (receptores da proteína G')
plt.show()
'''
'''
#gráfico logp (coeficiente de partição ) X tpsa (área superficial polar)
plt.plot(logp,ltpsa)
plt.xlabel('Log de P (coeficiente de partição')
plt.ylabel('Tpsa na forma de log de base 10')
plt.show()
'''

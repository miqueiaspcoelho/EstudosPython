import numpy as np
import matplotlib.pyplot as plt
import math
import scipy as sc
from scipy import stats

#normalizar as variáveis
RT=[1.169,1.168,1.165,1.177,1.166,1.179,1.171,1.169,
1.177,1.172,1.168,1.162,1.165,1.168,1.163,1.170	,1.168,
1.170,1.167,1.172,1.166,1.168,1.162,1.171,1.170,
1.169,1.167,1.168,1.171,1.164,1.163,1.167,1.162,
1.166,1.163,1.170,1.168,1.166,1.167,1.166,1.178,
1.169,1.172,1.165,1.172,1.175,1.174,1.173,1.169	,1.170]


media=round((sum(RT)/50),3)
print('media',media)
desvp=0.00412
pi=math.pi
gaussiana=[]
e=math.e
for x in range(0,50):
    z=round(((e**(-(RT[x]-media)**2)/2*(desvp**2))/(((desvp**2)*2*pi)**0.5)),6)
    gaussiana.append(z)
print(gaussiana)
plt.plot(gaussiana)
plt.show()



'''

RT=[1.169,1.168,1.165,1.177,1.166,1.179,1.171,1.169,
1.177,1.172,1.168,1.162,1.165,1.168,1.163,1.170,1.168,
1.170,1.167,1.172,1.166,1.168,1.162,1.171,1.170,
1.169,1.167,1.168,1.171,1.164,1.163,1.167,1.162,
1.166,1.163,1.170,1.168,1.166,1.167,1.166,1.178,
1.169,1.172,1.165,1.172,1.175,1.174,1.173,1.169,1.170]


plt.hist(RT,bins=6,color='green',alpha=0.5,label='Probabilidade')


plt.rcParams['figure.figsize'] = (11,7)
plt.xlabel('Resistências')
plt.ylabel('Quantidade de resistores')
plt.title('Histograma')
plt.legend(loc='best')

d=0.00412
gauss=[]
m=1.169
pi=math.pi
e=math.e
l=[]
z=[]



for x in range(0,50):
    g=abs((RT[x]- m)/d)
    g=round(g,3)
    z.append(g)

mu=1.169
sigma = 0.00412
s = np.random.normal(mu, sigma,50)


# Create the bins and histogram
count, bins, ignored = plt.hist(s, 7,alpha=0.1, density=True)

# Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ),       linewidth=3, color='b')

plt.show()
'''

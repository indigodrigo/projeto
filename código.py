import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp


#gera os valores das distribuições normal e lognormal
    normal = sp.norm.rvs(size=30)
lognormal = sp.lognorm.rvs(1,size=50)

#NORMAL
#encontra os pontos das CDFs empírica e teórica com maior distância vertical
x1 = np.sort(normal)
y1 = np.arange(0, len(x1)) / len(x1)
a=sp.norm.cdf(x1)
distance1=abs(y1-a)
for i, value in enumerate(distance1):
    if value == max(distance1):
        nx = x1[i]
        ny1 = a[i]
        ny2 = y1[i] 
        

#plota o grafico anterior, mas com uma reta ligando os pontos com maior distância vertical
plt.figure(figsize=(6, 6))
plt.scatter(x1, y1, color='k', s=10)
plt.plot(np.arange(-3,3,0.1),sp.norm.cdf(np.arange(-3,3,0.1)), color='r')
plt.plot((nx, nx), (ny1, ny2), 'm-', linewidth=1.3)
plt.show



#LOGNORMAL
#encontra os pontos das CDFs empírica e teórica com maior distância vertical
x2 = np.sort(lognormal)
y2 = np.arange(0, len(x2)) / len(x2)
b=sp.lognorm.cdf(x2, 1)
distance2=abs(y2-b)
for i, value in enumerate(distance2):
    if value == max(distance2):
        lx = x2[i]
        ly1 = b[i]
        ly2 = y2[i]
        
#plota o grafico anterior, mas com uma reta ligando os pontos com maior distância vertical
plt.figure(figsize=(6, 6))    
plt.scatter(x2, y2, color='k', s=10)
plt.plot(np.arange(0,max(lognormal),0.1),sp.lognorm.cdf(np.arange(0,max(lognormal),0.1), 1), color='r')
plt.plot((lx, lx), (ly1, ly2), 'm-', linewidth=1.3)
plt.show

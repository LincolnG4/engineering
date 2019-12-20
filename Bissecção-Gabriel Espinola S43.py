# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 18:49:44 2017

@author: Gabriel Espinola
"""
import matplotlib.pyplot as plt

  
def f(x):
    return -1 + x**10

Imax=50
xu = 1.3
xl = 0
es = 0.0000000000005
c = []
j = []
r = []
t = [] 

for i in range (1,Imax):
    xr=(xu+xl)/2
    j.append(i)
    
    if f(xr)==0:
        exit
    elif f(xu)*f(xr)<0:
        xl=xr
    else:
        xu=xr
    r.append(xr)  
    t.append(f(xr))
    e=abs((xr-xu)/xr)
    c.append(e)
    if e<abs(es):
        exit
        
print('\n Grafico i x Erro')
plt.plot(j,c,label='Bissecção')
plt.show()

print ('\n Grafico i x Valor Raiz')
plt.plot(j,r, label = 'bissecção')
plt.legend()
plt.show()

print ('\n Grafico i x Valor F(Raiz)')
plt.plot(j,t, label = 'bissecção')
plt.legend()
plt.show()

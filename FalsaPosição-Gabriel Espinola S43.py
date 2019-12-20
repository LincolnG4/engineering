# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 18:49:44 2017

@author: Gabriel Espinola
"""



def f(x):
    return -1 + x**10

Imax=50
xu = 1.3
xo = 0
es = 0.0000000000005
c = []
j = []
t = []
r = []

for i in range (1,Imax):
    xr=xo-(f(xo)*(xo-xu))/(f(xo)-f(xu))
    j.append(i)
    if f(xr)==0:
        exit
    elif f(xu)*f(xr)<0:
        xo=xr
    else:
        xu=xr
        

    e=abs((xr-xu)/xr)
    c.append(e)
    r.append(xr)
    t.append(f(xr))
    if e<abs(es):
        exit

print('\n Grafico i x Erro')
plt.plot(j,c,label='Falsa Posição')
plt.show()

print ('\n Grafico i x Valor Raiz')
plt.plot(j,r, label = 'Falsa Posição')
plt.legend()
plt.show()

print ('\n Grafico i x Valor F(Raiz)')
plt.plot(j,t, label = 'Falsa Posição')
plt.legend()
plt.show()
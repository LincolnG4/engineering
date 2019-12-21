# -*- coding: utf-8 -*-
"""
Created on Mon Aug  21 17:44:40 2017

@author: Gabriel Espinola
"""
import matplotlib.pyplot as plt

def funcao (x):
    return x**10 - 1


xl = 0
xu = 1.3
es = 0.0000000005
xi = 1.3
xi2 = 0.8


c=[]
r=[]
j=[]
t=[]

def sec (xi,xi2,es):
    for i in range (0,200):
        j.append(i)
        if i==0:
            e=1
            c.append(e)
            t.append(funcao(xi2))
            r.append(xi2)
        if i==1:
            e=float (xi-xi2)/(xi)
            c.append(e)
            r.append(xi)
            t.append(funcao(xi))
        if i>1:
            xt=r[i-1]-float(((funcao(r[i-1]))*(r[i-2]-r[i-1]))/(funcao(r[i-2])-funcao(r[i-1])))
            r.append(xt)
            t.append(funcao(xt))
            e=abs(float((xt-r[i-1])/xt))
            c.append(e)
            if funcao(xt)==0:
                print ('\nQuantidade de iterações (secante): %d' % (i))
                print ('Erro final (secante): %f' % (c[i-1] ))
                return xt
                exit
            if e<abs(es):
                print ('\nQuantidade de iterações (secante): %d' % (i))
                print ('Erro final (secante): %f' % (c[i-1] ))
                return xt
                exit
            if i == 199:
                print ('\nQuantidade de iterações (secante): %d' % (i))
                print ('Erro final (secante): %f' % (c[i-1] ))
                return xt
                exit
                
xraiz=sec(xi2,xi,es)

print('\n Grafico i x Erro')
plt.plot(j,c,label='Secante')
plt.show()

print ('\n Grafico i x Valor Raiz')
plt.plot(j,r, label = 'Secante')
plt.legend()
plt.show()

print ('\n Grafico i x Valor F(Raiz)')
plt.plot(j,t, label = 'Secante')
plt.legend()
plt.show()
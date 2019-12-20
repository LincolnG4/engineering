# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:50:41 2017

@author: Gabriel Espinola
"""

Imax=50
x0=1.3
raizes = []
e=[]
fx=[]
es=0.0000000005
c = []
j = []
xo=1.3


def newton(xo,es):
    for i in range (0,Imax):
     
        j.append(i)
        if i==0:
            e=1
            c.append(e)
            fx.append(f(x0))
            raizes.append(x0)
        else :
            x2=raizes[i-1]-float((f(raizes[i-1]))/(f1(raizes[i-1])))
            raizes.append(x2)
            fx.append(f(x2))
 
            e=abs(float((x2-raizes[i-1])/x2))
                
            c.append(e)
            exit 
            if f(x2)==0:
                return x2
                exit
            if e<abs(es):
                return x2
                exit
xraiz=newton(xo,es)       

print('Raiz: %f' % xraiz)

print('\n Grafico i x Erro')
plt.plot(j,c,label='Newton')
plt.show()

print ('\n Grafico i x Valor Raiz')
plt.plot(j,raizes,label = 'Newton')
plt.legend()
plt.show()

print ('\n Grafico i x Valor F(Raiz)')
plt.plot(j,fx,label = 'Newton')
plt.legend()
plt.show()




# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 23:11:06 2017

@author: Gabriel Espinola
"""
#Bissecção#

def f(x):
    return -1 + x**10

Imax=50
xu = 1.3
xl = 0
es = 0.00000000005
c = []
j = []
for i in range (1,Imax):
    xr=(xu+xl)/2
    j.append(i)
    if f(xr)==0:
        exit
    elif f(xu)*f(xr)<0:
        xl=xr
    else:
        xu=xr

    e=abs((xr-xu)/xr)
    c.append(e)
    if e<abs(es):
        exit
plt.plot(j,c)

#Falso Posição#


def f(x):
    return -1 + x**10

Imax=50
xu = 1.3
xo = 0
es = 0.1
c = []
j = []

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
    if e<abs(es):
        exit
plt.plot(j,c)

#Newton#
  
def f(x):
    return -1 + x**10

def f2(x):
        return  10*x**9
    

Imax=10
xo = 1.3
es = 0.0000005
c = []
j = []

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


plt.plot(j,c)


#Secante#

import matplotlib.pyplot as plt
def f(x):
        return -1 + x**10
    
Imax=10
xu=1.3
xo=xu-1
es=0.1
c = []
j = []
for i in range (0,Imax):
        x2= xu - (f(xu)*(xo-xu))/(f(xo)-f(xu))  
        j.append(i)
        if f(x2)==0:
            exit
        elif f(xo)*f(x2)<0:
            xu=x2
        else:
            xo=x2
        
        e=abs ((x2-xu)/x2)
        c.append(e)
        if e<abs(es):
            exit

plt.plot(j,c)

####

plt.plot(iteracoes,erros, label='Bissecção')
plt.plot(iteracoes2,erros2, label='Falsa posição')
plt.plot(iteracoes3,erros3, label='Newton')
plt.plot(iteracoes4,erros4, label='Secante')
plt.xlabel('Número de Iterações')
plt.ylabel('Erros(%)')
plt.title('Comparativo de erros(%), Falsa posição x Bissecção x Newton x Secante ')
plt.legend()
plt.show()

plt.plot(iteracoes,raizes, label='Bissecção')
plt.plot(iteracoes2,raizes2, label='Falsa posição')
plt.plot(iteracoes3,raizes3, label='Newton')
plt.plot(iteracoes4,raizes4, label='Secante')
plt.xlabel('Número de Iterações')
plt.ylabel('valor da raiz')
plt.title('Comparativo dos valores de raizes, Falsa posição x Bissecção x Newton x Secante ')
plt.legend()
plt.show()

plt.plot(iteracoes,f_raiz, label='Bissecção')
plt.plot(iteracoes2,f_raiz2, label='Falsa posição')
plt.plot(iteracoes3,f_raiz3, label='Newton')
plt.plot(iteracoes4,f_raiz4, label='Secante')
plt.xlabel('Número de Iterações')
plt.ylabel('f(raiz)')
plt.title('Comparativo de f(raiz), Falsa posição x Bissecção x Newton ')
plt.legend()
plt.show()

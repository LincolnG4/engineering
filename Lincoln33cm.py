" Método da Bissecção " 
"  Gabriel Espinola - S43 - Eng. Mecânica "

import matplotlib.pyplot as plt
import math
import pylab 
  
def f(x):
    return -1 + x**10

Imax=50
xu = 1.3
xo = 0
es = 0.00000000000005
c = []
j = []

for i in range (2,Imax):
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

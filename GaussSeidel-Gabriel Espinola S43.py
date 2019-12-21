# -*- coding: utf-8 -*-
"""
Created on Mon Aug  21 17:44:40 2017

@author: Gabriel Espinola
"""
import matplotlib.pyplot as plt

def GaussSeidel (A[][],B[],X[]):
    for

    return x**10 - 1


x = 0
xu = 1.3
es = 0.0000000005
xi = 1.3
xi2 = 0.8


c=[]
r=[]
j=[]
t=[]

def GaussSeidel (A[],B[],X[]):
    for i in range (1,len(B)-1):
        for j in range (i+1,len(B)):
            for k in range (i,len(X)):
                A[j][k]=((A[i][k]*A[j][i])/(A[i][i]))+(A[j][k])
            B[j]=(B[j]+((B[i]*A[j][i])/(A[i][i]))


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
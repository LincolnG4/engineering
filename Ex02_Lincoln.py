# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:08:20 2017

@author: Gabriel Espinola
"""

import numpy as np
import matplotlib.pyplot as plt

S = 3
C = S
emin = float(input("Erro: "))
imax = int(input("Numero de iteracoes: "))
A = [[0 for i in range (S)]for i in range (C)]
b = [0 for i in range (S)]
x = [0 for i in range (C)]
x1s = []
x2s = []
x3s = []
x1j = []
x2j = []
x3j = []
iteracao=[]

for j in range (C):
    solin = float(input('Solucao inicial para x[%d] = ' % (j+1)))
    x[j] = solin

def refresh (A,x,b):
    A[0][0]=3.0
    A[0][1]=-0.1
    A[0][2]=-0.2
    A[1][0]=0.1
    A[1][1]=7.0
    A[1][2]=-0.3
    A[2][0]=0.3
    A[2][1]=-0.2
    A[2][2]=10
    b[0]=7.85
    b[1]=-19.3
    b[2]=71.4
    x[0]=0
    x[1]=0
    x[2]=0

    
def SEIDELOIRO (A,b,x,emin,imax):
    start = timer()
    refresh(A,x,b)
    print ("Metodo Gauss-Seidel")
    xold = [0 for t in range (C)]
    e = [0 for i in range (C)]
    for k in range (imax):    
        for i in range (S):
            xold[i] = x[i]
            soma = b[i]
            for j in range (0,C):
                if (i!=j):
                    soma = soma - A[i][j]*x[j]
            x[i] = soma/A[i][i]
            if(i==0):
                x1s.append(x[i])
            elif(i==1):
                x2s.append(x[i])
            else:
                x3s.append(x[i])
            e[i] = abs((x[i]-xold[i])/x[i])
        if(max(e)<emin):
            print('Iteracoes realizadas: %d' % k)
            #print('Erro maximo: %f' % (max(e)))
            for i in range (C):
                print('Valor de x['+ str (i+1) +'] = %f' %(x[i]))
            break
    if(k==(imax-1)):
        print("Erro aproximado eh maior que Emin")
        #print('Erro maximo: %f' % (max(e)))
        for i in range (C):
            print('Valor de x['+ str (i+1) +'] = %f' %(x[i]))
    end = timer()-start
    print("Tempo de execução: %.6f"%end)
        
def JACOBLOIRO (A,b,x,emin,imax):
    start = timer()
    refresh(A,x,b)
    print ("Metodo Gauss-Jacobi")
    xold = [0 for t in range (C)]
    e = [0 for i in range (C)]
    for k in range (imax):    
        for i in range (S):
            xold[i] = x[i]
            soma = b[i]
            for j in range (0,C):
                if (i!=j):
                    soma = soma - A[i][j]*xold[j]
            x[i] = soma/A[i][i]
            if(i==0):
                x1j.append(x[i])
            elif(i==1):
                x2j.append(x[i])
            else:
                x3j.append(x[i])
            e[i] = abs((x[i]-xold[i])/x[i])
        if(max(e)<emin):
            print('Iteracoes realizadas: %d' % k)
            #print('Erro maximo: %f' % (max(e)))
            for i in range (C):
                print('Valor de x['+ str (i+1) +'] = %f' %(x[i]))
            break
    if(k==(imax-1)):
        print("Erro aproximado eh maior que Emin")
        #print('Erro maximo: %f' % (max(e)))
        for i in range (C):
            print('Valor de x['+ str (i+1) +'] = %f' %(x[i]))
    end = timer()-start
    print("Tempo de execução: %.6f"%end)

def CALOURO (A,x,b):
    start = timer()
    refresh(A,x,b)
    print("Metodo Gauss-Ingenuo")
    print("Matriz Original")
    print(A[0])
    print(A[1])
    print(A[2])
    for i in range (C):
        for j in range (i+1,C):
            fator = A[j][i]/A[i][i]
            b[j] = b[j] - b[i]*fator
            for k in range (i,C):
                A[j][k] = A[j][k] - A[i][k]*fator                  
    #print("Matriz Escalonada")
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print("Resultados atualizados")
    #print(b)
    x[S-1]=b[S-1]/A[S-1][S-1]
    for i in range (C-2,-1,-1):
        soma = b[i]
        for j in range (C):
            soma = soma - A[i][j]*x[j]
        x[i] = soma/A[i][i]
    print("Solucao")
    for i in range (C):
        print('Valor de x['+ str (i+1) +'] = %f' %(x[i]))
    end = timer()-start
    print("Tempo de execução: %.6f"%end)
    
def MICHAEL (A,x,b):
    start = timer()
    refresh(A,x,b)
    print ("Metodo Gauss-Jordan")
    for i in range (C):
        for j in range (i+1,C):
            if(i!=j):
                fator = A[j][i]/A[i][i]
                b[j] = b[j] - b[i]*fator
                for k in range (i,C):
                    A[j][k] = A[j][k] - A[i][k]*fator
    for i in range(C-1,0,-1):
        for j in range(i-1, -1,-1):  
            fator = A[j][i]/A[i][i]
            b[j] = b[j] - b[i]*fator
            for k in range(C-1,0,-1):
                A[j][k] = A[j][k] - A[i][k]*fator
    for i in range(C-1, -1, -1): 
        if(A[i][i]!=0):
            b[i]=(b[i])/A[i][i]
            A[i][i]= A[i][i] /A[i][i]
    for i in range(C-1, -1, -1):   
        x[i]=b[i]
    print("Solucao")
    for i in range (C):
        print('Valor de x['+ str (i+1) +'] = %f' %(x[i]))
    end = timer()-start
    print("Tempo de execução: %.6f"%end)
    
SEIDELOIRO(A,b,x,emin,imax)
JACOBLOIRO(A,b,x,emin,imax)

xx, yy = np.meshgrid(range(1,5),range(-3,-1))
z1 = (-A[0][0] * xx - A[0][1] * yy + b[0]) * 1. / A[0][2]
z2 = (-A[1][0] * xx - A[1][1] * yy + b[1]) * 1. / A[1][2]
z3 = (-A[2][0] * xx - A[2][1] * yy + b[2]) * 1. / A[2][2]

plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx, yy, z1, alpha=0.2)
plt3d.plot_surface(xx, yy, z2, alpha=0.2)
plt3d.plot_surface(xx, yy, z3, alpha=0.2)
ax = plt.gca()
ax.scatter(x1s, x2s, x3s, color='blue')
ax.scatter(x1j, x2j, x3j, color='red')
plt.show()

CALOURO(A,x,b)
MICHAEL(A,x,b)
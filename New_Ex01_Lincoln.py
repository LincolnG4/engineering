# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:15:30 2017

@author: Gabriel Espinola
"""
import matplotlib.pyplot as plt
from timeit import default_timer as timer # tempo de execucao
from copy import deepcopy # impedir problema com referencias
import numpy as np


l = 2
c = l
emin = float(input("Erro: "))
imax = int(input("Numero de iteracoes: "))
A = [[0 for i in range (l)]for i in range (c)]
b = [0 for i in range (l)]
x = [0 for i in range (c)]
x1s = []
x2s = []
x1j = []
x2j = []
iteracao=[]

for j in range (c):
    solin = float(input('Solucao inicial para x[%d] = ' % (j+1)))
    x[j] = solin


def refresh (A,x,b):
    A[0][0]=3.0
    A[0][1]=2
    A[1][0]=-1
    A[1][1]=2
    b[0]=18
    b[1]=2
    x[0]=0
    x[1]=0
   
def SEIDEL (A,b,x,emin,imax):
    refresh(A,x,b)
    start = timer()
    print ("Metodo Gauss-Seidel")
    xold = [0 for t in range (c)]
    e = [0 for i in range (c)]
    for k in range (imax):    
        for i in range (l):
            xold[i] = x[i]
            soma = b[i]
            for j in range (0,c):
                if (i!=j):
                    soma = soma - A[i][j]*x[j]
            x[i] = soma/A[i][i]
            if(i==0):
                x1s.append(x[i])
            else:
                x2s.append(x[i])
            e[i] = abs((x[i]-xold[i])/x[i])
        if(max(e)<emin):
            print('Iteracoes realizadas: %d' % k)
            #print('Erro maximo: %f' % (max(e)))
            for i in range (c):
                print('Valor de x['+ str (i+1) +'] = %f' %(x[i]))
            break
    if(k==(imax-1)):
        print("Erro aproximado eh maior que Emin")
        #print('Erro maximo: %f' % (max(e)))
        for i in range (c):
            print('Valor de x['+ str (i+1) +'] = %f' %(x[i]))
    end = timer()-start
    print("Tempo de execução: %.6f"%end)
            
def JACOBI (A,b,x,emin,imax):
    start = timer()
    refresh(A,x,b)
    print ("Metodo Gauss-Jacobi")
    xold = [0 for t in range (c)]
    e = [0 for i in range (c)]
    for k in range (imax):    
        for i in range (l):
            xold[i] = x[i]
            soma = b[i]
            for j in range (0,c):
                if (i!=j):
                    soma = soma - A[i][j]*xold[j]
            x[i] = soma/A[i][i]
            if(i==0):
                x1j.append(x[i])
            else:
                x2j.append(x[i])
            e[i] = abs((x[i]-xold[i])/x[i])
        if(max(e)<emin):
            print('Iteracoes realizadas: %d' % k)
            #print('Erro maximo: %f' % (max(e)))
            for i in range (c):
                print('Valor de x['+ str (i+1) +'] = %f' %(x[i]))
            break
    if(k==(imax-1)):
        print("Erro aproximado eh maior que Emin")
        #print('Erro maximo: %f' % (max(e)))
        for i in range (c):
            print('Valor de x['+ str (i+1) +'] = %f' %(x[i]))
    end = timer()-start
    print("Tempo de execução: %.6f"%end)

def INGENUO (A,x,b):
    start = timer()
    refresh(A,x,b)
    print("Metodo Gauss-Ingenuo")
    print("Matriz Original")
    print(A[0])
    print(A[1])
    for i in range (c):
        for j in range (i+1,c):
            fator = A[j][i]/A[i][i]
            b[j] = b[j] - b[i]*fator
            for k in range (i,c):
                A[j][k] = A[j][k] - A[i][k]*fator                  
    #print("Matriz Escalonada")
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print("Resultados atualizados")
    #print(b)
    x[l-1]=b[l-1]/A[l-1][l-1]
    for i in range (c-2,-1,-1):
        soma = b[i]
        for j in range (c):
            soma = soma - A[i][j]*x[j]
        x[i] = soma/A[i][i]
    print("Solucao")
    for i in range (c):
        print('Valor de x['+ str (i+1) +'] = %f' %(x[i]))
    end = timer()-start
    print("Tempo de execução: %.6f"%end)
    
def JORDAN (A,x,b):
    start = timer()
    refresh(A,x,b)
    print ("Metodo Gauss-Jordan")
    for i in range (c):
        for j in range (i+1,c):
            if(i!=j):
                fator = A[j][i]/A[i][i]
                b[j] = b[j] - b[i]*fator
                for k in range (i,c):
                    A[j][k] = A[j][k] - A[i][k]*fator
    for i in range(c-1,0,-1):
        for j in range(i-1, -1,-1):  
            fator = A[j][i]/A[i][i]
            b[j] = b[j] - b[i]*fator
            for k in range(c-1,0,-1):
                A[j][k] = A[j][k] - A[i][k]*fator
    for i in range(c-1, -1, -1): 
        if(A[i][i]!=0):
            b[i]=(b[i])/A[i][i]
            A[i][i]= A[i][i] /A[i][i]
    for i in range(c-1, -1, -1):   
        x[i]=b[i]
    print("Solucao")
    for i in range (c):
        print('Valor de x['+ str (i+1) +'] = %f' %(x[i]))
    end = timer()-start
    print("Tempo de execução: %.6f"%end)
    
def graph(formula, x_range,label):  
    x = np.array(x_range)  
    y = formula(x)  # <- note now we're calling the function 'formula' with x
    plt.plot(x, y,label=label)
    
def eq1(x):
    return (18-3*x)/2
def eq2(x):
    return (2+x)/2

    
SEIDEL(A,b,x,emin,imax)
JACOBI(A,b,x,emin,imax)

graph(eq1,range(0,5),"Equacao 1")
graph(eq2,range(0,5),"Equacao 2")
plt.plot(x1s,x2s,'k:',color='blue', label = 'Seidel')
plt.plot(x1j,x2j,'k--',color='green', label = 'Jacobi')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Convergencia Gauss-Seidel e Gauss-Jacobi')
plt.legend()
plt.show()

INGENUO(A,x,b)
JORDAN(A,x,b)
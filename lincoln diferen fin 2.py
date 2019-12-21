import numpy as np
import pylab 


def coef(x, y):
    for i in range(n):
        a[i] = y[i]
    for j in range(1, n):
        for i in range(n-1,j-1,-1):
            a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])
    print(a)
    temp = 0
    for i in range(n-1,-1,-1):
        temp = temp*(ponto-x[i]) + a[i]
    return temp

x = [2.6, 2, 3.5, 3.7, 4, 4.5]
y = [2,4,24,16,8,28]
a = np.zeros(len(x))

ponto = float(input("Insira o ponto: "))

n = int(input("Ordem-polinomio: "))+1
while n > int(len(x)):
    n = int(input("Ordem-polinomio: \n"))+1


resultado =coef(x,y)
print(resultado)

k = np.linspace(-10,10,100)
y = a[0] + a[1]*(k-x[0]) + a[2]*(k-x[0])*(k-x[1]) + a[3]*(k-x[0])*(k-x[1])*(k-x[2]) + a[4]*(k-x[0])*(k-x[1])*(k-x[2])*(k-x[3]) + a[5]*(k-x[0])*(k-x[1])*(k-x[2])*(k-x[3])*(k-[4])

pylab.plot(k,y)

pylab.show() 
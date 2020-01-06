# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:46:00 2020

@author: Gabriel
"""
#import openpyxl
import csv
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
sns.set(style="darkgrid")
import matplotlib 

t=[]
k=[]
g=[]
conta=1
a=1

File = open('DADOS.csv')
LerFile = csv.reader(File)
dadosSJ = list(LerFile)

t.append(float(dadosSJ[0][0]))
k.append(float(dadosSJ[0][1]))


for lista in dadosSJ[conta:]:
    if lista == []:
        break
    else:
        #condição de quebra
        conta=conta+1
        if lista[0] == '0.50':
            g.append(t)
            g.append(k)
            t=[]
            k=[]
            t.append(float(lista[0]))
            k.append(float(lista[1]))
            continue
        ####################
        t.append(float(lista[0]))
        k.append(float(lista[1]))      
        
g.append(t)
g.append(k)      

for graf in range(0,len(g),2):
    
    figure(num=None, figsize=(15, 15), dpi=80, facecolor='w', edgecolor='k')
    matplotlib.rc('xtick', labelsize=20) 
    matplotlib.rc('ytick', labelsize=20) 
    years = g[graf]
    gdp = g[graf+1]
    
    # create a line chart, years on x-axis, gdp on y-axis
    plt.plot(years, gdp, color='blue', marker='', linestyle='solid')
    
    # add a title
    plt.title("Temperatura(°C) x Tempo(s)",fontsize=24)
    
    # add a label to the y-axis
    plt.ylabel("Temperatura",fontsize=22)
    plt.xlabel("Tempo",fontsize=22)
    #plt.show()
    plt.savefig('Grafico%s.png' %(a))
    a=a+1


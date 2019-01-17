#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:49:58 2019

@author: jeanmarioml
"""


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from math import ceil

#lendo dados de arquivo csv via Pandas
base = pd.read_csv('iris.csv')


#amostragem simples

#gerando amostras
np.random.seed(2345)
amostra = np.random.choice(a=[0, 1], size=150, replace=True, 
                           p=[0.5, 0.5])

len(amostra)
len(amostra[amostra==1])
len(amostra[amostra==0])


#amostragem estratiicada 

iris = pd.read_csv('iris.csv')
iris['class'].value_counts()

#gerando amostragem com 75 valores
#de forma proporcional a qtd de registros
#nesse caso 25 de cada

x,_,y,_ = train_test_split(iris.iloc[:, 0:4],iris.iloc[:,4],
                           test_size=0.5,stratify=iris.iloc[:,4])

y.value_counts()

infert = pd.read_csv('infert.csv')
infert['education'].value_counts()
#48, 47 e 5

X1,_,y1,_ = train_test_split(infert.iloc[:,2:9],infert.iloc[:,1],
                             test_size=0.6, stratify = infert.iloc[:,1])

y1.value_counts()


#Amostragem Sistemática

populacao = 150
amostra = 14
k = ceil(populacao / amostra) #ceil arredonda pra cima

#sorteio entre 1 e k
r = np.random.randint(low=1,high=k+1,size=1)

acumulador = r[0]
sorteados = []

for i in range(amostra):
   # print(acumulador)
   sorteados.append(acumulador)
   acumulador += k
   
base = pd.read_csv('iris.csv')

base_final = base.loc[sorteados]








#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 10:49:57 2019

@author: jeanmarioml
"""

from scipy.stats import binom

# binom.pmf(X,n,p) - probabilidade
# binom.cdf(X,n,p) - Cumulativa

#jogar moeda 5 vezes, sair 3 caras

prob = binom.pmf(3,5,0.5)

#4 sinais de 4 tempos, prob de pegar 0, 1, 2, 3, 4 sinais verdes

binom.pmf(0,4,0.25)
binom.pmf(1,4,0.25)
binom.pmf(2,4,0.25)
binom.pmf(3,4,0.25)
binom.pmf(4,4,0.25)


binom.cdf(4,4,0.25)

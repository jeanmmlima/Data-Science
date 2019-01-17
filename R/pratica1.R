#aula pratica 01

#qtd de linhas e colunas
dim(iris)


#AMOSTRAS ALEAT??RIAS
#1. gera apenas valores 0 e 1, 150 amostras, 
#replace=True, prob= probabiliade de cada um ser gerado. 
amostra = sample(c(0,1),150,replace=TRUE, prob = c(0.5,0.5))
amostra

#2. Tamanho de dados em amostra com valor igual 1 ou 0
length(amostra[amostra==1])
length(amostra[amostra==0])

#AMOSTRAS ESTRATIFICADAS

summary(iris)

#carrega pacote sampling
library(sampling)

#conjunto de dados, vetor com colunas, vetor com o tamanho de cada extrato
#srswor -> amostra aleatoria sem reposi????o
amostraIris2 = strata(iris,c("Species"), size=c(25,25,25), method="srswor")
summary(amostraIris2)


summary(infert)

amostras= strata(infert,c("education"),size=c(5,48,47),method="srswor")
summary(amostras)

# AMOSTRAGEM SISTEM??TICA
library(TeachingSampling)

#total, intervalo
amostra = S.SY(150,10)
amostra

amostrairis = iris[amostra,]
amostrairis

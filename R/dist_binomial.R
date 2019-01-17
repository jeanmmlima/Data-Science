
# dbinom() - Encontrar a probabilidade
# pbinom() - Cumulativa

# X - numero de sucessos
# n - total de eventos
# p - probabilidade de sucesso

#EXEMPLOS

#Jogar moeda 5 vezes, sair 3 caras
dbinom(3,5,0.5)

#4 sinais de 4 tempos, prob de pegar 0, 1, 2, 3, 4 sinais verdes
dbinom(0,4,0.25) #0 sinais
dbinom(1,4,0.25) #1 sinais
dbinom(2,4,0.25) #2 sinais
dbinom(3,4,0.25) #3 sinais
dbinom(4,4,0.25) #4 sinais

# cumulatira
pbinom(4,4,0.25)

## prova 12 questoes, 4 alternativas, prob de acertar 7
dbinom(7,12,0.25)
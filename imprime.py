# Imprime o melhor fitness da população
def melhorFitness(populacao, geracao):
    str = "Geracao {0}: {1}"
    print(str.format(geracao, populacao[0][1]))

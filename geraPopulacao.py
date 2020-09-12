import random
import avaliaPopulacao


# Gera um indivíduo da populacao
def geraIndividuo(distancias, demandas):
    demandas_aux = []
    for i in range(len(demandas)):
        demandas_aux.append([i, demandas[i]])

    individuo = []
    while demandas_aux:
        erb = random.choice(demandas_aux)
        indice = demandas_aux.index(erb)
        individuo.append(demandas_aux[indice][0])
        demandas_aux[indice][1] = demandas_aux[indice][1] - 1
        if demandas_aux[indice][1] <= 0:
            del demandas_aux[indice]
    return individuo, avaliaPopulacao.avaliaIndividuo(distancias, demandas, individuo)


# Gera a população
def geraPopulacao(distancias, demandas, tam_populacao):
    populacao = []
    for i in range(tam_populacao):
        populacao.append(geraIndividuo(distancias, demandas))
    return populacao

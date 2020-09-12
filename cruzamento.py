import random
import avaliaPopulacao


# Realiza o somatório de todos os fitness de uma populacao
def somaFitness(populacao):
    tamanho_populacao = len(populacao)
    soma = 0
    for i in range(tamanho_populacao):
        individuo = populacao[i]
        soma = soma + individuo[1]
    return soma


# Calcula o peso de cada indivíduo de acordo com o fitness
def calculaPesos(populacao, soma_fitness):
    tamanho_populacao = len(populacao)
    pesos = []
    for i in range(tamanho_populacao):
        individuo = populacao[i]
        peso = individuo[1] / soma_fitness * 100
        pesos.append(peso)
    return pesos


# Realiza o cruzamento entre dois individuos
# Baseado no operador OX
def cruzamento1(individuo_1, individuo_2, distancias, demandas):
    # definindo os pontos de corte
    ponto1 = random.randint(1, int(len(individuo_1[0]) / 2))
    ponto2 = random.randint(int(len(individuo_1[0]) / 2) + 1, len(individuo_1[0]) - 1)

    # coloca indices nos pais
    individuo1_aux = individuo_1[0].copy()
    individuo2_aux = individuo_2[0].copy()

    # Gera o filho 1
    filho_1 = [-1] * len(individuo_1[0])
    filho_1[ponto1:ponto2] = individuo1_aux[ponto1:ponto2]
    demandas_aux = demandas.copy()
    for i in filho_1:
        if i != -1:
            demandas_aux[i] = demandas_aux[i] - 1
    i = 0
    j = ponto2
    while (i < len(individuo_1[0])):
        if (j == len(individuo_1[0])):
            j = 0
        if demandas_aux[individuo2_aux[i]] > 0:
            demandas_aux[individuo2_aux[i]] = demandas_aux[individuo2_aux[i]] - 1
            filho_1[j] = individuo2_aux[i]
            j = j + 1
        i = i + 1

    # Gera o filho 2
    filho_2 = [-1] * len(individuo_1[0])
    filho_2[ponto1:ponto2] = individuo2_aux[ponto1:ponto2]
    demandas_aux = demandas.copy()
    for i in filho_2:
        if i != -1:
            demandas_aux[i] = demandas_aux[i] - 1
    i = 0
    j = ponto2
    while (i < len(individuo_1[0])):
        if (j == len(individuo_1[0])):
            j = 0
        if demandas_aux[individuo1_aux[i]] > 0:
            demandas_aux[individuo1_aux[i]] = demandas_aux[individuo1_aux[i]] - 1
            filho_2[j] = individuo1_aux[i]
            j = j + 1
        i = i + 1

    return [(filho_1, avaliaPopulacao.avaliaIndividuo(distancias, demandas, filho_1)),
            (filho_2, avaliaPopulacao.avaliaIndividuo(distancias, demandas, filho_2))]


# Realiza o cruzamento dos indivíduos de uma população
def cruzamento(populacao, pesos, probabilidade, distancias, demandas):
    nova_populacao = []
    lista = list(range(len(populacao)))
    while lista:

        # Seleciona individuo 1
        indice1 = random.choices(lista, pesos, k=1)[0]
        individuo1 = populacao[indice1]
        m = lista.index(indice1)
        lista.remove(indice1)
        del pesos[m]

        # Seleciona individuo 2
        indice2 = random.choices(lista, pesos, k=1)[0]
        individuo2 = populacao[indice2]
        m = lista.index(indice2)
        lista.remove(indice2)
        del pesos[m]

        if (probabilidade > random.random()):
            novos_individuos = cruzamento1(individuo1, individuo2, distancias, demandas)
            nova_populacao = nova_populacao + novos_individuos

    nova_populacao = populacao + nova_populacao

    # retorna a populacao
    return nova_populacao

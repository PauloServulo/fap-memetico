import random
import avaliaPopulacao


# Realiza a busca local em um indivíduo
def metodoDescidaRandomica(custoInicial, solucaoInicial, matrizDistancias, demandas, quantCidades, maxIter):
    i = 0
    while i < maxIter:
        solucao = solucaoInicial[:]
        custo = custoInicial
        pos = list(range(1, len(solucaoInicial)))
        n1 = random.choice(pos)
        pos.remove(n1)
        n2 = random.choice(pos)
        aux = solucao[n2]
        solucao[n2] = solucao[n1]
        solucao[n1] = aux
        custo = avaliaPopulacao.avaliaIndividuo(matrizDistancias, demandas, solucao)
        if custo < custoInicial:
            i = 0
            solucaoInicial = solucao[:]
            custoInicial = custo
        else:
            i += 1
    return solucaoInicial, custoInicial


# Realiza a busca local em todos os individuos da populacao
def buscaLocal(populacao, matrizDistancias, demandas, quantCidades):
    nova_populacao = []
    for individuo in populacao:
        atributos = individuo[0]
        custo = individuo[1]
        atributos, custo = metodoDescidaRandomica(custo, atributos, matrizDistancias, demandas, quantCidades, 5)
        nova_populacao.append([atributos.copy(), custo])
    return nova_populacao

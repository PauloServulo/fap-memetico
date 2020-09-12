import random
import avaliaPopulacao


# troca duas erbs de posição
def mutacao1(individuo):
    individuo_mutado = individuo.copy()

    # selecina duas posições para serem trocadas
    pos_aux = list(range(len(individuo)))
    cidade_1 = random.choice(pos_aux)
    pos_aux.remove(cidade_1)
    cidade_2 = random.choice(pos_aux)
    # realiza a troca
    aux = individuo_mutado[cidade_1]
    individuo_mutado[cidade_1] = individuo_mutado[cidade_2]
    individuo_mutado[cidade_2] = aux
    return individuo_mutado


# Realiza a mutação da populacao
def mutacao(populacao, distancias, demandas, probabilidade):
    tamanho_populacao = len(populacao)
    for individuo in populacao:
        if probabilidade > random.random():
            individuo_at = mutacao1(individuo[0])
            individuo_at = (individuo_at, avaliaPopulacao.avaliaIndividuo(distancias, demandas, individuo_at))
            populacao.append(individuo_at)
    return populacao

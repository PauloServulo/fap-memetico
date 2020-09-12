import lerArquivos
import geraPopulacao
import avaliaPopulacao
import cruzamento
import mutacao
import imprime
import buscaLocal
import time
import statistics

instancias = [["21", [[1, 1, 533],
                      [1, 2, 309],
                      [2, 1, 533],
                      [2, 2, 309],
                      [3, 1, 457],
                      [3, 2, 265],
                      [4, 1, 457],
                      [4, 2, 265],
                      [5, 1, 381],
                      [5, 2, 221],
                      [6, 1, 381],
                      [6, 2, 221],
                      [7, 1, 305],
                      [7, 2, 177],
                      [8, 1, 305],
                      [8, 2, 177]]]]

resultados = []

# Percorre todos as matrizes de distâncias e vetor de demandas
for classe in instancias:
    for inst in classe[1]:
        vetor_tempo = []
        vetor_resultado = []
        # Carrega os dados do problema
        distancias = lerArquivos.lerMatrizDistancias("instancias/" + classe[0] + "_celulas/C" + str(inst[0]) + ".txt")
        demandas = lerArquivos.lerVetorDemandas("instancias/" + classe[0] + "_celulas/D" + str(inst[1]) + ".txt")
        for i in range(3):

            # Contador das geracoes
            geracao = 0

            # Maximo de geracoes
            max_geracoes = 5

            # Probabilidade de cruzamento
            probabilidade_cruzamento = 0.9

            # Probabilidade de mutacao
            probabilidade_mutacao = 0.1

            # Tamanho da populacao
            tamanho_populacao = 10

            # inicia contagem do tempo
            inicio = time.time()

            # Gera população inicial
            populacao = geraPopulacao.geraPopulacao(distancias, demandas, tamanho_populacao)

            # inicia laço do algoritmo
            while geracao < max_geracoes:
                # Realiza busca local na populacao inicial
                populacao = buscaLocal.buscaLocal(populacao, distancias, demandas, len(demandas))

                # Calcula a soma de todos os fitness
                soma_fitness = cruzamento.somaFitness(populacao)

                # Calcula o peso de cada individuo
                pesos = cruzamento.calculaPesos(populacao, soma_fitness)

                # Realiza o cruzamento
                populacao = cruzamento.cruzamento(populacao, pesos, probabilidade_cruzamento, distancias, demandas)

                # Realiza Mutacao
                populacao = mutacao.mutacao(populacao, distancias, demandas, probabilidade_mutacao)

                # Realiza a seleção dos individuos
                populacao = avaliaPopulacao.selecionaMelhores(populacao, tamanho_populacao)

                # Ordena a populacao
                populacao = avaliaPopulacao.ordenaPopulacao(populacao)

                # imprime o melhor fitness da geracao
                imprime.melhorFitness(populacao, geracao)

                # incrementa a geracao
                geracao = geracao + 1

            # calcula tempo de execução
            tempo = time.time() - inicio

            # armazena o resultado de cada uma das 10 execuções
            vetor_tempo.append(tempo)
            vetor_resultado.append(populacao[0][1])

        # organizar e salvar resultados no arquivo
        media_tempo = statistics.mean(vetor_tempo)
        desvio_tempo = statistics.pstdev(vetor_tempo)
        variancia_tempo = statistics.variance(vetor_tempo)

        media_resultado = statistics.mean(vetor_resultado)
        desvio_resultado = statistics.pstdev(vetor_resultado)
        variancia_resultado = statistics.variance(vetor_resultado)

        max_resultado = max(vetor_resultado)
        min_resultado = min(vetor_resultado)

        resultados.append(
            ["C" + classe[0][0] + "_" + str(inst[0]) + "-D" + classe[0][0] + "_" + str(inst[1]),
             round(max_resultado, 4),
             round(min_resultado, 4),
             round(media_resultado, 4), round(desvio_resultado, 4), round(variancia_resultado, 4),
             round(media_tempo, 4), round(desvio_tempo, 4), round(variancia_tempo, 4)])
    lerArquivos.gravarRespostaArquivo(resultados, 'resultados/saida7.txt')

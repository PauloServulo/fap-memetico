import random
#Recebe um indivíduo e retorna qual é o valor da sua função de avaliação
def avaliaIndividuo(distancias,demandas,ind):
	individuo = ind.copy()

	matriz = [[0] * len(demandas)]
	linha = 0
	while individuo:
		erb = individuo[0]
		while matriz[linha][erb] != 0:
			linha = linha + 1
			if len(matriz) < linha + 1:
				matriz.append([0]*len(demandas))
				break

		verifica = 1
		i = 0
		while verifica == 1 and i < len(distancias[erb]):
			dist = distancias[erb][i]
			if dist > 0:
				if len(matriz) < dist + linha:
					for j in range(dist):
						matriz.append([0] * len(demandas))
				verifica = 1
				for j in range(dist):
					if matriz[linha + j][i] == 1:
						verifica = 0
						break
			i = i + 1

		if verifica == 1:
			for i in range(len(distancias[erb])):
				dist = distancias[erb][i]
				if dist > 0:
					for j in range(dist):
						matriz[linha + j][i] = -1
			matriz[linha][erb] = 1
			del individuo[0]
			linha = 0
		else:
			linha = linha + 1

		cont = 0
		for i in range(len(matriz)-1,0,-1):
			sair = 0
			for j in matriz[i]:
				if j == 1:
					sair = 1
					break
			if sair == 1:
				break
			else:
				cont = cont + 1

	freq = len(matriz) - cont
	return freq

#Dada uma população, seleceiona os melhores indivíduos de acordo com o tamanho da mesma
def selecionaMelhores(populacao, tamanho_populacao):
	populacao.sort(key=lambda x: x[1])
	populacao = populacao[:tamanho_populacao]
	return populacao

#Retorna uma população ordenada pelo seu fitness
def ordenaPopulacao(populacao):
	populacao.sort(key=lambda x: x[1])
	return populacao
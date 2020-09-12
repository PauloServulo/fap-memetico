#Lê a matriz de distâncias
def lerMatrizDistancias(nome_arquivo):
	arquivo = open(nome_arquivo)
	matriz_distancias = []
	for linha in arquivo:
		l = linha.split()
		l = list(map(int,l))
		matriz_distancias.append(l)
	arquivo.close()
	return(matriz_distancias)

#Lê o vetor de demandas
def lerVetorDemandas(nome_arquivo):
	arquivo = open(nome_arquivo)
	vetor_demandas = []
	for linha in arquivo:
		vetor_demandas = linha.split()
		vetor_demandas = list(map(int,vetor_demandas))
		return vetor_demandas

#Gravar resultados em um arquivo de saída
def gravarRespostaArquivo(resultados, nomeArquivoSaida):
	arquivo = open(nomeArquivoSaida, 'w')
	for i in resultados:
		for j in i:
			arquivo.write(str(j))
			arquivo.write('\t')
		arquivo.write('\n')
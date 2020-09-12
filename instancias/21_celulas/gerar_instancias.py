def gravarInstanciaArquivo(nomeArquivo,instancia):
    arquivo = open(nomeArquivo, 'w')
    for i in range(len(instancia)):
        for j in range(len(instancia[i])):
            if j < len(instancia[i])-1:
                arquivo.write(str(instancia[i][j]))
                arquivo.write(' ')
            else:
                arquivo.write(str(instancia[i][j]))
        if i < len(instancia)-1:
            arquivo.write('\n')
    arquivo.close()


c = [[7,1,1,0],[7,2,1,0],[6,1,1,0],[6,2,1,0],[5,1,1,0],[5,2,1,0],[4,1,1,0],[4,2,1,0]]

base = [[7,1,2,0,0,2,1,1,2,0,0,0,0,2,2,2,0,0,0,0,0],
[1,7,1,2,0,0,2,1,1,2,0,0,0,0,2,2,2,0,0,0,0],
[2,1,7,1,2,0,0,2,1,1,2,0,0,0,0,2,2,2,0,0,0],
[0,2,1,7,1,0,0,0,2,1,1,2,0,0,0,0,2,2,0,0,0],
[0,0,2,1,7,0,0,0,0,2,1,1,0,0,0,0,0,2,0,0,0],
[2,0,0,0,0,7,1,2,0,0,0,0,1,1,2,0,0,0,0,0,0],
[1,2,0,0,0,1,7,1,2,0,0,0,2,1,1,2,0,0,2,0,0],
[1,1,2,0,0,2,1,7,1,2,0,0,0,2,1,1,2,0,2,2,0],
[2,1,1,2,0,0,2,1,7,1,2,0,0,0,2,1,1,2,2,2,2],
[0,2,1,1,2,0,0,2,1,7,1,2,0,0,0,2,1,1,0,2,2],
[0,0,2,1,1,0,0,0,2,1,7,1,0,0,0,0,2,1,0,0,2],
[0,0,0,2,1,0,0,0,0,2,1,7,0,0,0,0,0,2,0,0,0],
[0,0,0,0,0,1,2,0,0,0,0,0,7,1,2,0,0,0,0,0,0],
[2,0,0,0,0,1,1,2,0,0,0,0,1,7,1,2,0,0,2,0,0],
[2,2,0,0,0,2,1,1,2,0,0,0,2,1,7,1,2,0,1,2,0],
[2,2,2,0,0,0,2,1,1,2,0,0,0,2,1,7,1,2,1,1,2],
[0,2,2,2,0,0,0,2,1,1,2,0,0,0,2,1,7,1,2,1,1],
[0,0,2,2,2,0,0,0,2,1,1,2,0,0,0,2,1,7,0,2,1],
[0,0,0,0,0,0,2,2,2,0,0,0,0,2,1,1,2,0,7,1,2],
[0,0,0,0,0,0,0,2,2,2,0,0,0,0,2,1,1,2,1,7,1],
[0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,2,1,1,2,1,7]]

cont = 1

for i in c:
    instancias_i = []
    for j in range(21):
        instancias_j = []
        for k in range(21):
            instancias_j.append(0)
        instancias_i.append(instancias_j)

    for j in range(21):
        for k in range(21):
            if base[j][k] == 0:
                instancias_i[j][k] = i[3]
            elif base[j][k] == 2:
                instancias_i[j][k] = i[2]
            elif base[j][k] == 1:
                instancias_i[j][k] = i[1]
            elif base[j][k] == 7:
                instancias_i[j][k] = i[0]
    nomeAquivo = 'C'+str(cont)+'.txt'
    gravarInstanciaArquivo(nomeAquivo,instancias_i)
    cont = cont + 1

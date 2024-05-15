def creandoMatriz():
    matriz = []
    for i in range(8):
        fila = []
        for j in range(8):
            fila.append(" * ")
        matriz.append(fila)
    return matriz

matriz = creandoMatriz()

for i in range(8):
    for j in range(8):
        print(matriz[i][j], end = " ")
    print("")

    
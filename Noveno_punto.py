def generar_matriz(m, n):
    matriz = [[(i * n) + j + 1 for j in range(n)] for i in range(m)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))

num_filas = 4
num_columnas = 5

matriz = generar_matriz(num_filas, num_columnas)
imprimir_matriz(matriz)

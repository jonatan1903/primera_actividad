def media_aritmetica(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

lista_numeros = [101, 202, 303, 404, 505]
print("La media aritmética es: ", media_aritmetica(lista_numeros))
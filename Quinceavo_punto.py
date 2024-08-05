def es_palindromo(texto):
    return texto == texto[::-1]

cadena = input("Ingresa una cadena de texto: ")

if es_palindromo(cadena):
    print("La palabra que ingresaste es un palindromo")
else:
    print("La palabra que ingresaste no es un palindromo")
def factorial (num):

    if num < 0:
        print("No existe el factorial de un numero negativo")
    
    else:

        num_factorial = 1

        for i in range(1, num + 1):
            
            num_factorial *= i

    return (num_factorial)
    

num = int(input("Ingrese el valor del numero que dese hallarle el factorial: ")) 

el_factorial_es = factorial(num)

print("El factorial del numero", num , "es: 5", el_factorial_es)
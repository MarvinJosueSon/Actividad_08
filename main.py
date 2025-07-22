def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    else:
        return n + fibonacci(n - 1)

def letraypalabras(palabra, letra):
    if len(palabra) == 0:
        return 0
    else:
        if palabra[-1] == letra:
            return 1 + letraypalabras(palabra[:-1], letra)
        else:
            return letraypalabras(palabra[:-1], letra)

def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

while True:
    print("==MENU==")
    print("1. Factorial")
    print("2. Suma de enteros")
    print("3. Suma Fibonacci")
    print("4. Contar letra en palabra")
    print("5. Invertir palabra")
    print("6. Potencia")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            n = int(input("Ingrese un número entero positivo: "))
            print(f"Factorial de {n} es: {factorial(n)}")

        case "2":
            n = int(input("Ingrese un número entero positivo: "))
            print(f"La suma es: {suma(n)}")

        case "3":
            n = int(input("Ingrese un número entero positivo: "))
            print(f"Fibonacci es: {fibonacci(n)}")

        case "4":
            palabra = input("Ingrese la palabra: ")
            letra = input("Ingrese la letra que desea contar: ")
            print(f"La letra '{letra}' aparece {letraypalabras(palabra, letra)} veces")

        case "5":
            cadena = input("Ingrese la palabra: ")
            print("Palabra invertida:", invertir_cadena(cadena))

        case "6":
            base = int(input("Ingrese la base: "))
            exponente = int(input("Ingrese el exponente: "))
            print(f"{base}^{exponente} = {potencia(base, exponente)}")

        case "7":
            print("Saliendo.")
            break

        case _:
            print("Opcion no encontrada")



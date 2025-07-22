def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def suma(n):
    if n==0:
        return 0
    else:
        return n+suma(n-1)

def fibonacci(n):
    if n==0:
        return 0
    else:
        return n+fibonacci(n-1)
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




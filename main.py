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
print(fibonacci(10))

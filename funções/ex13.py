def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

resultado = fatorial(5)
print("o fatorial de 5 é:", resultado)

def somaList(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

resultado = somaList([1, 2, 3, 4, 5])
print("A soma dos números é:", resultado)

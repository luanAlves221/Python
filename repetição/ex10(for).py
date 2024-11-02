numero = int(input("Digite um número: "))
soma = 0

for i in range(1, numero + 1):
    if i % 2 != 0:
        soma += i

    print("A soma dos números ímpares de 1 até", numero, "é:", soma)
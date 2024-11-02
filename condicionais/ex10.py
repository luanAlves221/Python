valorC = float(input("digite o valor da compra"))
if valorC > 100:
    desconto = valorC * 0.9
    print(f"Você recebeu 10% de desconto. O valor final da compra é: R$ {desconto:.2f}")
else:
    print(f"O valor da compra é: R$ {valorC:.2f}")
print("bem-vindo à calculadora de IMC")
altura = float(input("digite sua altura"))
peso = float(input("digite seu peso"))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("peso ideal")
else:
    print("Acima do peso")
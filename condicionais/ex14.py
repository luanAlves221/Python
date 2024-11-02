vendas = int(input("Digite o número de vendas realizadas no mês: "))

if vendas >= 50:
    bonus = vendas * 0.10
    print("Seu bônus é de", bonus, "reais.")
elif vendas >= 30 and vendas <= 49:
    bonus = vendas * 0.07
    print("Seu bônus é de", bonus, "reais.")
elif vendas >= 10 and vendas <= 29:
    bonus = vendas * 0.05
    print("Seu bônus é de", bonus, "reais.")
else:
    print("Você não tem direito a um bônus este mês.")

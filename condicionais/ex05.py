salario = float(input("digite o valor do seu salário"))
emprestimo = float(input("digite o valor do seu empréstimo"))

limite = salario * 0.30

if emprestimo <= limite:
    print("seu empréstimo foi aprovado")
else:
    print("seu empréstimo foi negado")

nota = float(input("Digite a nota da prova: "))

if nota >= 90 and nota <= 100:
    print("A")
elif nota >= 80 and nota < 90:
    print("B")
elif nota >= 70 and nota < 80:
    print("C")
elif nota >= 60 and nota < 70:
    print("D")
else:
    print("F")

a, b = 0, 1

for _ in range(5):
    print(a)
    a, b = b, a + b

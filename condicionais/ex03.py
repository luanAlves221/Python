temperatura = int(input("digite a temperatura em graus celsius"))
if temperatura < 15:
    print("está frio")
elif temperatura >= 15 and temperatura < 25:
    print("a temperatura está agradável")
else:
    print("está quente")

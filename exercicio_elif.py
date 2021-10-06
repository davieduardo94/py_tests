nota = float(input("Digite a nota de 0.0 a 10.0: "))

if nota < 6.0:
    print("Nota F")
elif nota <= 7.0:
    print("Nota D")
elif nota <= 8.0:
    print("Nota C")
elif nota <= 9.0:
    print("Nota B")
else:
    print('Nota A')
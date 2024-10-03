n = 1
soma = 0
num = int(input("Número de médias: "))
while n <= num:
    x = int(input(f"{n}º número: "))
    soma = soma + x
    n = n + 1
print (f"Média dos {num} números: {soma / num:.2f} ")   
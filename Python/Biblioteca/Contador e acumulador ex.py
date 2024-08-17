n = 1
#elemento neutro
soma = 0
num = int(input("Número de somas: "))
while n <= num:
    x = int(input(f"{n}º número: "))
#var acumulador
    soma = soma + x
#var contador   
    n = n + 1
print (f"Soma: {soma} ")
print ("Calculadora: Máximo divisor comum entre dois números")
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a
num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))
res = mdc(num1, num2)
print(f"\nO máximo divisor comum entre {num1} e {num2} é: {res}")
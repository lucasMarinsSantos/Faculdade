print ("Calculadora Fibonacci")
num = int(input("\nNúmero inteiro: "))
acom = 0
if num <= 0:
    print ("\nO número deve ser maior que zero")
elif num == 1 or num == 2:
    print (f"\nO número corresponde a {num:.0f}º é: 1")
else:
    fibo1, fibo2 = 1, 1
    for i in range(3, num + 1):
        fibo1, fibo2 = fibo2, fibo1 + fibo2
        acom = acom + 1
    print (f"\nO número Fibonacci correspondente a {num:.0f}º casa é: {fibo2:.0f}")
    
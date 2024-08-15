print ("Qual o maior e menor de 3 números\n")
while True:
    try:
        a = float(input("Primeiro número: \n"))
        b = float(input("Segundo número: \n"))
        c = float(input("Terceiro número: \n"))
        maior = max (a, b, c)
        menor = min (a, b, c)
        print (f"O maior número é : {maior:.2f}\nO menor número é : {menor:.2f}")
        break
    except ValueError:
        print("Digite apenas números!\n")
print ()
input ("Pressione enter para finalizar")
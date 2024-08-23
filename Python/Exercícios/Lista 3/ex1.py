print ("Ex. Nota entre zero e dez")
while True:
    try:
        x = float(input("\nDigite um número de 0 a 10: "))
        if 0 <= x <= 10:
            print ("\nSeu número é:", x)
            break
        else:
            print ("\nO número deve estar entre 0 e 10.")
    except ValueError:
        print ("\nDigite apenas números!")

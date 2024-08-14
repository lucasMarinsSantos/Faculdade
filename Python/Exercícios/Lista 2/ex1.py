print ("Qual o tipo do triângulo")
while True:
    try:
        lA = float(input("Tamanho do primeiro lado: "))
        lB = float(input("Tamanho do segundo lado: "))
        lC = float(input("Tamanho do terceiro lado: "))
        if lA == lB == lC:
            print("O triângulo é Equilátero")
        elif lA != lB != lC != lA:
            print ("o triângulo é escaleno")
        else:
            print ("O triângulo é isósceles")          
        break
    except ValueError:
        print ("Digite apenas números!")
print ()
input ("Pressione enter para finalizar")
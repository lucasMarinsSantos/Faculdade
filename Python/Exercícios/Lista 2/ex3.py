print ("Controle de pesca")
while True:
    try:
        peso = float(input("Quantos quilos foi pescado: \n"))
        if peso > 50:
            excesso = peso - 50
            multa = excesso * 4
        if peso <= 50:
            excesso = multa = 0
        print (f"O peso máximo permitido foi ultrapassado em: {excesso:.2f} Kg\nResultando na multa, no valor de: R$ {multa:.2f}")
        break
    except ValueError:
        print ("Digite apenas número!\n")
print ()
input ("Pressione enter para finalizar")
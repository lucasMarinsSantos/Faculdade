print ("Calculadora de latas de tinta para 'x' metros quadrados\n")
while True:
    try:
        area = float(input("Tamanho em metros quadrados da área a ser pintada: "))
        m2Lata = 18 * 3
        qL1 = area / m2Lata
        qL2 = area // m2Lata
        qL3 = qL1 - qL2
        if qL3 != 0:
            qL1 = qL2 + 1
        print (f'\nSerão necessárias: {qL1:.0f} lata(s) de tinta para {area:.2f} metro(s) quadrado(s)\nFicando no valor de R$ {qL1*80:.2f}')
        break
    except ValueError:
        print("Digite apenas número!")
print ()
input ("Pressione enter para finalizar")
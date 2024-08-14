print ('O carro foi multado?')
velocidade = float(input('Velocidade: '))
if velocidade > 110:
    multado  = (velocidade - 110) * 5
    print (f'O carro foi multado em {multado:.2f} R$')
else:
    print ('O carro não foi multado')
    
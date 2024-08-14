print ('Calculadora para aluguel de carros\n')
print ('Referência: 1 dia de aluguel = R$60,00 e R$0.15 por KM rodado\n')
while True:
    try:
        dia = int(input('Dias de uso do carro: \n'))
        percorrido = float(input('Quilômetros percorridos: \n'))
        valor = (dia*60) + (percorrido*0.15)
        print (f'O valor total do alugel é: R${valor:.2f}')
        break
    except ValueError:
        print ('Digite apenas números!\n')
print ()
input ('Pressione enter para finalizar') 
        

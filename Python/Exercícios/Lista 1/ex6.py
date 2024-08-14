print ('Calculadora de tempo de viagem\n')
print ('Formato de digitação\n Ex: 1.234,50 = 1234.50\n  Não separe as casas de milhares e use "." para separar a casa decimal\n')
while True:
    try:
        distancia = float(input('Distância da viagem em quilômetros: '))
        velocidade = float(input('Velocidade média em KM/h esperado: '))
        tempo = (distancia / velocidade) * 60
        hora = tempo / 60
        print (f'O tempo de viagem é: {tempo:.2f} minutos')
        break
    except ValueError:
        print ('Digite apenas números!\n')
print ()
print ('Pressione enter para finalizar')
        

print ('Conversor de temperatura: Celsius para Fahrenheit\n')
while True:
    try:
        cel = float(input('Digite a temperatura em graus Celsius: \n'))
        fah = (9*cel/5) + 32
        print (f'A temperatura em graus Fahrenheint é: {fah:.2f} Fº\n')
        break
    except ValueError:
        print ('Digite apenas números!\n')
input ('Pressione enter para finalizar')

print ('Conversor de temperatura: Fahrenheint para Celsius\n')
while True:
    try:
        fah = float(input('Digite a temperatura em Fahrenheint: '))
        cel = (fah-32) * 5/9
        print (f'A temperatura em Celsius é: {cel:.2f} Cº\n')
        break
    except ValueError:
        print ('Digite apenas números')
print ()
input ('Pressione enter para finalizar')

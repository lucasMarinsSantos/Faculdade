print ('Calculadora de redução da vida de um fumante\n')
while True:
    try:
        dia = int(input('Quantidade média de cigarros consumidos por dia: \n'))
        ano = int(input('Quantos anos consome cigarro: \n'))
        total =  (ano * 365 * dia * 10) / 1440
        print (f'O usuário perdeu em média pelo consumo de cigarro: {total:.0f} dias')
        break
    except ValueError:
        print ('Digite apenas números inteiros\n')
print ()
input ('Pressione enter para finalizar')

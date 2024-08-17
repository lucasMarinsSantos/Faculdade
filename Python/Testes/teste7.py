soma = 0
y = 0
while True:
    x = int(input('nº (zero sai): '))
    if x == 0:
        break
    soma = soma + x
    y = y + 1
if y != 0:   
    print (f'A média de {y} números é: {soma / y}')
else:
    print('Nenhum número foi inserido') 
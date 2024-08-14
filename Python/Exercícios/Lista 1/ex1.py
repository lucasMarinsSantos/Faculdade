print ('Soma de dois números inteiros.')
while True:
    try:
        n1 = int(input ('Digite o primeiro número: '))
        n2 = int(input ('Digite o segundo número: '))
        soma = n1 + n2
        print ('A soma dos dois número são: ', soma)
        break
    except ValueError:
        print ('Erro, Digite apenas números inteiros.')
print ()
input('Pressione enter para finalizar')

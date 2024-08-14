print ('Conversor de medidas: metros para milímetros\n')
print ('Utilize o formato correto para digitação\nEx: 1.239,50 = 1239.50\nNão separe os milhares e use "." como separador decimal\n')
while True:
    try:
        metro = float (input ('Digite seu valor em metros: \n'))
        resultado = metro * 1000
        if resultado.is_integer():
            resultado = int(resultado)
        print ('Seu resultado em milímetros é: ', resultado ,'mm')
        break
    except ValueError:
        print ('Digite apenas números e no formato citado!')
print ()
input('Pressione enter para finalizar')

               

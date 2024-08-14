print ('Desconto sobre mercadoria\n')
print ('Não separe a casa dos milhares e use "." para separar a casa decimal\nEx: 1.234,50 = 1234.50\n')
while True:
    try:
        mercadoria = float(input('Preço da mercadoria: '))
        porcentagem = float(input('Qual o percentual de desconto: '))
        desconto = (mercadoria/100) * porcentagem
        total = desconto + mercadoria
        print (f'O valor do desconto é de: R$ {desconto:.2f}')
        print (f'O valor final do produto é de: R$ {total:.2f}')
        break
    except ValueError:
        print ('Digite apenas números!')
input ('Pressione enter para finalizar')
       

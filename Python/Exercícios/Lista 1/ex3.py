print ('Conversor de "data" para segundos\nSerá convertido a quantidade de dias, horas, minutos e segundos digitados, para um total em segundos\n')
while True:
    try:
        dia = int(input('Digite os dias: '))
        hora = int(input('Digite as horas: '))
        minuto = int(input('Digite os minutos: '))
        segundo = int(input('Digite os segundos: '))
        resultado = (dia * 86400) + (hora * 3600) + (minuto * 60) + segundo
        print ('A quantidade total de segundos em: ', dia , ' dias,' , hora , ' horas,' , minuto , ' minutos e ' , segundo , ' segundos' , 'equivale a: ' , resultado , ' segundos')  
        break
    except ValueError:
            print ('Digite apenas números inteiros!')
print ()
input ('Pressione enter para finalizar')

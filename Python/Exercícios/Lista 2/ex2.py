print ("O ano é bissexto?")
while True:
    try:
        ano = int(input("Digite o ano: \n"))
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) :
            print ("O ano é bissexto\n")
        else:
            print ("O ano não é bissexto\n")
        break
    except ValueError:
        print ("Digite apenas números inteiros!\n")
print ()
input ("Pressione enter para finalizar")
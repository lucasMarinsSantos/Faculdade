print ("Digite nome de usuário != senha")
while True:
    usuario = input("\nDigite seu usuário: ")
    senha = input("\nDigite sua senha: ")
    if usuario == senha:
        print ("\nUsuário e senha iguais, tente novamente!")
    else:
        print ("\nUsuário cadastrado com sucesso")
        break
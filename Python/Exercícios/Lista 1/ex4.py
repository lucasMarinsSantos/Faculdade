print ('Calculadora de aumento do salário em porcentagem\n')
while True:
    try:
        salario = float(input('Digite o salário: '))
        porcentagem = float(input('Digite a porcentagem do aumento: '))
        aumento = (salario/100 * porcentagem) + salario
        print ('O salário de R$' , salario , ',calculado com o aumento de' , porcentagem , '%, resulta no valor total de: R$' , aumento , '\n')
        break
    except ValueError:
        print ('Digite apenas números!')
input ('Pressione enter para finalizar')

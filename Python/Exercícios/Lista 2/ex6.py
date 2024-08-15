print ("Calculo de sálario e descontos mensais")
while True:
    try:
        ganhoHora = float(input("Valor da hora de trabalho: "))
        horaMes = float(input("Horas trabalhadas no mês: "))
        salarioBruto = horaMes * ganhoHora
        ir = salarioBruto * 0.11
        inss = salarioBruto * 0.08
        sind = salarioBruto * 0.05
        salarioLiquido = salarioBruto - ir - inss - sind
        descontoTotal = salarioBruto - salarioLiquido
        print (f"Informes sobre o salário mensal:\n\nSalário Bruto: R${salarioBruto:.2f}\n\n     Descontos:\nImposto de renda: R$ {ir:.2f}\nINSS: R$ {inss:.2f}\nSindicato: R$ {sind:.2f}\n\nSalário liquído: R$ {salarioLiquido:.2f}\nDescontos totais: R$ {descontoTotal:.2f}")
        break
    except ValueError:
        print ("Digite apenas números!")
print ()
input ("Pressione enter para finalizar")
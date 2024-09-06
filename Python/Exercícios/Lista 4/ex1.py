from random import randint

print ("\n10 números aleatórios, mostrando o maior e menor deles\n")
x = 0
numsort = []
while x <10:
    x += 1
    num = randint (1,100)
    print(f"{x: .0f}º número: {num: .0f}")
    numsort.append(num)
    maior = numsort [0]
    menor = numsort [0]
    for num in numsort:
        if num > maior: maior = num
        if num < menor: menor = num
print (f"\nO menor número é o: {menor:.0f}, e o maior número é o: {maior:.0f}")
print ("\nFim!\n")
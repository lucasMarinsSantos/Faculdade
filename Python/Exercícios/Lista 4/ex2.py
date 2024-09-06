from random import randint

print ("\n20 números aleatórios com: Lista dos 20, dos números pares e ímpares\n")
x = 0
numsort = []
while x < 20:
    x += 1
    num = randint (1,100)
    numsort.append(num)
par = []
impar = []
for PeI in numsort:
    if PeI % 2 == 0:
        par.append(PeI)
    else:
        impar.append(PeI)
print ("Números aleatórios: " ,numsort , "\n")
print ("Números pares: " ,par , "\n")
print ("Números ímpares: " ,impar , "\n") 
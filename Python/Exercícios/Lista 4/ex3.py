print ("Três vetores: \n")
from random import randint
x = 0
v1 = []
v2 = []
v3 = []
while x <10:
    x += 1
    num1 = randint (1,100)
    v1.append(num1)
    v3.append(num1)
    num2 = randint (1,100)
    v2.append(num2)
    v3.append(num2)
print (f"1º Lista: {v1}")
print (f"2º Lista: {v2}")
print (f"3º Lista: {v3}")
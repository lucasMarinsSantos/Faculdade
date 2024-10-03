f = open(r'C:\Users\lucas\Desktop\Faculdade\Python\Exercícios\Lista 1\LucasGabrielMarinsDosSantos-1ºDSM.txt')
for linha in f.readlines():
    print(linha.strip())
f.close()

with open (r'C:\Users\lucas\Desktop\Faculdade\Python\Exercícios\Lista 1\LucasGabrielMarinsDosSantos-1ºDSM.txt') as f:
    print(f.read())
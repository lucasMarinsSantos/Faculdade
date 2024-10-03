n = int(input('Número: '))
for k in range(2, n+1):
    while n % k == 0:
        print(k)
        n = n // k

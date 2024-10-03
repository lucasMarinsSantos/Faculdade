import random
import time

inicio = time.perf_counter()

amostra = random.sample(range(10000000000), 10000000)

fim = time.perf_counter()

print(amostra)
print(f"A função demorou {fim - inicio} segundos para executar.")
print (len(amostra))

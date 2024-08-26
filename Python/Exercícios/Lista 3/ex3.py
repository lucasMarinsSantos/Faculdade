print ("Crescimento populacional")
paisA = 80000
paisB = 200000
a = 0
while paisA <= paisB:
    paisA = paisA + (paisA * 0.03)
    paisB = paisB + (paisB * 0.015)
    a = a + 1
print (f"Demorou {a:.0f} anos para o paísA ultrapassar a população do paísB")
x = 0
for i in range(18644, 33088):
    num = str(i)
    if "2" in num and "7" not in num:
        x += 1
print(x)

print ('Conta de telefonia')
minuto = float(input('Minutos usados:'))
if minuto <=200:
    print (f'O valor da conta é {minuto*0.20:.2f} R$')
elif minuto <=400:
    print (f'O valor da conta é {minuto*0.18:.2f} R$')
elif minuto <=800:
    print (f'O valor da conta é {minuto*0.15:.2f} R$')
else:
    print *(f'O valor da conta é {minuto*0.08:.2f} R$')
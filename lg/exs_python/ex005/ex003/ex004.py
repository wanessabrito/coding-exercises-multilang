num = 0 
while num != 10000:
    num = int(input('Digite um número: '))
    if num > 10000:
        print('Um pouco mais!')
    elif num < 10000:
        print('Um pouco menos!')
print ('Acertou')
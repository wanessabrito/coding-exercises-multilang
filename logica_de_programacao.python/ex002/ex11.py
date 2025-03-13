num = 0
num = int(input('Escreva um número: '))
maior = num
while num:
    if num > maior:
        maior = num
    num = int(input('Escreva um número: '))
print('O maior número nas tentativas foi',maior)



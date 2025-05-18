num  = float(input('Digite um número: '))
soma = 0
qtd = 0

while num != 0:
    soma+= num
    qtd += 1
    num  = float(input('Digite um número: '))

media = soma/qtd
print('Média',media)



num = int(input('Digite um número inteiro: '))
if num %2 == 0:
    print('O número é par.')
else:
    print('O número é impar')


ano = int(input('Digite um ano: '))
if (ano %4 == 0 and ano %100 != 0) or (ano %400 == 0):
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')
km = float(input('Escreva quantos quilômentros pretende viajar: '))
if km <= 0:
   print('Desculpe, digite um valor correspodente a km maior que 0.')
elif km <= 200:
   valor = km * 0.50
   print(f'Certo!, sua passagem deu o valor de R${valor:.2f}')
else:
   valor = km * 0.45
   print(f'Certo!, sua passagem deu o valor de R${valor:.2f}')
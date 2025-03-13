
'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

import math

# Solicita o tamanho da área ao usuário
tamanho_em_metros = float(input('Digite a quantidade em metros quadrados da área a ser pintada: '))

# Calcula a quantidade de tinta necessária com 10% de folga
litros_necessarios = tamanho_em_metros / 6 * 1.1

# Calcula a quantidade de latas de 18 litros necessárias
latas = math.ceil(litros_necessarios / 18)

# Calcula a quantidade de galões de 3,6 litros necessários
galoes = math.ceil(litros_necessarios / 3.6)

# Calcula a melhor combinação de latas e galões
latas_mistura = math.floor(litros_necessarios / 18)
litros_restantes = litros_necessarios % 18
galoes_mistura = math.ceil(litros_restantes / 3.6)

# Calcula o preço total para cada opção
valor_latas = latas * 80
valor_galoes = galoes * 25
valor_mistura = (latas_mistura * 80) + (galoes_mistura * 25)

# Exibe os resultados
print(f'Sua compra deu os respectivos preços:')
print(f'Por latas será R$ {valor_latas:.2f}')
print(f'Por galões será R$ {valor_galoes:.2f}')
print(f'Misturando latas e galões será R$ {valor_mistura:.2f}')
print(f'Para a mistura, você precisará de {latas_mistura} latas e {galoes_mistura} galões.')

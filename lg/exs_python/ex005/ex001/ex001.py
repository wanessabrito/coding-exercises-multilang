velocidade = float(input('Escreva sua velocidade percorrida: '))
if velocidade > 80: 
    valor_multa = (velocidade -80) * 5 
    print(f'Você foi multado, com o valor da multa totalizando em R${valor_multa:.2f}.')
else: 
    print('Você não foi multado.')
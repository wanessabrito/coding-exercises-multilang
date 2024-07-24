
print('Bem-vindo(a) à loja da Wanessa Brito Ramalho')

# Solicita o valor do pedido e a quantidade de parcelas:

valor_do_pedido = float(input('Digite o valor do pedido: R$'))
quantidade_de_parcelas = int(input('Digite a quantidade de parcelas: '))

# Define as taxas de juros baseadas na quantidade de parcelas:

if quantidade_de_parcelas < 4: # o Juros será de 0% (0 / 100)
    juros = 0 / 100
elif 4 <= quantidade_de_parcelas < 6: # o Juros será de 4% (4 / 100)
    juros = 4 / 100
elif 6 <= quantidade_de_parcelas < 9: # o Juros será de 8% (8 / 100)
    juros = 8 / 100
elif 9 <= quantidade_de_parcelas < 13: # o Juros será de 16% (16 / 100)
    juros = 16 / 100
elif quantidade_de_parcelas >= 13: # o Juros será de 32% (32 / 100)
    juros = 32 / 100
else:
    juros = None  

# Verifica se a quantidade de parcelas é válida:

if juros is not None:
    valor_da_parcela = (valor_do_pedido * (1 + juros)) / quantidade_de_parcelas
    valor_total_parcelado = valor_da_parcela * quantidade_de_parcelas
    print(f'O valor das parcelas é de: R${valor_da_parcela:.2f}')
    print(f'O valor total parcelado é de: R${valor_total_parcelado:.2f}')
else:
    print('Erro: Escreva um valor válido')




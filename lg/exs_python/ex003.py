def escolha_modelo():
    while True:
        texto = '''
MCS - Manga Curta Simples
MLS - Manga Longa Simples
MCE - Manga Curta com Estampa
MLE - Manga Longa com Estampa
'''
        print(texto)
        modelo = input('Digite o modelo desejado: ').strip().upper()

        # Verifica qual modelo foi escolhido e retorna o preço correspondente
        match modelo:
            case 'MCS':
                return 1.80
            case 'MLS':
                return 2.10
            case 'MCE':
                return 2.90
            case 'MLE':
                return 3.20
            case _:
                print('Escolha inválida, digite o modelo novamente.')

def num_camisetas():
    while True:
        try:
            num = int(input('Digite a quantidade de camisetas: '))

            if num < 20:
                print('Não será aplicado desconto')
                return num, 0
            elif num > 2000:
                print('Não aceitamos tantas camisetas de uma vez.')
                continue  # Volta ao início do loop para pedir o número novamente

            else:  # Determina o desconto com base na quantidade de camisetas
                if 20 <= num < 200:
                    desconto = 5 / 100  # 5% de desconto
                elif 200 <= num < 2000:
                    desconto = 7 / 100  # 7% de desconto
                else:
                    desconto = 12 / 100  # 12% de desconto
                
                num_com_desconto = num - int(num * desconto) #Aplicando o desconto
                return num_com_desconto 
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def frete():
    while True:
        # Mostra opções de frete e solicita escolha ao usuário
        try:
            print('\n1 - Frete por transportadora: R$ 100.00\n2 - Frete por Sedex: R$ 200.00\n0 - Retirar pedido na fábrica: R$ 0.00')
            print(' ')
            frete_op = input('Escolha o tipo de frete: ').strip()  

            if frete_op == '1':
                return 100.00
            elif frete_op == '2':
                return 200.00
            elif frete_op == '0':
                return 0.00
            else:
                print('Opção de frete inválida. Digite 1, 2 ou 0.')

        except ValueError:
            print('Entrada inválida. Digite um número correspondente à opção de frete.')

# Mensagem inicial e opções de modelos
print('Bem vindo(a) à Fábrica de Camisetas da Wanessa Brito Ramalho.')


# Obtém valores de modelo, quantidade de camisetas e frete
valor_modelo = escolha_modelo()
quantidade = num_camisetas()
valor_frete = frete()

# Calcula o total com desconto
total = (valor_modelo * quantidade) + valor_frete

print(f'Total: R${total:.2f} = (Modelo: R${valor_modelo:.2f} * Quantidade(com desconto): {quantidade}  + Frete: R${valor_frete:.2f}).')

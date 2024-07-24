# criação do menu 
def menu():
    print('-'*6,'Bem-vindo(a) a Loja de Marmitas da Wanessa Brito Ramalho','-'*6)
    print('-'*27,'Cardápio','-'*33)
    print('-'*70)
    print('-'*4,'|',' Tamanho ','|',' Bife Acebolado(BA) ','|',' Fíle de Frango(FF) ','|','-'*5)
    print('-'*4,'|','    P   ',' |','      R$ 16.00   ','   |','       R$ 15.00','     |','-'*5)
    print('-'*4,'|','    M   ',' |','      R$ 18.00   ','   |','       R$ 17.00','     |','-'*5)
    print('-'*4,'|','    G   ',' |','      R$ 22.00   ','   |','       R$ 21.00','     |','-'*5)
    print('-'*70)

def fazer_pedido():
 total = 0

 while True:
    # Fazendo a leitura do sabor e inserido a mensagem de erro 
    sabor = input('Digite o sabor desejado: ').upper()
    if sabor not in ['BA', 'FF']:
        print('Sabor inválido! Tente novamente.')
        continue

    # Fazendo a leitura do tamanho e inserido a mensagem de erro
    tamanho = input('Digite o tamanho desejado: ').upper()
    if tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido! Tente novamente.')
        continue

    # Exibindo o pedido com base no sabor e tamanho
    if sabor == "BA":
        if tamanho == "P":
            total += 16.00
            print('Você pediu um Bife Acebolado no tamanho P: R$ 16.00')
        elif tamanho == "M":
            total += 18.00
            print('Você pediu um Bife Acebolado no tamanho M: R$ 18.00')
        elif tamanho == "G":
            total += 22.00
            print('Você pediu um Bife Acebolado no tamanho G: R$ 22.00')
    elif sabor == "FF":
        if tamanho == "P":
            total += 15.00
            print('Você pediu um Fíle de Frango no tamanho P: R$ 15.00')
        elif tamanho == "M":
            total += 17.00
            print('Você pediu um Fíle de Frango no tamanho M: R$ 17.00')
        elif tamanho == "G":
            total += 21.00
            print('Você pediu um Fíle de Frango no tamanho G: R$ 21.00')

    # Perguntando se deseja fazer outro pedido
    continuar = input('Deseja mais alguma coisa? (S/N):').upper()
    # Imprimindo o valor total com a escolha a mais do cliente
    if continuar == 'N':
        print('O valor Total a ser pago é',total)
        break
      
menu()
fazer_pedido()
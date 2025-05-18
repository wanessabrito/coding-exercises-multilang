nome = input('Digite seu nome: ')
sexo = input('Digite seu sexo: ')
valor = float(input('Digite o valor final da sua compra: '))
if sexo.lower() == 'mulher':
    desconto = valor * (13/100)
    valor_final = valor - desconto
    print( f'Feliz dias das Mulheres!, seu valor final com o desconto deu R${valor_final:.2f}.')
else:
    desconto = valor * (5/100)
    valor_final = desconto - valor 
    print(f'Feliz dias das Mulheres!, seu valor final com o desconto deu R${valor_final:.2f}.')
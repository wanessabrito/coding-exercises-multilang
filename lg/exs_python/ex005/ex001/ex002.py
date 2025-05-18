ano = int(input('Digite o ano do seu nascimento: '))
idade = 2024 - ano
if 18 > idade: 
    print('Você ainda è de menor, não pode votar.')
else:
    print('Você pode votar.')

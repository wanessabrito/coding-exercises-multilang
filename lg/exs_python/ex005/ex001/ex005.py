ano = int(input('Digite seu ano de nascimento: '))
idade = 2024 - ano 
if idade < 18:
    quanto_falta = 18 - idade
    print(f'Você ainda não tem idade suficiente para o alistamento militar, ainda faltam {quanto_falta} anos.') 
elif idade ==18:
    print('Você estar no ano de se alistar.')
elif idade > 18:
    quando_acaba = idade - 20 
    print(f'Seu alistamento militar ja acabou fazem {quando_acaba} anos. ')
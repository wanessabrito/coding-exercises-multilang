nm1= int(input('Escreva o primeiro número inteiro: '))
nm2= int(input('Escreva o segundo número inteiro: '))
if nm1 > nm2:
    print(f'O {nm1} é maior que o {nm2}.')
elif nm2 > nm1:
    print(f'O {nm2} é maior que o {nm1}.')
else:
    print('Os dois números são iguais.')
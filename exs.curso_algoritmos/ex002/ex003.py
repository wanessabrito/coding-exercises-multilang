nota1 =  float(input('Digite a sua primeira nota:  '))
nota2 =  float(input('Digite a sua segunda nota:  '))

media = (nota1 + nota2) /2

if media < 4:
    print ('Você foi reprovado.')
elif media <=6:
    print('Você estar de recuperação.')
else:
    print('Você passou.')
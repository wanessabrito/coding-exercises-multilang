nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: '))
anos = float(input('Digite seu tempo na empresa: '))
if anos == 3:
    aumento = anos*(3/100)
    salario_final = salario + aumento
    print(f'{nome} seu salário atual com o aumento será {salario_final:.2f}.')
elif 3 >= anos <=10:
    aumento = anos*(12.5/100)
    salario_final = aumento + salario
    print(f'{nome} seu salário atual com o aumento será {salario_final:.2f}')
elif 10>= anos:
    aumento = anos* (20/100)
    salario_final = aumento + salario
    print(f'{nome} seu salário atual com o aumento será {salario_final:.2f}.')
else:
    print('Salário não encontrado')
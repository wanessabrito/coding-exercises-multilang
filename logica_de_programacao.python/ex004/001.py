#EstruturaDeRepeticao
'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido'''

while True:
    numero = int(input('Digite uma nota(0 a 10): '))
    if 0 < numero < 10:
        print('Nota válida',numero)
        break
    else:
        print('erro')
    
print(' ')

'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

while True:
    user = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    if user == senha:
        print('O número de usuário não pode ser igual a sua senha!')
    else:
        print('Senha Salva...')
        break 
    
print(' ')

'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

while True:

    nome = input('Digite seu nome(maior que 3 caracteres): ')
    if len(nome) > 3:
        print(nome)
        break
    else:
        print("erro")

while True:

    idade = int(input('Digite sua idade: '))
    if 0 <= idade <= 150:
        print(idade)
        break 
    else:
        print('erro')

while True: 

    salario = float(input('Digite seu salário: '))
    if salario > 0:
        print(f'Seu salário é R${salario:.2f}')
        break 
    else:
        print('Desempregado ou mendigo?')

while True:

    sexo = input('Digite seu sexo(F/M): ').lower()
    if sexo in ['f','m']:
        if sexo == 'm':
            print('moça')
        else:
            print('moço')
            break
    else:
        print('erro')
    
while True: 

    estado_civil = input('Digite seu estado civil(S/C/V/D): ').upper()
    if estado_civil in ['S','C','V','D']:
        if estado_civil == 'S':
            print('Solteiro')
        elif estado_civil == 'C':
            print('Casado')
        elif estado_civil == 'V':
            print('viúvo')
        elif estado_civil == 'D':
            print('divorciada')
            break
    else:
        print('erro')
    
print(' ')




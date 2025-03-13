'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''
valor_hora = float(input('Digite o valor da sua hora de expediente: '))
horas_mes = int(input('Digite a quantidade de horas trabalhadas no mês: '))
salario_bruto = valor_hora * horas_mes

# Desconto do INSS e Sindicato
inss = salario_bruto * 0.10
sindicato = salario_bruto * 0.03

# Desconto do IR
if salario_bruto <= 900.00:
    ir = 0.00
elif salario_bruto <= 1500.00:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500.00:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.20

# FGTS (não descontado do salário)
fgts = salario_bruto * 0.11

# Total de descontos
total_descontos = ir + inss + sindicato

# Salário líquido
salario_liquido = salario_bruto - total_descontos

# Impressão das informações
print(f'Salário Bruto: ({valor_hora:.2f} * {horas_mes}): R${salario_bruto:.2f}')
print(f'(-) IR ({(ir / salario_bruto * 100) if salario_bruto != 0 else 0:.0f}%)       : R$ {ir:.2f}')
print(f'(-) INSS (10%): R$ {inss:.2f}')
print(f'(-) Sindicato (3%): R$ {sindicato:.2f}')
print(f'FGTS (11%): R$ {fgts:.2f}')
print(f'Total de descontos: R$ {total_descontos:.2f}')
print(f'Salário Líquido: R$ {salario_liquido:.2f}')

print(' ')

'''
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto
'''
try:
 ano = int(input('Escreva um ano: '))
 if (ano % 4 == 0  and ano % 100 != 0) or (ano % 400 == 0):
     print('O ano é bissexto')
 else:
     print('O ano não é bissexto')
except ValueError:
    print('Erro, digite novamente')

print(' ')

'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''
from datetime import datetime

def verificar_data(data_str):
    try:
        datetime.strptime(data_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

data_input = input('Digite a sua data de aniversário(xx/xx/xxxx):')

if verificar_data(data_input):
    print('A data é válida')
else:
    print('A data não é válida')

print(' ')

 # Faça um Programa que peça dois números e imprima o maior deles.
num1 = int(input('digite num1:'))
num2 = int(input('digite num2:'))
if num1 > num2:
    print('num1')
elif num2 > num1:
    print('num2')
else:
    print('==')

print(' ')

# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo
num1 = int(input('digite num1:'))
if num1 < 0:
    print('negativo')
else:
    print('positivo')


#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
genero = input('Escreva seu gênero(F/M): ').upper()
if genero  =='F':
    print('feminino')
elif genero =='M':
    print('masculino')
else:
    print('não encontrado, alen')

print(' ')

# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Escreva uma letra: ').upper()

if letra in ('A', 'E', 'I', 'O', 'U'):
    print('Vogal')
else:
    print('Consoante')

print(' ')

'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
nota1 = float(input('Nota1: '))
nota2 = float(input('Nota2: '))
media = (nota1 + nota2)/2
if media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
elif media == 10:
    print('Aprovado com Distinção')
else:
    print('erro')

print(' ')

# Faça um Programa que leia três números e mostre o maior deles.
try:
 num1 = int(input('digite num1:'))
 num2 = int(input('digite num2:'))
 num3 = int(input('digite num3:'))
 if num1 == num2 == num3:
     print('números iguais')
 elif num1 > num2 and num1> num3: 
    print('num1 maior')
 elif num2 > num1 and num2> num3: 
     print('num2 maior')
 elif num3 > num1 and num3 > num2: 
    print('num3 maior')
 else:
     print('Há um empate entre dois ou mais números')
except ValueError:
    print('Erro, digite novamente')
    
print(' ')

# Faça um Programa que leia três números e mostre o maior e o menor deles.

try:
 num1 = int(input('digite num1:'))
 num2 = int(input('digite num2:'))
 num3 = int(input('digite num3:'))

 if num1 == num2 == num3:
     print('números iguais')
 elif num1 > num2 and num1 > num3:
     if num2>num3:
         print('num1 é o maior e num3 é o menor.')
     else:
         print('num1 é o maior e num2 é o menor.')
 elif  num2 > num1 and num2 > num3:
     if num1>num3:
         print('num2 é o maior e num3 é o menor.')
     else:
         print('num2 é o maior e num1 é o menor.')
 elif  num3 > num2 and num3 > num1:
     if num2>num1:
         print('num3 é o maior e num1 é o menor.')
     else:
         print('num3 é o maior e num2 é o menor.')
 else:
     print('Há um empate entre dois ou mais números')
except ValueError:
    print('Erro, digite novamente')
    
print(' ')

# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('Digite o preço do primeiro produto: '))
produto2 = float(input('Digite o preço do segundo produto: '))
produto3 = float(input('Digite o preço do terceiro produto: '))
if produto3 < produto2 < produto1:
    print('Compre o produto 3 , pobre')
elif produto2 < produto1 < produto3:
    print('Compre o produto 2 , pobre')
elif produto1 < produto2 < produto3:
    print('Compre o produto 3 , pobre')
else:
    print('Digite novamente')

print(' ')

# Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = int(input('digite num1:'))
num2 = int(input('digite num2:'))
num3 = int(input('digite num3:'))

numeros= [num1,num2,num3]
numeros_ordenados = sorted(numeros, reverse=True)

print(f'{numeros_ordenados[0]},{numeros_ordenados[1]},{numeros_ordenados[2]}')

#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Digite o turno no qual estuda, escrever(M-matutino ou V-Vespertino ou N- Noturno): ').upper()
match turno:
    case 'M':
        print('Bom Dia')
    case 'V':
        print('Boa Tarde')
    case 'N':
        print('Boa Noite')
    case _:
        print('erro')
    
print(' ')

#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
num = int(input('Digite um número da semana(1-7):'))
match num:
    case '1':
        print('Segunda')
    case '2':
        print('Terça')
    case '3':
        print('Quarta')
    case '4':
        print('Quinta')
    case '5':
        print('Sexta')
    case '6':
        print('Sabádo')
    case '7':
        print('Domingo')
    case _:
        print('Erro, digite um número correspondente a 1 para 7.')

print(' ')

'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
numero = int(input('Digite um número de três digitos: '))
if numero != 0 and 100 <= numero <= 999:
     cetena = numero //100
     dezena = (numero % 100) // 10
     unidade = numero % 10
     print(f'{cetena} cetena , {dezena} dezena e {unidade} unidade.')
else:
    print('Digite o valor válido...')

print(' ')

'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
nota3 = float(input('Digite sua nota: '))
media = (nota1 + nota2 + nota3)/3
if media >= 7:
     print('Aprovado')
elif media <= 7:
     print('Reprovado')
elif media == 10:
     print('Aprovado com Distinção')
else:
     print('Erro, digite novamente...')

print(' ')




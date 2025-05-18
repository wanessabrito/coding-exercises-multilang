'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''
nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
media = (nota1 + nota2)/2
if 9 <= media <= 10:
    print('A - aprovado')
elif 7.5 <= media < 9:
    print('B - aprovado')
elif 6.0 <= media <7.5:
    print('C - aprovado')
elif 4.0 <= media < 6.0:
    print('D - reprovado')
elif 0 <= media <4:
    print('E - reprovado')
else:
    print('Nota inválida')

print(' ')

'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''
lado1 = float(input('Digite o lado:'))
lado2 = float(input('Digite o lado:'))
lado3 = float(input('Digite o lado:'))
if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado3 + lado2) > lado1:
    if lado1 == lado2 == lado3:
        print('Triângulo Equilátero')
    elif (lado1 == lado2) != lado3 or (lado1 == lado3) != lado2 or (lado3 == lado2) != lado1:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Não é um triângulo')

print(' ')

'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c= int(input('Digite o valor de C: '))
if a == 0:
    print('A equação não é do segundo grau...')
elif a != 0:
    delta = (b**2) - (4 * a * c)
    if delta < 0:
        print('A equação não possui raizes reais...')
    elif delta == 0:
        x = -b/(2*a)
        print(f'A equação possui apenas uma raiz real ={x:.2f}')
    else:
        import math
        raiz = math.sqrt(delta)
        x1 = (- b + raiz)/(2*a)
        x2 = (- b - raiz)/(2*a)
        print(f'As raízes da equação são: x1 = {x1:.2f} e x2 = {x2:.2f}')
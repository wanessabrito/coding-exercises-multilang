Base = 10
Altura = 4
Area = Base * Altura
print(Area)


x = 1.0 
print(type(x))

y = 18
print(type(y))

Z= x+y
print(type(Z))

a = 5+3j
type(a)
b=42
type(b)

print(' ')

x = 0.0
print(type(x))
y = 18
print(type(x))
z = x + y 
print(z)
print(type(z))

print(' ')

A = 'Questão 3'
B = 25
C = 3.9
print(type(A))
print(type(B))
print(type(C))

print(' ')


Base = (float(9))
Altura = (float(6))
Area = Base * Altura 
print('A área é',Area)

print(' ')


# Escreva a sequência de comandos para calcular o salário bruto de um pro-fissional que ganha por hora, sabendo que ele ganha R$ 14,25/h e trabalhou 163 horas normais e 20 horas extras (pagam o dobro)

valor_hora = 14.25
horas_trabalhadas = 163
hora_extra = 20

salario_normal = valor_hora * horas_trabalhadas
hora_extra_dobrada = valor_hora * 2
extra = hora_extra_dobrada * hora_extra
salario_bruto = salario_normal + extra 
print(f'O sálario bruto é {salario_bruto:.2f} ') 

print(' ')

A = 4
B = 5 
C = 1
qts1 = (A+B)/2
print(' O r vale', qts1)

print(' ')

# Escreva um programa que calcule o faturamento de um representante comercial que recebe R$ 500,00 fixos e 6% de comissão sobre as vendas do mês. Considere que ele fechou o mês com um valor de R$ 12.398,00 em vendas. Exiba o resultado com duas casas decimais



print('Início do Programa') 

print(' ') 

Fixo = 500.00 
Vendas = 12398.00 
Comissao = 6 / 100

Fat = Fixo + Vendas * Comissao

print(f'Faturamento do mês = {Fat:.2f}') 

print(' ')
      
print('Fim do Programa')

print (' ')

A = 4
B = 5
C = 1
discrimante = (B **2) - 4 *A*C
import math
raiz_discrimante = math.sqrt(discrimante)
x = (- B + raiz_discrimante)/ 2 * A 
x2 = (- B - raiz_discrimante)/ 2 * A
print('x é',x,x2)

print(' ')

A = 4
B = 5
C = 1
r = (3*A) + (2*B)/ A + B
print(r)

print(' ')
A = 4
B = 5
C = 1
z = (7.6*A) - (B ** 1.7)
print(f'z é {z:.2f}')

print(' ')

x1 = 1
y1 = 1
x2 = 4
y2 = 5

import math
raiz_d = ((x1 + x2)**2) + ((y1-y2)**2)
raiz_d = math.sqrt(raiz_d)
print(f'd1 é {raiz_d:.2f}')

print (' ')
x1 = 0.0
y1 = 0.0
x2 = 3.0
y2 = 4.0
d = 5.000
import math
raiz_d = ((x1 + x2)**2) + ((y1-y2)**2)
raiz_d = math.sqrt(raiz_d)
print(f'd2 é {raiz_d:.3f}')

print(' ')

Boneco_Malandrinho = int(17) * float(18.50) 
Spinner_Pequeno = int(36) * float(12.00)
Cubo_Mágico = int(7) * float(5.90)
soma = Boneco_Malandrinho + Spinner_Pequeno + Cubo_Mágico
print(f'O faturamento para cada produto foi:\nBoneco Maladrinho = {Boneco_Malandrinho:.2f}\nCubo Mágico = {Cubo_Mágico:.2f}\ne Spinner Pequeno = {Spinner_Pequeno:.2f}\nO faturamento total foi {soma:.2f}.')

print(' ')




# 1)Escreva um programa que mostre na tela a mensagem "Olá, Mundo!"
print('Olá,mundo')

# 2) Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas para ela:
nome=input('Qual é o seu nome? ')
print('Olá',nome,',È um prazer te conhecer!')

"""

3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
Ex:
Nome do Funcionário: Maria do Carmo
Salário: 1850,45
O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.
"""
nome_funcionario= input('Digite seu nome: ')
salario= float(input('Digite seu salário: '))
print(f'O funcionário(a) {nome_funcionario} tem um salário de {salario} em Junho.')

#4)  Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório entre eles.
numero1 = int(input('Digite um valor inteiro: '))
numero2 = int(input('Digite um segundo valor inteiro: '))
soma = numero1 + numero2
print(f'A soma entre {numero1}+{numero2} é {soma}')

#5)  Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1+nota2)/ 2
print(f'A média entre {nota1} e {nota2} é {media}')

#6  Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.
num1 =int(input('Digite um numero inteior: '))
antecessor = num1-1
sucessor = num1+1
print(f'O antecessor do {num1} é {antecessor} e o sucessor é {sucessor}')

# Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte.
num1 =int(input('Digite um numero inteiro; '))
dobro =num1*2
terca_parte = num1/3
print(f'O dobre de {num1} é {dobro} e o sua terça parte é {terca_parte}')

# Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
metro = float(input('Digite uma mediade de metros:'))
km = metro/1000
hm = metro/100
dam =metro/10
dm = metro*10 
cm = metro*100
mm = metro*1000
print(f'À distância em metro de {metro} corresponde á \n{km}km\n{hm}hm\n{dam}dam\n{dm}dm\n{cm}cm\n{mm}mm\n')

#Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.
dinheiro = float(input('Digite sua quantidade de dinheiro restante: '))
taxa= 3.45 
dolar = dinheiro / taxa
print(f'Com R${dinheiro:.2f} você terar em dolar {dolar:.2f}')

 #Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados.
 
largura =float(input('Digite a sua largura; '))
altura =float(input('Digite a sua altura: '))
area = largura * altura 
tinta = area/ 2
print(f'A área a ser pintada corresponde a {area}m^, sendo necessária a quatidade de tinta a ser usada é {tinta}l.')

# Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.
valorA =float(input('Digite o primeiro valor: '))
valorB =float(input('Digite o segundo valor: '))
valorC =float(input('Digite o terceiro valor: '))
delta =(valorB*2)-(4*valorA*valorC)
print(f'O valor de delta é {delta}')


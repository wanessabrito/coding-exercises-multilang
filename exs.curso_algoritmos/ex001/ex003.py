nome = input('Digite seu nome: ')
materia1 = float(input('Digite sua primeira nota: '))
materia2 = float(input('Digite sua segunda nota: '))
media = (materia1+materia2)/2
if media > 7:
    print('Você teve um bom aproveitamento.')
else:
    print('Você não teve um bom aproveitamento.')
    
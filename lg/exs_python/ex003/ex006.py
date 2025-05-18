
def inverter(num):
    invertido = str(num)[::-1]
    return int(invertido)

num = int(input('Digite um número: '))

invertido = inverter(num)
print('O número invertido é',invertido)


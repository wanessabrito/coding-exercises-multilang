
idade = int(input('Digite sua idade: '))
genero =input('Digite seu genêro: ')

while idade != 0 and genero != "":
    if genero == 'masculino' and idade<18:
        print('Boa noite rapaz')
    elif genero == 'masculino' and idade >= 18:
        print('Boa noite senhor')
    elif genero =="feminino" and idade<18:
        print('Boa noite moça')
    elif genero == 'feminino' and idade>=18:
        print('Boa noite senhora')
    idade = int(input('Digite sua idade: '))
    genero =input('Digite seu genêro: ')

print('fim')
nome =input('Digite seu nome: ')
sexo = input('Digite seu sexo: ')
estratura = float(input('Digite por fim a sua estratura: '))
if sexo.lower() == 'mulher':
    peso_ideal = (62.1*estratura) - 44.7
    print(f'{nome} seu peso ideal seria {peso_ideal}.')
elif sexo.lower() == 'homem':
   peso_ideal = (72,7*estratura)-58
   print (f'{nome} seu peso ideal seria {peso_ideal}.')
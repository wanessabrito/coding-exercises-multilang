largura = float(input('Dgite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

metros_quadrados = largura * comprimento
print (f'O terreno possui {metros_quadrados:.2f} metros quadrados.')
if metros_quadrados<100:
    print('Terreno Popular')
#elif 100 <= metros_quadrados < 500:
elif metros_quadrados >100 and metros_quadrados <500:
    print('Terreno Master')
else:
    print('Terreno Viper')

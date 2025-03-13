
caracter = input('Digite um caracter: ')
ascii= (ord('caracter'))
if 57 >= ascii >=48:
        print(f"{caracter} é uma letra.")
elif 122 >= ascii >97:
        print(f"{caracter} é um número.")
else:
        print(f"{caracter} é um símbolo.")

x=float(input('Digite a primeira X coordenada: '))
y=float(input('Digite a segunda Y coordenada: '))

if x>0 and y>0:
    print('Primeiro Quadrante')
elif x<0 and y>0:
    print('Segundo Quadrante')
elif x<0 and y<0:
    print('Terceiro Quadrante')
elif x>0 and y<0:
    print('Quarto Quadrante')
elif x == 0 and y==0:
    print('Você estar sobre o eixo.')
else:
    print('Não encontrei as coordenadas')
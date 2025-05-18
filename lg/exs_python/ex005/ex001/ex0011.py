print ('Advinhar animal, respostas com S/N: ')
tem_pelo = input('o animal tem pelos?').lower
late = input('o animal late?').lower
tem_asas = input('o animal tem asas').lower
voa = input ('o animal voa?').lower
faz_miau = input('o animal mia?').lower

if tem_pelo == 'Sim' and late =='Sim' and tem_asas == 'Não' and voa == 'Não' and faz_miau == 'Não':
    print('Cachorro')
if tem_pelo == 'Sim' and late =='Não' and tem_asas == 'Não' and voa == 'Não' and faz_miau == 'sim':
    print('Gato')
if tem_pelo == 'Não' and late =='Não' and tem_asas == 'SIm' and voa == 'Sim' and faz_miau == 'Não':
    print('Pássaro')
if tem_pelo == 'Não' and late =='Não' and tem_asas == 'Sim' and voa == 'Não' and faz_miau == 'Não':
    print('Galinha')
else:
    print('Não conheço')

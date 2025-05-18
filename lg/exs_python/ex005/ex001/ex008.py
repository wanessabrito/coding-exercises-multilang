# #sg1 = input 1 segm de seta 
# sg2 = input 2 segm de seta
# sg3 = input 3 segm de seta 
# if (sg1 < sg2 + sg3) and (sg2 <sg1+sg3) and (sg3 < sg2 + sg1) 
#    print (dar certo)
# else
# não dar certo  

sr1 = float(input('Digite o comprimento do primeiro segmento de reta: '))
sr2 = float(input('Digite o comprimento do segundo segmento de reta: '))
sr3 = float(input('Digite o comprimento do terceiro segmento de reta: '))

if (sr1 < (sr2 + sr3)) and (sr2 < (sr1+sr3)) and (sr3 < (sr2 + sr1)):
    print('È possível formar um triângulo.')

    if sr1 == sr2 == sr3: 
        print('O triângulo será EQUILÁTERO: todos os lados iguais')
    elif sr1 == sr2 or sr2 == sr3 or sr1 == sr3:
        print('O triângulo será ISÓSCELES: dois lados iguais')
    else:
        print('o triângulo será ESCALENO: todos os lados diferentes')
else:
    print('Não é possível formar um triângulo.')     

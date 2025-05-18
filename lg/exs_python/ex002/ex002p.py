print(1+2+3+4+5)
print((23+19+31)//3)
print(403%73)#resto da divisão
print(403//73)#numero inteiro 
print(2 ** 10 )#potencia 
print(abs(54-57))#valor absoluto 
print(54-57)
print(min(34,29,31))#menor valor

a = 3 #Atribuir o valor inteiro 3 á variavel a 
b = 4
c = a*a+b*b 
print(c)

#contatenação
s1 ='ant'
s2 ='bat'
s3 ='cod'
res = s1 +' '+s2+ ' '+s3 
print(res) 
#repetição
s1 = 'ant'
s2 = 'bat'
res = ((s1+' ') + (s2+' ')) *14  
print(res)

s1 = 'batbatcod'
res = (s1+' ')*10 
print(res)

#ex 001
numero = float(input('Digite um número: '))
percentual = float(input('Digite o desconto(0-100%): '))
desconto = numero*(percentual/100)
final = numero - desconto 
print(f'O desconto do valor {numero} é de {desconto}%. Sendo o valor final {final}.')
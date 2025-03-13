def contMat (numero):
    contador = 0
    while numero != 0: 
     numero //= 10
     contador +=1
     return contador 
    
num = int(input('Digite um número: '))
print (contMat(num))    


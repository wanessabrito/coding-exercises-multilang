import math

def eh_primo(num):
  for i in range(2, int(math.sqrt(num))+1 ):
    if num % i == 0:
      return False
  return True

num = int(input("Digite um número: "))
num+=1
while not eh_primo(num):
  num+=1
  print('O próximo primo é',num)
#Lojinha
mensagem = 'Olá, oque gostaria de levar hoje?\n1 - maça\n2 - banana\n3 - laranja'
print(mensagem)
produto = int(input('Digite sua escolha: '))
quantidade = int(input('Quantas unidades?: '))
if (produto == 1):
   pagar = quantidade * 2,30
   print(f'O valor da compra é de R${pagar}')
else:
   if (produto == 2):
      pagar = quantidade *1,85
      print(f'O valor da compra é de R${pagar}')
   else:
      if(produto == 3):
         pagar = quantidade*3,6
         print(f'O valor da compra é de R${pagar}')
      else:
         print(f'Produto inexitente!')

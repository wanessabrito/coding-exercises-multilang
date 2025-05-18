programa {
  inclua biblioteca Util --> u
  funcao inicio() {
    inteiro  n, acima_5 = 0 , d_3 = 0, cont = 0
    cadeia numeros_sorteados = " "

    enquanto(cont <= 19){
      n = u.sorteia(0,10)
      escreva("Número sorteado: ",n,"\n")
      numeros_sorteados = numeros_sorteados + n + " "
      cont ++
      se(n > 5){
        acima_5 ++
      }
      se(n % 3 == 0){
        d_3 ++
      }
    }
    escreva("----------------RESULTADOS----------------\n")
    escreva("a) Quais foram os números sorteados:",numeros_sorteados,"\n")
    escreva("b) Quantos números estão acima de 5:",acima_5,"\n")
    escreva("c) Quantos números são divisíveis por 3:",d_3)
  }
}

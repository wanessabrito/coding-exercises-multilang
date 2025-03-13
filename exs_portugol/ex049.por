programa {
  funcao inicio() {
    inteiro cont = 1, pares = 0, impares = 0, n
    enquanto(cont <= 6){
      escreva("Digite um número: ")
      leia(n)
      cont ++
      se (n % 2 == 0){
        pares ++
      }
      senao{
        impares ++
      }
    }
    escreva("Quantidade de ímpares = ",impares,", e quantidade de pares = ",pares,"\n")
    escreva("Acabou")
  }
}

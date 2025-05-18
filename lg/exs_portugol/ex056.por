programa {
  funcao inicio() {
    inteiro soma = 0, cont = 0, n 
    enquanto(n != 1111){
      escreva("Digite um número(para interromper digite 1111): ")
      leia(n)
      se(n != 1111){
        soma += n 
      }
    }
    escreva(soma)
  }
}

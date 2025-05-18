programa {
  funcao inicio() {
    inteiro soma = 0, cont = 1, n
    enquanto (cont <= 7){
      escreva("Digite o número: ")
      leia(n)
      cont ++
      soma += n
    }
    escreva("Soma = ",soma)
  }
}

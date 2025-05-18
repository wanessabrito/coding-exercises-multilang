programa {
  funcao inicio() {
    inteiro cont = 6, soma = 1
    enquanto(cont <= 100){
      escreva(cont, " + ")
      soma += cont
      cont += 2
    }
    escreva("= ",soma, " Acabou")
  }
}

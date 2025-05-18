programa {
  funcao inicio() {
    inteiro cont = 500, soma = 1
    enquanto(cont >= 0){
      escreva(cont," + ")
      soma += cont
      cont -= 50
    }
    escreva("= ",soma," Acabou")
  }
}

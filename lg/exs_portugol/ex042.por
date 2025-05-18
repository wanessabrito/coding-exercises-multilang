programa {
  funcao inicio() {
    inteiro numero, contador = 1
    escreva("Digite um número inteiro e postivo: ")
    leia(numero)
    enquanto(contador <= numero){
      escreva(contador," \n")
      contador = contador + 1
    }
    escreva("Acabou")
  }
}

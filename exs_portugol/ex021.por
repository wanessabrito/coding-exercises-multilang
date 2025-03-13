programa {
  funcao inicio() {
    inteiro ano
    escreva("Digite o ano: ")
    leia(ano)
    se (ano %4 == 0){
      escreva("O ano é bissexto")
    }
    senao{
      escreva("O ano não é bissexto")
    }
  }
}

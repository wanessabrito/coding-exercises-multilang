programa {
  funcao real media(real n1, real n2){
    inteiro result
    result = (n1 + n2)/2.0
    retorne result
  }
  funcao inicio() {
    real n1, n2
    escreva("Digite sua primeira nota: ")
    leia(n1)
    escreva("Digite sua segunda nota: ")
    leia(n2)
    escreva(media(n1,n2))
  }
}

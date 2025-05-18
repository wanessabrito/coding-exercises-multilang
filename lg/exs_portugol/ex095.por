programa {
  funcao inteiro somador(inteiro v1, inteiro v2){
    inteiro result
    result = v1 + v2
    retorne result
  }

  funcao inicio() {
    inteiro v1, v2, result
    escreva("Digite o primeiro valor: ")
    leia(v1)
    escreva("Digite o segundo valor: ")
    leia(v2)
    escreva(somador(v1,v2))
    
  }
}

programa {
  funcao inicio() {
    real a,b,c
    escreva("Digite o primeiro segmento de reta: ")
    leia(a)
    escreva("Digite o segundo segmento de reta: ")
    leia(b)
    escreva("Digite o terceiro segmento de reta: ")
    leia(c)
    se ((a + b) > c ou (a + c) > b ou (b + c)> a){
      escreva("È possível formar um triângulo")
    }
    senao{
      escreva("Não é possível formar um triângulo")
    }
  }
}

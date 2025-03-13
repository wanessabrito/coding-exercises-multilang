programa {
  funcao inicio() {
    inteiro a,b
    escreva("Digite o primeiro número: ")
    leia(a)
    escreva("Digite o segundo número: ")
    leia(b)
    se (a > b){
      escreva("O valor ",a, " é maior")
    }
    senao se ( b > a){
      escreva("o valor ",b, " é maior")
    }
    senao se (a == b){
      escreva("Os valores são iguais")
    }
    senao {
      escreva("Erro")
    }
  }
}

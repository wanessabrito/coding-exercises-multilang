programa {
  funcao inicio() {
    cadeia nome
    real n1, n2 , media
    escreva("Digite seu nome: ")
    leia(nome)
    escreva("Digite sua primeira nota: ")
    leia(n1)
    escreva("Digite sua segunda nota: ")
    leia(n2)
    media = (n1 + n2)/2
    se (media >= 7){
      escreva("Boa nota ",nome )
    }
    senao{
      escreva("Nota ruim ",nome)
    }
  }
}

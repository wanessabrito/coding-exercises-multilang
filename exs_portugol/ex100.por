programa {
  funcao real media(real n1, real n2){
    real media
    media = (n1 + n2)/2
    retorne media
  }
  funcao vazio Situacao(real media){
    se(media < 6){
      escreva("Reprovado")
    }
    senao se(media >= 6 e media <= 7){
      escreva("Recuperação")
    }
    senao{
      escreva("Aprovado")
    }
  }
  funcao inicio() {
    real n1, n2
    escreva("Digite sua primeira nota: ")
    leia(n1)
    escreva("Digite sua segunda nota: ")
    leia(n2)
    escreva("Média ",media(n1,n2)," = ")
    Situacao(media(n1,n2))
    
  }
}

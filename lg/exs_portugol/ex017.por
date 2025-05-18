programa {
  funcao inicio() {
    inteiro ano, idade
    escreva("Digite seu ano de nascimento: ")
    leia(ano)
    idade = 2025 - ano
    se (idade >= 18){
      escreva("Você tem ",idade," já pode votar")
    }
    senao {
      escreva("Você ainda tem ",idade, ", não pode votar")
    }

  }
}

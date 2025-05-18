programa {
  funcao inicio() {
    inteiro idade, ano
    escreva("Digite seu ano de nascimento: ")
    leia(ano)
    idade = 2025 - ano
    se (idade >=18){
      escreva("Pode votar!")
    }
    senao {
      escreva("Não pode votar!")
    }
  }
}

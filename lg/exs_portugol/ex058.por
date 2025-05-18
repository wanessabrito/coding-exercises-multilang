programa {
  funcao inicio() {
    inteiro idade, cont_idade = 0, soma_idade = 0
    real media
    enquanto(idade != 999){
      escreva("Digite sua idade(Para interromper digite '999'): ")
      leia(idade)
      se(idade != 999){
        cont_idade ++
        soma_idade += idade
      }
    }
    media = soma_idade/cont_idade
    escreva("Existem no total de ",cont_idade," alunos e sua média de idade do grupo é ",media)
  }
}

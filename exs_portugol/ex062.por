programa {
  funcao inicio() {
    inteiro idade, cont_idade = 0, soma_idades = 0, mais_21 = 0
    real media
    caracter resp = 'S'

    enquanto(resp == 'S'){
      escreva("Digite sua idade: ")
      leia(idade)
      escreva("Deseja continuar[S/N]: ")
      leia(resp)

      cont_idade ++
      soma_idades += idade 

      se(idade > 21){
        mais_21 ++
      }
    }
    media = soma_idades/cont_idade
    escreva("----------------------RESULTADOS---------------------\n")
    escreva("Foram no total de ",cont_idade, " idades registradas\n")
    escreva("A média de idade do grupo é de: ",media,"\n")
    escreva("São no total de ",mais_21," de pessoas com mais de 21 anos")
  }
}

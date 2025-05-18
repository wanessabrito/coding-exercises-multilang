programa {
  funcao inicio() {
    inteiro idade, cont = 0, cont_F = 0, cont_M = 0, soma_idade = 0, soma_idade_M = 0, mais_20_F = 0
    real media, mediaM
    caracter sexo
    enquanto(cont < 5){
      escreva("Digite seu sexo(F|M)")
      leia(sexo)
      escreva("Digite sua idade: ")
      leia(idade)

      soma_idade = soma_idade + idade

      se(sexo == "M"){
        cont_M ++
        se(idade > 0){
          soma_idade_M = soma_idade_M + idade
        }
      }
      senao se(sexo == "F"){
        cont_F ++
        se(idade > 20){
          mais_20_F ++
        }
      }
      cont ++
      se(cont_M == 0){
        mediaM = 0
      }
    }
    mediaM = soma_idade_M/cont_M
    media = soma_idade/cont

    escreva("----------------------RESULTADOS------------------------\n")
    escreva("Foram ",cont_M," homens cadastrados\n")
    escreva("Foram ",cont_F," mulheres cadastradas\n")
    escreva("A média de idade do grupo foi de: ",media,"\n")
    escreva("A média de idade referente a homens foi de: ",mediaM,"\n")
    escreva("A quantidade de mulheres que tem mais de 20 anos é de: ",mais_20_F)

  }
}

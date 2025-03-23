programa {
  funcao inicio() {
    inteiro idade[9]
    cadeia nome[9]
    para(inteiro i = 0; i < 9; i++){
      escreva("=====================\n")
      escreva("Digite seu nome: ")
      leia(nome[i])
      escreva("Digite sua idade: ")
      leia(idade[i])

    }
    escreva("\n")
    escreva("Pessoas menores de idade: \n")

    para(inteiro i = 0; i < 9; i++){
      se(idade[i] < 18){
        escreva(nome[i]," = ",idade[i], " | ")
      }
    }
  }
}

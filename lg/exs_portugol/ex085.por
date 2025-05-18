programa {
  funcao inicio() {
    cadeia nome[5]
    caracter sexo[5]
    real salario[5]
    para(inteiro i = 0; i < 5; i ++ ){
      escreva("Digite seu nome: ")
      leia(nome[i])
      escreva("Digite seu sexo[M/F]: ")
      leia(sexo[i])
      escreva("Digite seu salário: ")
      leia(salario[i])
    }
    escreva("\n")
    escreva("Mulheres que ganham mais de 5.000: \n")
    para(inteiro i = 0; i < 5; i ++){
      se(sexo[i] == 'F'e salario[i] > 5000){
        escreva(nome[i], " = ",salario[i]," | ")
      }
    }
  }
}

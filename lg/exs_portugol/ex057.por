programa {
  funcao inicio() {
    real salario, sF = 0, sM = 0
    caracter sexo , resp = 'S'
    enquanto(resp == 'S'){
      escreva("Digite seu sexo[F/M]: ")
      leia(sexo)
      escreva("Digite seu sálario: ")
      leia(salario)

      se(sexo == 'F'){
        sF += salario
      }senao{
        sM += salario
      }

      escreva("Deseja continuar?[S/N]: ")
      leia(resp)
    }
    escreva("O total de salários pagos aos homens é de: R$",sM,"\n")
    escreva("O total de salários pagos as mulheres é de: R$",sF,"\n")

  }
}

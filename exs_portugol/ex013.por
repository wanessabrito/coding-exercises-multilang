programa {
  funcao inicio() {
    real salario, novo_salario
    escreva("Digite seu salário atual: $")
    leia(salario)
    novo_salario = salario + (salario * (15/100))
    escreva("Seu novo salário com uma aumento de 15% é : $",novo_salario)
  }
}

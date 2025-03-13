programa {
  funcao inicio() {
    inteiro dias, horas
    real salario
    horas = 8
    escreva("Digite a quantidade de dias trabalhados durante este mês: ")
    leia(dias)
    salario = (horas*dias) * 25
    escreva("Seu salário será de: $",salario)
  }
}

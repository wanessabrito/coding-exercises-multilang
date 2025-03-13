programa {
  funcao inicio() {
    cadeia nome
    inteiro anos
    real salario, n_salario
    escreva("Digite seu nome: ")
    leia(nome)
    escreva("Digite seu salário: ")
    leia(salario)
    escreva("Digite quantos anos trabalha na empresa: ")
    leia(anos)
    se (anos <= 3){
      n_salario = salario + (salario*(3/100))
      escreva("Seu novo salário com aumento de 3% totalizou de ",n_salario)
    }
    senao se (anos >= 3 e anos <= 10 ){
      n_salario = salario + (salario*(12.5/100))
      escreva("Seu novo salário com aumento de 12.5% totalizou de ",n_salario)
    }
    senao se (anos > 10){
      n_salario = salario + (salario *(20/100))
      escreva("Seu novo salário com aumento de 20% totalizou de ",n_salario)
    }
    senao{
      escreva("Erro")
    }
  }
}

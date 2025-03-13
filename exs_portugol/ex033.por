programa {
  funcao inicio() {
    real valor_casa, salario, prets, limite
    inteiro anos
    escreva("Digite o valor da casa: R$")
    leia(valor_casa)
    escreva("Digite o seu salário: R$")
    leia(salario)
    escreva("Digite quantos anos pretende pagar: ")
    leia(anos)
    prets = valor_casa/(anos * 12)
    limite = salario * (30/100)
    se (limite >= prets ){
      escreva("Aprovado")
    }
    senao{
      escreva("Negado")
    }
  }
}

programa {
  funcao inteiro Maior(inteiro valor1, inteiro valor2){
    se(valor1 == valor2){
      escreva("Valores iguais = ")
    }
    se(valor1 > valor2){
      retorne valor1
    } senao{
      retorne valor2
    }

  }
  funcao inicio() {
    inteiro valor1, valor2, result

    escreva("Digite o primeiro número: ")
    leia(valor1)
    escreva("Digite o segundo número: ")
    leia(valor2)

    result = Maior(valor1,valor2)
    escreva(result)
    
  }
}

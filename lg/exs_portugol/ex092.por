programa {
  funcao vazio ParouImpar(inteiro valor1, inteiro valor2){
    se(valor1 == valor2){
      se(valor1 % 2 == 0){
        escreva("Valores iguais e pares")
      }senao{
        escreva("Valores iguais e impares")
      }
    }
    senao se(valor1 % 2 == 0){
      escreva("Valor ",valor1," é par\n")
      escreva("Valor ",valor2," é ímpar")
    }senao{
      escreva("Valor ",valor2," é par\n")
      escreva("Valor ",valor1," é ímpar")
    }
  }
  funcao inicio() {
    inteiro valor1, valor2
    escreva("Digite o primeiro valor: ")
    leia(valor1)
    escreva("Digite o segundo valor: ")
    leia(valor2)

    ParouImpar(valor1,valor2)  
 
  }
}

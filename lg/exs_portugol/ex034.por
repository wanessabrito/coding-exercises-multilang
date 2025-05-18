programa {
  funcao inicio() {
    real p, h, imc
    escreva("Digite seu peso: ")
    leia(p)
    escreva("Digite sua altura: ")
    leia(h)
    imc = p/(h*h)
    se ( imc <= 18.5){
      escreva("Abaixo do peso")
    }
    senao se (imc > 18.5 e imc <= 25){
      escreva("Peso ideal")
    }
    senao se (imc > 25 e imc <=30){
      escreva("Sobrepeso")
    }
    senao se (imc > 30 e imc <= 40){
      escreva("Obesidade")
    }
    senao se ( imc > 40){
      escreva("Obesidade mórbida")
    }
    senao{
      escreva("Erro")
    }
  }
}

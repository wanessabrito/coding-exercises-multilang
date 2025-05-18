programa {
  funcao inicio() {
    inteiro numero = 1
    enquanto(numero <= 30){
      numero = numero + 1
      se (numero % 4 == 0){
        escreva("[",numero,"] ")
      }
      senao{
        escreva(numero," ")
      }
    }
    escreva("Acabou")
  }
}

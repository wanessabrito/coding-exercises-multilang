programa {
  funcao inicio() {
    real l, c, area
    escreva("Escreva a largura do terreno: ")
    leia(l)
    escreva("Escreva o comprimento do terreno: ")
    leia(c)
    area = l*c
    se (area <= 100){
      escreva("Terreno Popular")
    }
    senao se (area >= 100 e area <= 500){
      escreva("Terreno Master")
    }
    senao se (area > 500){
      escreva("Terreno Vip")
    }
    senao{
      escreva("Erro")
    }
  }
}

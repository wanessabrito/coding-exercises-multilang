programa {
  funcao inicio() {
    real larg, alt, area, tinta
    escreva("Digite o valor da largura: ")
    leia(larg)
    escreva("Digite o valor da altura: ")
    leia(alt)
    area = larg * alt
    tinta = area/2
    escreva("A área equivale a: ", area ,"m² e a quantidade de tintas necessárias é ",tinta )
  }
}

programa {
  funcao inicio() {
    real km, p1, p2
    escreva("Digite a quantidade de km que deseja percorrer: ")
    leia(km)
    se (km <= 200){
      p1 = 0.50 * km
      escreva("O valor da viagem ficará de R$",p1)
    }
    senao {
      p2 = 0.45 * km
      escreva("O valor da viagem ficará de R$",p2)
    }
  }
}

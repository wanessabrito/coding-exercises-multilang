programa {
  funcao inicio() {
    real km, preco
    inteiro dias
    escreva("Digite o total de km percorridos: ")
    leia(km)
    escreva("Agora digite o total de dias que o carro foi alugado: ")
    leia(dias)
    preco = (km*0.20) + (dias*90)
    escreva("O total ficou de $",preco)


  }
}

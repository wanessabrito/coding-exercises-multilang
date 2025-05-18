programa {
  funcao inicio() {
    real preco, promo
    escreva("Digite o preço do produto: $")
    leia(preco)
    promo = preco - (preco*(5/100))
    escreva("O seu desconto de 5% ficou de $",preco," para $",promo)
  }
}

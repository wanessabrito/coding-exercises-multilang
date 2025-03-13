programa {
  funcao inicio() {
    cadeia carro
    inteiro dias
    real km, valor
    
    escreva("Digite o tipo de carro alugado( 1 - Carro popular| 2 -Carro de Luxo): ")
    leia(carro)
    escreva("Quantos dias de aluguel?: ")
    leia(dias)
    escreva("Quantos km foram pecorridos?: ")
    leia(km)

    se (carro == 1  e km <= 100){
      valor = (dias * 90) + (km * 0.20)
      escreva("Preço a ser pago: R$",valor)
      se (km > 100){
        valor = (dias * 90) + (km * 0.10)
        escreva("Preço a ser pago: R$",valor)
      }
    }
    senao se(carro == 2 e km <= 200){
      valor = (dias * 150) + (km * 0.30)
      escreva("Preço a ser pago: R$",valor)
      se( km > 200){
        valor = (dias * 150) + (km * 0.25)
        escreva("Preço a ser pago: R$",valor)
      }
    }
    senao{
      escreva("Erro")
    }
  }
}

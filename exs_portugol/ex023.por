programa {
  funcao inicio() {
    cadeia nome
    caracter sexo
    real promoF, valor, promoM
    escreva("Digite seu nome: ")
    leia(nome)
    escreva("Digite seu sexo(F,M): ")
    leia(sexo)
    escreva("Digite o valor das suas compras: ")
    leia(valor)
    se (sexo == 'F'){
      promoF = valor - (valor*(13/100))
      escreva("O valor total da sua compra com 13% de desconto totalizou de R$",promoF,"\nFeliz dias das Mulheres")

    }
    senao{
      promoM = valor - (valor*(5/100))
      escreva("O valor total da sua compra com 5% de desconto totalizou de R$",promoM)
    }
    
  }
}

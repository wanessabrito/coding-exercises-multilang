programa {
  funcao inicio() {
    real peso, altura, media, soma = 0
    inteiro mais_90 = 0, pequenos = 0, grandes = 0, cont = 0
    enquanto(cont < 7){
      escreva("Digite seu peso: ")
      leia(peso)
      escreva("Digite sua altura: ")
      leia(altura)

      soma = soma + altura

      se(peso > 90){
        mais_90 ++
      }
      se(peso > 100 e altura > 1.90){
        grandes ++
      }
      senao se (peso < 50 e altura < 1.60){
        pequenos ++
      }
      cont ++ 
    }
    media = soma/7
    escreva("---------------------------------RESULTADOS-----------------------------------------\n")
    escreva("A média da altura do grupo foi de: ",media,"\n")
    escreva("A quantidade de pessoas com mais de 90kg é de ",mais_90," pessoas\n")
    escreva("A quantidade de pessoas com menos de 50kg e com menos de 1.60m é de ",pequenos," pessoas\n")
    escreva("A quantidade de pessoas com mais de 100kg e com mais de 1.90m é de ",grandes," pessoas\n")
  }
}

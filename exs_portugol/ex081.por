programa {
  funcao inicio() {
    inteiro v[8], soma_idade = 0, maior_idade = 0
    real media

    para(inteiro i = 0; i < 8; i ++){
      escreva("======================\n")
      escreva("Digite sua idade: ")
      leia(v[i])
      soma_idade += v[i]
      se(v[i] > maior_idade){
        maior_idade = v[i]
      }
    }

    escreva("\n")
    escreva("Posições das idades maiores de 25: \n")

    para(inteiro i = 0; i < 8; i ++){
      se(v[i] > 25){
        escreva(i, " ")
      }
    }
    escreva("\n")
    escreva("A maior idade do grupo foi de ",maior_idade," anos\n")
    escreva("Posição da maior idades: \n")
  
    para(inteiro i = 0; i < 8; i ++){
      se(v[i] == maior_idade){
        escreva(i, " ")
      }
    }
    media = soma_idade/8.0
    escreva("-----------------------RESULTADO----------------------\n")
    escreva("A média de idade do grupo é de: ",media,"\n")
  }
}

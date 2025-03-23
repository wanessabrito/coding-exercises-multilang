programa {
  funcao inicio() {
    inteiro maior = 0, menor_5 = 0, cont = 1, maior_18 = 0, idade = 0, soma_idades = 0
    real media
    enquanto(cont <= 10){
      escreva("Digite sua idade: ")
      leia(idade)

      soma_idades = soma_idades + idade

      se(cont == 1){
        maior = idade
      }senao{
        se(idade > maior){
          maior = idade
        }
        se(idade < 5){
          menor_5 ++
        }
        se(idade > 18){
          maior_18 ++
        }
      }
      cont ++
      media = soma_idades/10
    }
    escreva("------------------------RESULTADOS----------------------\n")
    escreva("Há média de idade do grupo é: ",media,"\n")
    escreva("Há no total de ",maior_18," pessoas com mais de 18 anos\n")
    escreva("Há no total de ",menor_5," pessoas com menos de 5 anos\n")
    escreva("E por fim, a maior idade foi de ",maior," anos")
  }
}

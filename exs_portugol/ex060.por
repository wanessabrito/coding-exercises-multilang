programa {
  funcao inicio() {
    cadeia nome, mais_velha = "", mais_jovem = ""
    inteiro idade, maior = 0, menor = -1, mais_30M = 0, menos_18 = 0, soma = 0, cont = 0
    caracter sexo, result = 'S'
    real media

    enquanto(result == 'S'){
      escreva("Digite seu nome: ")
      leia(nome)
      escreva("Digite seu sexo[F/M]: ")
      leia(sexo)
      escreva("Digite sua idade: ")
      leia(idade)
      escreva("Deseja continuar[S/N]: ")
      leia(result)

      cont ++
      soma += idade

      se(idade > maior){
        maior = idade
        mais_velha = nome
      }

      se(sexo == 'F'){
        se(menor == -1 ou idade < menor){
          menor = idade
          mais_jovem = nome
        se(menor < 18){
          menos_18 ++ 
        }
      }
    }

      se(sexo == 'M'){
        se(idade > 30){
          mais_30M ++
        }
      }

    }
    media = soma/cont
    escreva("----------------------RESULTADOS-----------------------\n")
    escreva("A pessoa mais velha é ",mais_velha, " com ",maior," anos\n")
    escreva("A mulher mais jovem é a ",mais_jovem," com ",menor," anos\n")
    escreva("A média de idade do grupo é de: ",media,"\n")
    escreva("Há no total de ",mais_30M," homens com mais de 30 anos\n")
    escreva("Há no total de ",menos_18," mulheres com menos de 18 anos")
  }
}

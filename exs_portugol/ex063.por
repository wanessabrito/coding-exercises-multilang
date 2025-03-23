programa {
  funcao inicio() {
    inteiro num, menor = -1, soma = 0, par = 0, cont = 0
    real media
    caracter resp = 'S'

    enquanto(resp == 'S'){
      escreva("Digite um número: ")
      leia(num)
      escreva("Deseja continuar[S/N]?: ")
      leia(resp)

      cont ++
      soma += num
      se(menor == -1 ou num < menor){
        menor = num 
      }
      se(num % 2 == 0){
        par++
      }
    }
    media = soma/cont
    escreva("---------------------RESULTADOS---------------------")
    escreva("O somatório entre os valores é: ",soma,"\n")
    escreva("O menor valor digitado foi ",menor,"\n")
    escreva("A média entre os valores é: ",media,"\n")
    escreva("A quantidade de valores que são pares é de ",par)
  }
}

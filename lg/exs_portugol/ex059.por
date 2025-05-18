programa {
  funcao inicio() {
    inteiro idade, maior_id = 0, cont_M = 0, menor_idF = -1, soma_idM = 0
    real mediaM 
    caracter sexo, result = 'S'
    enquanto(result == 'S'){
      escreva("Digite sua idade: ")
      leia(idade)
      escreva("Digite seu sexo[F/M]: ")
      leia(sexo)
      escreva("Deseja continuar?[S/N]: ")
      leia(result)

      se(idade > maior_id ){
        maior_id = idade
      }
      se(sexo == 'M'){
        cont_M ++
        soma_idM += idade
      }

     se(sexo == 'F'){
      se(menor_idF == -1 ou idade < menor_idF){
        menor_idF = idade
      }
     }

     se(cont_M > 0){
      mediaM = soma_idM/cont_M
     }senao{
      mediaM = 0
     }

    }
    mediaM = soma_idM/cont_M

    escreva("-------------------RESULTADOS--------------------\n")
    escreva("Maior idade lida: ",maior_id,"\n")
    escreva("Foram no total de ",cont_M," de homens cadastrados\n")
    escreva("A idade da mulher mais jovem é de ",menor_idF," anos\n")
    escreva("A média de idade do grupo masculino é de: ",mediaM)
  }
}

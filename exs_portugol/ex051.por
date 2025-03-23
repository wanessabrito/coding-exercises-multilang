programa {
  funcao inicio() {
    inteiro cont = 1, maior = 0, menor = 0, valor
    enquanto(cont <= 8){
      escreva("Digite um valor: ")
      leia(valor)
      se (cont == 1){
        maior = valor
        menor = valor
      }senao{
        se(valor > maior){
          maior = valor
        }
        se( valor < menor){
          menor = valor
        }
      }
      cont ++
    }
    escreva("\nO maior valor digitado foi ",maior)
    escreva("\nO menor valor digitado foi ",menor)
  }
}

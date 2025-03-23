programa {
  funcao inicio() {
    inteiro v[10]
    para(inteiro i = 0; i < 10; i ++){
      escreva("Digite um número: ")
      leia(v[i])
    }

    para(inteiro i = 0; i < 10; i ++){
      escreva(v[i], " ")
    }

    escreva("\n")

    escreva("Posições dos números pares: ")
    para(inteiro i = 0; i < 10; i ++){
      se(v[i] % 2 == 0){
        escreva(i," ")
      }

    }
  }
}

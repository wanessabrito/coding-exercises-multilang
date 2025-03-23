programa {
  funcao inicio() {
    inteiro v[15]
    para(inteiro i = 0; i < 15; i++){
      escreva("Digite um número: ")
      leia(v[i])
    }
    para(inteiro i = 0; i < 15; i ++){
      escreva(v[i]," ")
    }
    para(inteiro i = 0; i < 15; i ++){
      se(v[i] % 10 == 0){
        escreva(i," ")
      }
    }
  }
}

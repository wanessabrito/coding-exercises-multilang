programa {
  funcao inicio() {
    cadeia v[7] 
    para(inteiro i = 0; i < 7; i++){
      escreva("Digite seu nome: ")
      leia(v[i])
    }
    para(inteiro i = 6; i > 0; i --){
      escreva(v[i], ",")
    }
    
  }
}

programa {
  inclua biblioteca Util --> u
  funcao inicio() {
    inteiro v[7]
    para(inteiro i = 0; i < 7; i++){
      v[i] = u.sorteia(1,50)
    }
    para(inteiro i = 0; i < 7; i++){
      escreva(v[i]," ")
    }
    
  }
}

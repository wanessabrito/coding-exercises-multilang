programa {
  funcao inicio() {
    inteiro v[10] 
    para(inteiro i = 0;i < 10; i++){
      se(i % 2 == 0){
        v[i] = 5
      }
      senao{
        v[i] = 3
      }
    }
    para(inteiro i = 0; i < 10; i++){
      escreva(v[i]," ")
    }
  }
}

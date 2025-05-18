programa {
  funcao inicio() {
    inteiro t1 = 1, t2 = 1, t3
    escreva(t1," ",t2," ")
    para(inteiro cont = 3;cont <= 10;cont ++){
      t3 = t1 + t2
      escreva(t3," ")
      t1 = t2
      t2 = t3
    }
    
  }
}

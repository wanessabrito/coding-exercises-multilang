programa {
  funcao vazio Fibonacci(inteiro valor){
    inteiro t1 = 1, t2 = 1, t3
    escreva(t1," ",t2," ")
    para(inteiro i = 2; i < valor; i ++){
      t3 = t1 + t2
      escreva(t3," ")
      t1 = t2
      t2 = t3
    }

  }
  funcao inicio() {
    inteiro valor
    escreva("Digite a quantidade de termos a serem mostrados ma tela: ")
    leia(valor) 
    Fibonacci(valor)

  }
}

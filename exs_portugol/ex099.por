programa {
  funcao inteiro Potencia(inteiro b, inteiro exp){
    inteiro result = 1
    para(inteiro i = 1; i <= exp; i++){
      result *= b
    } 
    retorne result
  }
  funcao inicio() {
    inteiro b, exp
    escreva("Digite a base: ")
    leia(b)
    escreva("Digite o expoente: ")
    leia(exp)
    escreva(Potencia(b,exp))    
  }
}

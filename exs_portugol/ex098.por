programa {
  funcao inteiro SuperSomador(inteiro inicio, inteiro fim){
    inteiro soma = 0
    para(inteiro i = inicio; i <= fim; i++){
      soma += i
    }
    retorne soma
  }
  funcao inicio() {
    inteiro inicio, fim
    escreva("Digite o começo: ")
    leia(inicio)
    escreva("Digite o fim: ")
    leia(fim)
    escreva(SuperSomador(inicio,fim))    
  }
}

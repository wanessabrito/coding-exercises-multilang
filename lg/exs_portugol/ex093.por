programa {
  funcao vazio contador(inteiro inicio, inteiro fim, inteiro incremento){
  para(inteiro i = inicio; i <= fim; i += incremento){
    escreva(i, " ")
  }
  }
  funcao inicio() {
    inteiro inicio, fim, incremento
    escreva("Digite o início: ")
    leia(inicio)
    escreva("Digite o fim: ")
    leia(fim)
    escreva("Digite o incremento: ")
    leia(incremento)

    contador(inicio,fim,incremento)
    
  }
}

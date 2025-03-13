programa {
  funcao inicio() {
    inteiro nC, nF, iN
    escreva("Digite o primeiro valor: ")
    leia(nC)
    escreva("Digite o último valor: ")
    leia(nF)
    escreva("Digite o incremento: ")
    leia(iN)
    enquanto(nF >= nC){
      escreva(nC," ")
      nC = nC + iN
    }
  }
}

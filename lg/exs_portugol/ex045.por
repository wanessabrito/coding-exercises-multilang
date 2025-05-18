programa {
  funcao inicio() {
    inteiro c, f, inc, cont
    escreva("Digite o primeiro valor: ")
    leia(c)
    escreva("Digite o último valor: ")
    leia(f)
    escreva("Digite o incremento: ")
    leia(inc)
    cont = c
    se (f > cont){
      enquanto(cont<=f){
        escreva(cont," ")
        cont += inc
      }
    }
    senao{
      enquanto(cont>=f){
        escreva(cont," ")
        cont -= inc 
      }
    }
  }
}

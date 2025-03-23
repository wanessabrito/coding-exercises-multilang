programa {
  funcao inteiro maior(inteiro a, inteiro b , inteiro c){
    inteiro maior
    se(a > b e a > c){
      maior = a
    }
    senao se(b > a e b > c){
      maior = b
    }
    senao se(c > a e c > b){
      maior = c
    }
    senao{
      escreva("Todos são iguais.")
    }
    retorne maior
  }
  funcao inicio() {
    inteiro a,b,c
    escreva("Digite o primeiro número: ")
    leia(a)
    escreva("Digite o segundo número: ")
    leia(b)
    escreva("Digite o terceiro número: ")
    leia(c)
    escreva(maior(a,b,c))
  }
}

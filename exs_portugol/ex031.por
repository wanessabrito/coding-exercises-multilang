programa {
  inclua biblioteca Util --> u
  funcao inicio() {
    inteiro comp = u.sorteia(1,3), teste
    cadeia a = "Papel vence Pedra", b = "Tesoura vence Papel", c = "Pedra vence de Tesoura" 
    escreva("Seja bem vindo(a), tente ganhar no JokenPo...\n")
    escreva(" 1 -- Papel\n 2 -- Tesoura\n 3 -- Pedra\n")
    escreva("Digite: ")
    leia(teste)
    se (comp == teste){
      escreva("Impate")
    }
    se (comp == 1 e teste == 3){
      escreva("Computador Ganhou!,",a)
    }
    senao se (comp == 3 e teste == 1){
      escreva("Você Ganhou!,",a)
    }
    senao se (comp == 2 e teste == 1){
      escreva("Computador Ganhou!,",b)
    }
    senao se (comp == 1 e teste == 2){
      escreva("Você Ganhou!,",b)
    }
    senao se (comp == 3 e teste == 2){
      escreva("Computador Ganhou!,",c)
    }
    senao se (comp == 2 e teste == 3){
      escreva("Você Ganhou!,",c)
    }
    }
  }

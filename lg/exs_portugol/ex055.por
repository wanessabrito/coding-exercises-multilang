programa {
  inclua biblioteca Util --> u
  funcao inicio() {
    inteiro numero, comp, cont = 0, acertos = 0, erros = 0
    comp = u.sorteia(1,10)
    enquanto(cont < 4){
      escreva("Digite um número: ")
      leia(numero)
      escreva("Número sorteado foi ",comp,"\n")
      se(numero == comp){
        escreva("Acertou \n")
        acertos ++
      }senao{
        escreva("Errou \n")
        erros ++
      }
      cont ++
    }
    escreva("Você acertou ",acertos," vezes e errou ",erros," vezes")
  }
}

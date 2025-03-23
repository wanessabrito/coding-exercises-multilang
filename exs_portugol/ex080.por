programa {
  inclua biblioteca Util --> u
  funcao inicio() {
    inteiro v[30]
    inteiro chave, chave_cont = 0
    escreva("Digite um número: ")
    leia(chave)

    escreva("Posição da sua chave: \n")
    para(inteiro i = 0; i < 30; i++){
      v[i] = u.sorteia(1,15)
      se(chave == v[i]){
        chave_cont++
        escreva(i," ")   
      }
    }
    escreva("\nQuantidade de vezes sorteadas: ",chave_cont)
    }
  }


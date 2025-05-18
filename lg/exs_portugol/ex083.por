programa {
  inclua biblioteca Util --> u
  funcao inicio() {
    inteiro v[20], aux

    para(inteiro i = 0; i < 20; i ++){
      v[i] = u.sorteia(0,99)
      escreva(v[i]," ")
    }
    escreva("\n")
    para(inteiro i = 0; i < 20; i ++){
      para(inteiro j = i + 1; j< 20; j++)
      se(v[i] > v[j]){
        aux = v[i]
        v[i] = v[j]
        v[j] = aux
      }
      escreva(v[i], " ")
    }
  }
}

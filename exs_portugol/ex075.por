programa {
  funcao inicio() {
    inteiro v[15]
    v[0] = 1
    v[1] = 1
    para(inteiro i = 2; i < 15; i++){
      v[i] = v[i - 2] + v[i - 1]
    }

    para(inteiro i = 0; i < 15; i ++)
    escreva(v[i]," ")
    }
  }


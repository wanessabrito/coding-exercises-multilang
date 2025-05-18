programa {
  funcao inicio() {
    inteiro p_termo, r, elementosPA = 0, soma = 0

    escreva("Digite o primeiro termo da PA: ")
    leia(p_termo)
    escreva("Digite a razão da PA: ")
    leia(r)

    escreva("\nO dez primeiros termos são: \n")

    para(inteiro cont = 0;cont < 10;cont++){
      elementosPA = p_termo + cont * r
      soma += elementosPA
      escreva(elementosPA," ")
    }
    escreva("\nA soma dos dez primeiros elementos da PA é ",soma)
  }
}

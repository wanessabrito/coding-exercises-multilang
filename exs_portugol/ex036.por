programa {
  funcao inicio() {
    real h, ponto = 0.05, v_pt, r_pt
    escreva("Digite a quantidade de horas que realizou atividades físicas este mês: ")
    leia(h)
    se (h <= 10){
      v_pt = h * 2
      r_pt = v_pt * ponto
      escreva("Você obteve ",v_pt," pontos, que totalizaram R$",r_pt)
    }
    senao se (h > 10 e h <= 20){
      v_pt = h * 5
      r_pt = v_pt * ponto
      escreva("Você obteve ",v_pt," pontos, que totalizaram R$",r_pt)
    }
    senao se (h > 20){
      v_pt = h * 10
      r_pt + v_pt * ponto
      escreva("Você obteve ",v_pt," pontos, que totalizaram R$",r_pt)
    }
    senao{
      escreva("Erro")
    }
  }
}

programa {
  funcao inicio() {
    inteiro f_dias, anos, ano, m_p, m_hrs
    real p_dias
    ano = 365
    m_p = 10
    m_hrs = 24*60
    escreva("Digite a quantidade de cigarros fumados por dia: ")
    leia(f_dias)
    escreva("Digite agora a quantidade de anos que já fumou: ")
    leia(anos)
    p_dias = (((ano * anos)* f_dias) * m_p)/m_hrs
    escreva("Você já perdeu ",p_dias," dias da sua vida")

  }
}

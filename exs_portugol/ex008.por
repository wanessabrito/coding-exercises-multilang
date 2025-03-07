programa {
  funcao inicio() {
    real  km, hm, dam, m, dm, cm, mm
    escreva("Digite uma distância em metros: ")
    leia(m)
    km = m/1000
    hm = m/100
    dam = m/10
    dm = m * 10
    cm = m * 100
    mm = m * 1000
    escreva("A distância de " + m + " corresponde a: " + km + "km " + hm + "hm " + dam + "dam " + dm + "dm " + cm + "cm " + mm + "mm")


  }
}

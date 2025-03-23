programa {
  funcao vazio gerador(cadeia frase, inteiro quantas, cadeia borda){
    para(inteiro i = 0; i < quantas; i ++){
     escreva("\n",borda,"\n")
     escreva("       Olá, Mundo!       ")
     escreva("\n",borda,"")
     escreva("\n")
     escreva("",borda,"\n")
     escreva("   ",frase,"       ")
     escreva("\n",borda,"")
     escreva("\n-x-x-x-x-x-x-x-x-x-x-x-x") 
    }

  }
  funcao inicio() {
    cadeia frase = "Apredendo Portugol"
    inteiro quantas
    cadeia borda[3] 
    borda[0] = "+-------=======-------+"
    borda[1] = "~~~~~~~~:::::::~~~~~~~~"
    borda[2] = "<<<<<<<<------->>>>>>>>"

    escreva("Digite a quantidade de vezes que se repita a frase: ")
    leia(quantas)

    gerador(frase, quantas, borda[0])  

  }
}

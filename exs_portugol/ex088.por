programa {
  funcao vazio gerador(cadeia frase, inteiro quantos){
    para(inteiro i = 0; i < quantos; i++){
     escreva("\n+-------=======-------+\n")
     escreva("       Olá, Mundo!       ")
     escreva("\n+-------=======-------+")
     escreva("\n")
     escreva("+-------=======-------+\n")
     escreva("   ",frase,"       ")
     escreva("\n+-------=======-------+")
     escreva("\n-x-x-x-x-x-x-x-x-x-x-x-x")
    }
  }
  funcao inicio() {
    cadeia frase = "Apredendo Portugol"
    inteiro quantos 

    escreva("Digite a quantidade de vezes que a frase se repita: ")
    leia(quantos)

    gerador(frase,quantos)
  }
}

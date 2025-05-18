programa {
  funcao inicio() {
   inteiro ano, idade, ant
   escreva("Digite seu ano de nascimento: ")
   leia(ano)
   idade = 2025 - ano
   ant = idade - 18

   se (idade < 18){
    escreva("Ainda faltam ", ant, " anos para seu alistamento militar")
   } 
   senao se (idade == 18){
    escreva("Seu alistamento militar irá acontecer este ano")
   }
   senao{
    escreva("Seu alistamento militar foi a ",ant, " anos")
   }
  }
}

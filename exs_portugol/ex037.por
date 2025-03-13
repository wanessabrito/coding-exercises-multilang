programa {
  funcao inicio() {
    real salario_at, salario_n
    inteiro anos
    caracter genero 
    escreva("Digite seu salário atual: R$")
    leia(salario_at)
    escreva("Digite seu gênero(M,F): ")
    leia(genero)
    escreva("Digite quantos anos trabalha na empresa: ")
    leia(anos)

    se ( genero == 'F'){
      se (anos < 15){
      salario_n = salario_at + (salario_at*(5/100))
      }
      senao se (anos >= 15 e anos < 20){
      salario_n = salario_at + (salario_at*(12/100))
      
      }
      senao se (anos >= 20){
        salario_n = salario_at + (salario_at*(23/100))
       
      }
    }
    senao se (genero == 'M'){
      se (anos < 20){
      salario_n = salario_at + (salario_at*(3/100))
      }
      senao se (anos <= 20 e anos > 30){
        salario_n = salario_at + (salario_at*(13/100))
        
      }
      senao se( anos > 30){
        salario_n = salario_at + (salario_at*(25/100))
        
     }
    }
    senao{
      escreva("Erro")
      retorne
    }
    escreva("Seu novo salário atual com o aumento é de R$",salario_n)
  }
}

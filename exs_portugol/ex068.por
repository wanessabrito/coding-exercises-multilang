programa {
  funcao inicio() {
   inteiro cont_f = 0, cont_m_100 = 0
   real mediaF, soma_pF = 0, maior_pM = 0

   para(inteiro cont = 1;cont <= 8;cont ++){
    real peso 
    caracter sexo

    escreva("Digite seu peso: ")
    leia(peso)
    escreva("Digite seu sexo[F/M]: ")
    leia(sexo)

    se(sexo == 'F'){
      cont_f ++
      soma_pF += peso
    }
    senao se(sexo == 'M'){
      se(peso > 100){
        cont_m_100 ++
      }
      se(peso > maior_pM){
        maior_pM = peso
      }
    }
    }
    se(cont_f > 0){
      mediaF = soma_pF/cont_f
    }
    senao{
      mediaF = 0
    }
    escreva("--------------------RESULTADOS-------------------\n")
    escreva("O total de mulheres cadastras foi de ",cont_f," mulheres\n")
    escreva("O total de homens que pesam mais de 100kg é de ",cont_m_100," homens\n")
    escreva("A média de peso de mulheres foi de: ",mediaF,"\n")
    escreva("O maior peso dos homens foi de ",maior_pM,"kg")
   }
  }


programa {
  funcao inicio() {
    real v[10], media, soma_notas = 0, cont_maior = 0, maior_nota = 0

    para(inteiro i = 0; i < 10 ; i ++){
      escreva("====================\n")
      escreva("Digite sua nota: ")
      leia(v[i])
      soma_notas += v[i]
      se(v[i] > maior_nota){
        maior_nota = v[i]
      }
    }
    media = soma_notas/10.0

    para(inteiro i = 0; i < 10; i ++){
      se(v[i] > media){
        cont_maior ++
      }
    }

    escreva("---------------------RESULTADOS--------------------\n")
    escreva("A média da turma é de: ",media,"\n")
    escreva("O total de alunos acima de média é de ",cont_maior," alunos\n")
    escreva("A maior nota foi de: ",maior_nota,"\n")
    escreva("A posição da maior nota: ")

    para(inteiro i = 0; i < 10; i ++){
      se(v[i] == maior_nota){
        escreva(i," ")
      }
    }

   }
  }


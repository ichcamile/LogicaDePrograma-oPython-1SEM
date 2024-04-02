programa {
  funcao inicio() {
    // As maçãs custam R$1,30 cada se forem compradas menos de uma dúzia, e R$1,00 se forem compradas pelo menos 12. 
    // Escreva um programa que leia o número de maçãs compradas, calcule e escreva o total da compra.

    inteiro quantidade
    real valor
    real total

    escreva("Quantas maças você deseja comprar? \n")
    leia(quantidade)

    se(quantidade >= 12){
      valor = 1.00
      total = quantidade*valor
      escreva("As maças valem R$1,00 \n o valor total da sua compra é " + total)
      

    }senao{
      valor = 1.30
      total = quantidade*valor
      escreva("As maças valem R$1,30 \n o valor total da sua compra é " + total)
    }

    

  }
}

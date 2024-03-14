programa {
  funcao inicio() {
    // As maçãs custam R$1,30 cada se forem compradas menos de uma dúzia, e R$1,00 se forem compradas pelo menos 12. 
    // Escreva um programa que leia o número de maçãs compradas, calcule e escreva o total da compra.

    real numero

    escreva("Quantas maças você deseja comprar? \n")
    leia(numero)

    se(numero >= 12){
      escreva("As maças valem R$1,00 \n")
    }senao{
      escreva("As maças valem R$1,30 \n")
    }

  }
}

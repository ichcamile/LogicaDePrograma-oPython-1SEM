programa {
  funcao inicio() {
    // As ma��s custam R$1,30 cada se forem compradas menos de uma d�zia, e R$1,00 se forem compradas pelo menos 12. 
    // Escreva um programa que leia o n�mero de ma��s compradas, calcule e escreva o total da compra.

    real numero

    escreva("Quantas ma�as voc� deseja comprar? \n")
    leia(numero)

    se(numero >= 12){
      escreva("As ma�as valem R$1,00 \n")
    }senao{
      escreva("As ma�as valem R$1,30 \n")
    }

  }
}

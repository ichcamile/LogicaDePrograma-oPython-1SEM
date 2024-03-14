programa {
  funcao inicio() {
  // Leia a velocidade máxima permitida em uma avenida e a velocidade com que o motorista estava dirigindo nela. Calcule a multa que uma pessoa vai receber, sabendo que são pagos:
    // a) R$50,00 se o motorista estiver ultrapassando em até 10 km/h a velocidade permitida (velocidade máxima: 50 km/h e o motorista a 60 km/h).
    // b) R$100,00 se o motorista ultrapassar de 11 a 30 km/h a velocidade permitida.
    // c) R$200,00 se estiver acima de 31 km/h da velocidade permitida.
  
    real velocidade 
    real avenidaMax
    real totalVelocidade

    escreva("Escreva a velocidade máxima da avenida \n")
    leia(avenidaMax)

    escreva("Escreva a velocidade em que estava dirigindo \n")
    leia(velocidade)

    totalVelocidade = velocidade - avenidaMax
    
    se(totalVelocidade <= 10){
      escreva("A sua multa é de R$50,00 \n")
    }senao se(totalVelocidade <= 30){
      escreva("A sua multa é de R$100,00 \n")
    }senao{
     escreva("A sua multa é de R$200,00 \n")

    }

  
  
  } 
}



"""Calcular a quantidade dinheiro gasto por um fumante. Dados: o número de 
anos que ele fuma, o nº de cigarros fumados por dia e o preço de uma carteira 
com 20 cigarros"""

def cigarettePrice():
    yearSmoke = int(input("How many years do you smoke?"))
    smokeDay = int(input("How many cigarretes do you smoke per day?"))
    smokePrice = float(input("How much does a pack containing 20 cigarettes cost? "))

    #calculo o valor do preço por cigarro
    pricePerCigarette = smokePrice/ 20

    #calculo quantos dias ele fumou
    daySmoke = yearSmoke*365

    #calculo o valor por dia que gasta fumando
    dayPrice = smokeDay*pricePerCigarette

    #calculo o preço total de todos esses dias
    totalPrice = dayPrice*daySmoke

    print("Actually you have spent " + str(totalPrice) + " in this years")

""" gere o preço de um carro ao consumidor e os valores pagos pelo imposto e 
pelo lucro do distribuidor, sabendo o custo de fábrica do carro e que são pagos: 

a) de imposto: 45% sobre o custo do carro; 

b) de lucro do distribuidor: 12% sobre o custo do carro."""

def priceCarFunction():
    #pergunta preço inicial do carro
    priceCar = float(input("Digite o valor do carro para saber mais sobre valores internos!"))

    #taxa do carro
    taxCar = 0.45 * priceCar

    #comissão
    commissionSales = 0.12* priceCar

    #calculo do preço final
    finalPrice = priceCar + taxCar + commissionSales

    print("The initial price is " + str(priceCar) + ". The total price is " + str(finalPrice) + ". The commission is about " + str(commissionSales) + ", and the tax is " + str(taxCar) + ".")



    
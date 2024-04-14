def cigarettePrice():
    """Calcular a quantidade dinheiro gasto por um fumante. Dados: o número de 
    anos que ele fuma, o nº de cigarros fumados por dia e o preço de uma carteira 
    com 20 cigarros"""
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
def priceCarFunction():

    """ gere o preço de um carro ao consumidor e os valores pagos pelo imposto e 
    pelo lucro do distribuidor, sabendo o custo de fábrica do carro e que são pagos: 

    a) de imposto: 45% sobre o custo do carro; 

    b) de lucro do distribuidor: 12% sobre o custo do carro."""
    #pergunta preço inicial do carro
    priceCar = float(input("Digite o valor do carro para saber mais sobre valores internos!"))

    #taxa do carro
    taxCar = 0.45 * priceCar

    #comissão
    commissionSales = 0.12* priceCar

    #calculo do preço final
    finalPrice = priceCar + taxCar + commissionSales

    print("The initial price is " + str(priceCar) + ". The total price is " + str(finalPrice) + ". The commission is about " + str(commissionSales) + ", and the tax is " + str(taxCar) + ".")
def sistemaDeNotas():
    """Calcular a média final dadas as notas das 3 provas e produzir uma saída com a 
        média e a situação do aluno de acordo com o seguinte critério: média >= 6, 
        aprovado; média >=3 e média < 6, recuperação; média < 3, reprovado. 
        Considerar também o número de faltas do aluno: se forem mais que 15 faltas, o 
        aluno estará automaticamente reprovado (o usuário deve fornecer o número 
        de faltas). Se o aluno se encontrar em recuperação, solicitar a nota da quarta 
        prova e, após calcular a média final, informar se o aluno passou (média final 
        >=5) ou não."""
    note1 = float(input("Digite sua nota em Geografia "))
    note2 = float(input("Digite sua nota em Matematica "))
    note3 = float(input("Digite sua nota em Filosofia "))
    media = (note1 + note2 + note3) / 3
    faltas = int(input("Qual seu total de faltas? "))

    if media >= 6 and faltas < 15:
        print("Você está aprovado")
        
    elif media >= 3 and media < 6 and faltas < 15:
        print("Você está recuperação")
        note4 = float(input("Digite sua nota em Eletivas "))
        media = (note1 + note2 + note3 + note4) / 4
        
        if media >= 6:
            print("Você está aprovado")
        else:
            print("Você está reprovado")        

    elif media < 3 and faltas < 15:
        print("Você está reprovado")   
        
    else: 
        print("Você está reprovado")
def maiorNumeroEntre():
    '''Para ler 3 números reais e verificar se o primeiro é maior que a soma dos outros dois.'''
    number1 = float(input("Digite um número "))
    number2 = float(input("Digite outro número "))
    number3 = float(input("Digite outro número "))
    somaDosDois = number2 + number3

    if number1 > somaDosDois:
        print("O primeiro número é maior que a soma dos outros números ")
    else:
        print("O primeiro número não é maior que a soma dos outros números ")
def produtoAtributos():
    '''Solicitar o nome do produto, descrição, preço e validade. Apresentar na tela os 
    dados recebidos.'''

    produto =  input("Digite o nome do produto ")
    descrição = input("Fale um pouco sobre o produto ")
    preço =  float(input("Qual é o preço do produto "))
    validade = input("Qual a validade do produto ")

    print("O nome do produto é " + str(produto) + " \n O descrição do produto é " + str(descrição) + "\n O preço do produto é " + str(preço) + "\n A validade do produto é " + str(validade))
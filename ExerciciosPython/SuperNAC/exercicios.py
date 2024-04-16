def cigarettePrice1():
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
def priceCarFunction2():

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
def sistemaDeNotas3():
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
def maiorNumeroEntre4():
    '''Para ler 3 números reais e verificar se o primeiro é maior que a soma dos outros dois.'''
    number1 = float(input("Digite um número "))
    number2 = float(input("Digite outro número "))
    number3 = float(input("Digite outro número "))
    somaDosDois = number2 + number3

    if number1 > somaDosDois:
        print("O primeiro número é maior que a soma dos outros números ")
    else:
        print("O primeiro número não é maior que a soma dos outros números ")
def produtoAtributos5():
    #Solicitar o nome do produto, descrição, preço e validade. Apresentar na tela os dados recebidos.'''
    produto =  input("Digite o nome do produto ")
    descrição = input("Fale um pouco sobre o produto ")
    preço =  float(input("Qual é o preço do produto "))
    validade = input("Qual a validade do produto ")

    print("O nome do produto é " + str(produto) + " \n O descrição do produto é " + str(descrição) + "\n O preço do produto é " + str(preço) + "\n A validade do produto é " + str(validade))
def somaDosCem6():
    resultado = 0
    for i in range(0, 101): 
        resultado += i
    print(f"A soma dos 100 primeiros números é: {resultado}")
def tabuada7():
    numero = float(input("Qual número você deseja saber a tabuada? (Nosso sistema aceita números decimais!)"))
    tabuada = int(input("Até qual número sua tabuada irá?"))
    
    for x in range(1, tabuada + 1):  # Alterado para incluir o número da tabuada
        resultado = numero * x
        print(f"{numero} x {x} = {resultado}")
def calcularPercentualVotos8():
    # Calcular o percentual de votos brancos, nulos e válidos em relação ao total de eleitores.

    nomeMunicipio = input("Qual o nome do seu município ")
    totalEleitores = int(input("Inclua o número de eleitores do " + str(nomeMunicipio) + "? "))
    
    votosBrancos = int(input("Qual o número de votos brancos?  "))
    while(votosBrancos > totalEleitores):
        print("O número de votos brancos excede ao total de moradores!!")
        votosBrancos = int(input("Qual o número de votos brancos? "))

    
    votosValidos = int(input("Qual o número de votos válidos?  "))
    while(votosValidos > totalEleitores):
        print("O número de votos nulos excede ao total de moradores!!")
        votosNulos = int(input("Qual o número de votos nulos?"))
    
    
    votosNulos = int(input("Qual o número de votos nulos?  "))
    while( votosNulos > totalEleitores):
        print("O número de votos válidos excede ao total de moradores!!")
        votosValidos = int(input("Qual o número de votos válidos?"))
    
    # Cálculo dos percentuais
    porcenBranco = (votosBrancos / totalEleitores) * 100
    porcenNulo = (votosNulos / totalEleitores) * 100
    porcenValidos = (votosValidos / totalEleitores) * 100
    
    # Verificação se a soma dos percentuais é maior que 100%
    while (porcenBranco + porcenNulo + porcenValidos) != 100  :
        print("A soma dos percentuais não é igual a 100%. Verifique os números inseridos.")
        votosBrancos = int(input("Qual o número de votos brancos? "))
        votosNulos = int(input("Qual o número de votos nulos? "))
        votosValidos = int(input("Qual o número de votos válidos? "))
        
        porcenBranco = (votosBrancos / totalEleitores) * 100
        porcenNulo = (votosNulos / totalEleitores) * 100
        porcenValidos = (votosValidos / totalEleitores) * 100

    # Exibição dos resultados
    print("\nResultado para o município de", nomeMunicipio)
    print("Votos brancos:", votosBrancos, "(", porcenBranco, "% )")
    print("Votos nulos:", votosNulos, "(", porcenNulo, "% )")
    print("Votos válidos:", votosValidos, "(", porcenValidos, "% )")
def positivoOuNegativo9():
    numero = float(input("Insira o número que você deseja verificar  "))
    
    if (numero >= 0):
        print("Esse número é positivo! ")
    else:
        print("Esse número é negativo! ")
    
    resposta = input("Deseja verificar outro número? Sim ou Não   ")

    while(resposta != "Não"):
        positivoOuNegativo()
def calcularSalarioFuncionario10():
    # Entrada de dados
    horasTrabalhadasMes = float(input("Quantas horas você trabalhou este mês? "))
    valorHora = float(input("Quanto custa a sua hora? "))

    # Verificação de horas extras
    if horasTrabalhadasMes > 160:  # 40 horas por semana * 4 semanas = 160 horas
        print("Você tem horas extras a receber!")
        
        horasExtras = horasTrabalhadasMes - 160
        salarioTotalSemExtras = 160 * valorHora
        salarioTotalExtras = horasExtras * valorHora * 1.5  # 50% de acréscimo para horas extras
        salarioTotal = salarioTotalSemExtras + salarioTotalExtras
        
        # Print explicativo sobre o cálculo das horas extras
        print(f"\nO funcionário trabalhou {horasTrabalhadasMes} horas no mês.")
        print(f"O salário total sem as horas extras é: R$ {salarioTotalSemExtras:.2f}")
        print(f"O funcionário trabalhou {horasExtras} horas extras no mês.")
        print(f"O salário total pelas horas extras é: R$ {salarioTotalExtras:.2f}")
        print(f"O salário total com as horas extras é: R$ {salarioTotal:.2f}")
    else:
        salarioTotal = horasTrabalhadasMes * valorHora

    # Saída de dados
    print(f"\nO salário total do funcionário é: R$ {salarioTotal:.2f}")
def calcularSalarioVendedor11():
    valorSalario =  float(input("Qual o valor do seu salario? "))
    valorComissao = float(input("Qual o valor da venda? "))
    valorSalarioTotal = 0

    if (valorComissao <= 1.500):
        valorSalarioTotal = valorSalario + (valorComissao * 0.03)
    else:
        valorSalarioTotal = valorSalario + (valorComissao * 0.05)
    print("O valor total do seu salário esse mês, sera:$" + str(valorSalarioTotal))
def verificarCompraEstoque12():
    # Lendo a quantidade atual em estoque
    quantidadeAtual = int(input("Digite a quantidade atual em estoque do produto: "))

    # Lendo a quantidade máxima em estoque
    quantidadeMaxima = int(input("Digite a quantidade máxima em estoque do produto: "))

    # Lendo a quantidade mínima em estoque
    quantidadeMinima = int(input("Digite a quantidade mínima em estoque do produto: "))

    quantidadeMedia = (quantidadeMaxima + quantidadeMinima) /2

    if quantidadeAtual >= quantidadeMedia:
        print("Não efetuar compra!")
    else: 
        print("Efetuar compra")
def somaDosMaiores13():
    #Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores
    valores = []

    for i in range(4):
        soma = float(input("Escreva um número para ser somado!"))
        valores.append(soma)
    
    valores = sorted(valores, reverse=True)
    valores.pop()
    valores = sum(valores)


    print(valores)
def nomeDoVencedor14():
    # Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.
    # Ler o nome dos times e os gols marcados
    time1 = input("Digite o nome do primeiro time: ")
    golsTime1 = int(input(f"Quantos gols {time1} marcou? "))

    time2 = input("Digite o nome do segundo time: ")
    golsTime2 = int(input(f"Quantos gols {time2} marcou? "))

    # Verificar o vencedor
    if golsTime1 > golsTime2:
        print(f"O vencedor é {time1}!")
    elif golsTime2 > golsTime1:
        print(f"O vencedor é {time2}!")
    else:
        print("EMPATE!")
def calcularValorCombustivel15():
    litroCombustivel = float(input("Quantos litros você comprou? "))
    tipoCombustivel = input("Qual tipo de combustivel? A-Álcool ou G-Gasolina: ").upper()

    while tipoCombustivel != "A" and tipoCombustivel != "G":
        print("Valor não encontrado! Talvez você esteja inserindo a condição errada.")
        tipoCombustivel = input("Qual tipo de combustivel? A-Álcool ou G-Gasolina: ").upper()

    if tipoCombustivel == "A":
      print("Você escolheu o Álcool")
      valorPorCombustivel = litroCombustivel* 3.39
      
      if litroCombustivel <= 20:
        desconto = 0.03
        valorDesconto = valorPorCombustivel * desconto
        valorPorCombustivel -= valorDesconto
        print(f"O valor total é: R${valorPorCombustivel:.2f}, com um desconto de R${valorDesconto:.2f}.")

      else:
        desconto = 0.05
        valorDesconto = valorPorCombustivel * desconto
        valorPorCombustivel -= valorDesconto
        print(f"O valor total é: R${valorPorCombustivel:.2f}, com um desconto de R${valorDesconto:.2f}.")

    elif tipoCombustivel == "G":
      print("Você escolheu o Gasolina")

      valorPorCombustivel = litroCombustivel* 4.89 
      
      if litroCombustivel <= 20:
        desconto = 0.04
        valorDesconto = valorPorCombustivel * desconto
        valorPorCombustivel -= valorDesconto
        print(f"O valor total é: R${valorPorCombustivel:.2f}, com um desconto de R${valorDesconto:.2f}.")

      else:
        desconto = 0.06
        valorDesconto = valorPorCombustivel * desconto
        valorPorCombustivel -= valorDesconto
        print(f"O valor total é: R${valorPorCombustivel:.2f}, com um desconto de R${valorDesconto:.2f}.")

    else:
        print("Valor não encontrado! Talvez você esteja inserindo a condição errada.")
def verificarAposentadoriaEmpregado16():
    idadeTrabalho = int(input("Digite o ano de nascimento do empregado: "))
    tempoTrabalho = int(input("Digite o ano de ingresso na empresa: "))
    anoAtual = 2024

    idadeTrabalho = anoAtual - idadeTrabalho
    tempoTrabalho = anoAtual - tempoTrabalho

    if idadeTrabalho >= 65 and tempoTrabalho >=30:
        print("Requerer aposentadoria")
    elif idadeTrabalho >= 65:
        print("Requerer aposentadoria")
    elif tempoTrabalho >=30:
        print("Requerer aposentadoria")
    else: 
        print("Não requerer!")
def imprimirNumerosCrescente17():
    for numero in range(1, 11):
        print(numero)
def imprimirNumerosDecrescente18():
    valores = []
    for numero in range(1, 11):
        valores.append(numero)
        valores = sorted(valores, reverse=True)
       
    print(valores)
def contarNegativos19():
    valores = []

    for i in range (0,3):
      valor = float(input("Escreva um número!"))
      if valor < 0:
          valores.append(valor)
    print(valores)
def calcularSomaSeisValores20():
    valores = []

    for i in range(6):
        valor = int(input("Escreva um número para ser somado!"))
        valores.append(valor)

    # Imprimindo os valores informados
    print("Valores informados:", valores)

    # Calculando a soma dos valores
    soma = sum(valores)
    print("Soma dos valores:", soma)

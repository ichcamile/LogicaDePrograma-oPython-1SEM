# exercicios dessa aula

def exercicio1():
# 1.Crie um programa que leia 10 valores inteiros em um vetor e, em seguida, mostre na tela os valores lidos.
    valoresArray = []
    
    for i in range(0,10):
        valor = input("Digite um dos valores!")
        valoresArray.append(valor)
    
    print(valoresArray)

def exercicio2():
   # Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado dos componentes deste vetor, armazenando o resultadoem outro vetor. Os conjuntos tem 20 elementos cada. Imprimir todas as listas.

    valoresReais = []
    valoresQuadrado = []
    quantidadeValores = int(input("Quantos números você quer no conjunto?"))

    for i in range(0,quantidadeValores):
        valor = int(input("Digite um dos valores: "))
        valoresReais.append(valor)
        valoresQuadrado.append(valor * valor) 

    print(valoresReais)
    print(valoresQuadrado)

def exercicio3():
    #Faça um programa que leia um vetor de 18 posições e, em seguida, leia também 2 valores (X e Y) quaisquer correspondentes a 2 posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y
    
    vetores = []

    for i in range(0,18):
        numerosVetor = int(input("Digite o número que irá entrar no Vetor"))
        vetores.append(numerosVetor)

        
    valorX = int(input("Digite um valor"))
    valorY = int(input("Digite um valor"))

    print("")
    while (valorX < 1 or valorX > 18) or (valorY < 1 or valorY > 18):
        print("Posição inválida. Por favor, digite valores entre 1 e 18.")
    
#finalizar script






# def exercicio4():
    #Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui

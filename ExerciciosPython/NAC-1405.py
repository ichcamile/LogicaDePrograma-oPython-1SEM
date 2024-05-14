def exercicio01():

    def calculo():
    #Desenvolva um programa que realize cálculos simples, como a soma, subtração, multiplicação e divisão de dois números inseridos pelo usuário.

        resposta = input("Olá usuário, qual calculo você deseja fazer? (ATENÇÃO! RESPONDA COM O NUMERO CORRESPONDENTE \n 1-Soma \n 2-Subtração \n 3- Divisão \n 4 - Multiplicação ")

        if (resposta == "1"):
            num1 = int(input("Escolha o número a ser somado: "))
            num2 = int(input("Escolha o outro número a ser somado: "))
            resultado = num1 + num2 
            print(f"O resultado da soma é {resultado}")
        elif (resposta == "2"):
            num1 = int(input("Escolha o número a ser subtraído: "))
            num2 = int(input("Escolha o número a subtrair: "))
            resultado = num1 - num2 
            print(f"O resultado da subtração é {resultado}")
        elif (resposta == "3"):
            num1 = int(input("Escolha o número a ser dividido: "))
            num2 = int(input("Escolha o número pelo qual será dividido: "))
            resultado = num1 / num2 
            print(f"O resultado da divisão é {resultado}")
        elif (resposta == "4"):
            num1 = int(input("Escolha o número a ser multiplicado: "))
            num2 = int(input("Escolha o número pelo qual será multiplicado: "))
            resultado = num1 * num2 
            print(f"O resultado da multiplicação é {resultado} ")
        else:
            print("Código errado!! Insira um válido ")
            validacaoResposta()

    
    def validacaoResposta():
            resposta = input("Você deseja tentar novamente SIM ou NAO ")
            if (resposta == "Sim "):
                 calculo()
            else: 
                print("Encerrando a função...")
                return
    calculo()
                

def exercicio02():
     #Implemente um programa que utilize estruturas de decisões (if, else, elif) para determinar se um número inserido pelo usuário é positivo, negativo ou zero. Utilize também loops para pedir novos números até que o usuário insira zero.
    
    print("Olá, seja bem vindo ao seu validador de números!")

    resposta = input("Insira um número para começar a verifição:  ")
    
    if (resposta > 0):
        print("O número inserido é maior que zero, logo, positivo!!")
    elif(resposta < 0):
        print("O número inserido é menor que zero, logo, negativo!!")
    elif(resposta == 0):
        print("O número inserido é Zero")
    else: 
        while True:
            alternativa = input("Insira um número válido, caso queira sair do verificador, digite 0: ")
            try:
                alternativa = float(alternativa)
                if alternativa == 0:
                    print("Saindo do verificador.")
                    break

                if alternativa > 0:
                    print("O número inserido é maior que zero, logo, positivo!")
                elif alternativa < 0:
                    print("O número inserido é menor que zero, logo, negativo!")
                else:
                    print("O número inserido é zero")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")



def exercicio03():
    #Crie uma função que receba dois números como parâmetros e retorne a soma deles. Em seguida, solicite ao usuário que entre com os 2 números, chame a função e imprima o resultado na tela.
    def somaNumeros(num1, num2):
        return num1 + num2

    def main():
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        resultado = somaNumeros(num1, num2)
        
        print(f" A soma de {num1} e {num2},  {resultado}" )

def exercicio04():
    listaDeAlunos = []

    for i in range (0,5):
        alunos = input(f"Insira o nome do aluno {1+i}")
        listaDeAlunos.append(alunos)
    print (f"Essa é a sua lista atual de alunos,{listaDeAlunos}")
    
    indice = int(input("Digite o indice do aluno que deseja remover!"))
    
    if indice >= 0 or  indice < len(listaDeAlunos):
        del listaDeAlunos[indice]
        print(f"Essa é a sua lista atual de alunos, {listaDeAlunos}")
    else:
        print("Índice fora do intervalo da lista.")


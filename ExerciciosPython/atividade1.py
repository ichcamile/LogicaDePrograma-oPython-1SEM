n1 = float(input("Entre com a n1"))
n2 = float(input("Entre com a n2"))

media = (n1+n2)/3

print("A média deste aluno foi", media)

if(media < 3):
    print("REPROVADO")
elif(media< 6):
    print("RECUPERAÇÃO")
else:
    print("APROVADO")

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

# Solicita ao usuário que insira os valores dos três produtos
produto1 = float(input("Digite o valor do primeiro produto: "))
produto2 = float(input("Digite o valor do segundo produto: "))
produto3 = float(input("Digite o valor do terceiro produto: "))

# Determina qual produto tem o menor valor e imprime a mensagem apropriada
if produto1 <= produto2 and produto1 <= produto3:
    print("Você deve comprar o primeiro produto, cujo valor é R$", produto1)
elif produto2 <= produto1 and produto2 <= produto3:
    print("Você deve comprar o segundo produto, cujo valor é R$", produto2)
else:
    print("Você deve comprar o terceiro produto, cujo valor é R$", produto3)
#Faça um Programa que leia três números e mostre o maior deles.

# Solicita ao usuário que insira o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número
num2 = float(input("Digite o segundo número: "))

# Solicita ao usuário que insira o terceiro número
num3 = float(input("Digite o terceiro número: "))

# Encontra o maior número entre os três usando a função max()
maior = max(num1, num2, num3)

# Imprime o maior número encontrado
print("O maior número é", maior)
#Faça um Programa que leia três números e mostre o maior e o menor deles.

# Solicita ao usuário que insira o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número
num2 = float(input("Digite o segundo número: "))

# Solicita ao usuário que insira o terceiro número
num3 = float(input("Digite o terceiro número: "))

# Encontra o menor número entre os três usando a função min()
menor = min(num1, num2, num3)

# Imprime o menor número encontrado
print("O menor número é", menor)
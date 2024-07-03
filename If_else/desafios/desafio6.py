#Faça um Programa que leia três números e mostre-os em ordem decrescente.

# Solicita ao usuário que insira três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Coloca os números em uma lista
numeros = [num1, num2, num3]

# Ordena a lista em ordem decrescente
numeros_ordenados = sorted(numeros, reverse=True)

# Imprime os números em ordem decrescente
print("Os números em ordem decrescente são:", numeros_ordenados[0], numeros_ordenados[1], numeros_ordenados[2])
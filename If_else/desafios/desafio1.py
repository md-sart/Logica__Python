#Faça um Programa que peça dois números e imprima o maior deles

# Solicita ao usuário que insira o primeiro número e converte a entrada para um número de ponto flutuante
numero1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número e converte a entrada para um número de ponto flutuante
numero2 = float(input("Digite o segundo número: "))

# Verifica se o primeiro número é maior que o segundo número
if numero1 > numero2:
    # Se o primeiro número for maior, imprime que o maior número é o primeiro número
    print("O maior número é", numero1)
# Verifica se o segundo número é maior que o primeiro número
elif numero2 > numero1:
    # Se o segundo número for maior, imprime que o maior número é o segundo número
    print("O maior número é", numero2)
# Caso os dois números sejam iguais (adicional para cobrir todos os casos)
else:
    # Se os dois números forem iguais, imprime que ambos são iguais
    print("Os números são iguais")
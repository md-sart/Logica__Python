#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo

# Solicita ao usuário que insira um valor e converte a entrada para um número de ponto flutuante
valor = float(input("Digite o valor: "))

# Verifica se o valor é maior ou igual a 0
if valor >= 0:
    # Se o valor for maior ou igual a 0, imprime que o valor é positivo
    print("O valor", valor, "é positivo")
# Caso o valor seja menor que 0
elif valor < 0:
    # Se o valor for menor que 0, imprime que o valor é negativo
    print("O valor", valor, "é negativo")

# Exercício 3

#Faça um programa que calcule e apresente o fatorial de um número inteiro e natural fornecido pelo usuário.

#Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120.
#Por definição 0! = 1.

# Solicita ao usuário que insira um número inteiro e natural e o armazena na variável 'numero'
numero = int(input("Digite um número inteiro e natural: "))

# Verifica se o número digitado é igual a zero
if numero == 0:
    # Se for igual a zero, imprime o fatorial de zero, que é 1
    print("0! = 1")
else:
    # Se o número for diferente de zero, inicializa a variável 'resultado' com 1
    resultado = 1

    # Loop para calcular o fatorial do número
    for i in range(1, numero + 1):
        resultado *= i  # Multiplica 'resultado' pelo valor de 'i' em cada iteração

    # Imprime o resultado do fatorial do número digitado
    print("O fatorial de", numero, "é", resultado)
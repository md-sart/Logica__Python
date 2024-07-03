# **While** e **For** Loops

#Instruções `while` e `for` permitem implementar *laços* de execução nos programas, os chamados *loops* \*. São blocos de instruções que se repetem até satisfazer alguma condição com chegar a um determinado valor ou índice.

#Os *loops* são muito úteis para codificar situações repetitivas sem a necessidade de extensas linhas de código que se repetem.

#\* *não confunda, às vezes também empregamos o têrmo 'loop' para quando um programa, geralmente por erro, 'não para'.*

# Exercício 1

#Escreva um programa que apresente todos os ímpares de 1 até 99.


# Loop de 1 a 99 (exclusivo)
for i in range(1, 100):
    # Verifica se o número é ímpar (resto da divisão por 2 não é zero)
    if i % 2 != 0:
        # Se for ímpar, imprime o número
        print(i)

# Exercício 2

#Escreva um programa que apresente os n (1 <= n <= 20) primeiros termos da seguinte sequência: 1, 4, 9, 16, 25, ...

# Loop de 1 a 20 (inclusive)
for i in range(1, 21):
    # Eleva o número atual ao quadrado usando ** e armazena o resultado na variável 'n'
    n = i ** 2
    # Imprime o resultado
    print(n)

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

# Exercício 4
#A conversão de graus Fahrenheit para Celsius é obtida pela fórmula:
#$$𝐶 = \frac{5}{9}(𝐹 − 32)$$

#Escreva um programa que calcule e apresente uma tabela de graus Celsius em função de graus Fahrenheit que variem de 50 a 150, de 1 em 1.

# Loop de 50 a 150 (inclusive) para valores de Fahrenheit
for fahrenheit in range(50, 151):
    # Fórmula de conversão de Fahrenheit para Celsius
    celsius = (5/9) * (fahrenheit - 32)
    # Imprime os valores de Fahrenheit e Celsius formatados com 2 casas decimais
    print(f"Fahrenheit: {fahrenheit}, Celsius: {celsius:.2f}")

# Exercício 5 RESOLVIDO
#Elabore um programa que calcule e apresente o valor de S, dado por:
#$$𝑆 = \frac{1}{N} + \frac{2}{N-1} + \frac{3}{N-2} + ... + \frac{N-1}{2} + N$$
#Sendo N fornecido pelo usuário.


# Solicita ao usuário que insira o valor de 'n' e converte para inteiro
n = int(input("Digite o valor de n: "))

# Inicializa a variável 'S' para armazenar a soma
S = 0

# Inicializa a variável 'denominador' com o valor de 'n'
denominador = n

# Loop de 1 até 'n'
for i in range(1, n + 1, 1):
    # Imprime o termo atual da série
    print("termo", i, "=", i, "/", denominador)

    # Calcula o valor do termo atual e adiciona à soma
    S = S + i / denominador

    # Decrementa o denominador para o próximo termo
    denominador = denominador - 1

# Imprime a soma com duas casas decimais
print("\nA soma é", "%.2f" % S)
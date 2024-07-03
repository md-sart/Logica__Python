#Escreva um programa que apresente os n (1 <= n <= 20) primeiros termos da seguinte sequência: 1, 4, 9, 16, 25, ...

# Loop de 1 a 20 (inclusive)
for i in range(1, 21):
    # Eleva o número atual ao quadrado usando ** e armazena o resultado na variável 'n'
    n = i ** 2
    # Imprime o resultado
    print(n)

# Exercício 4

#Escreva um programa que calcule e apresente uma tabela de graus Celsius em função de graus Fahrenheit que variem de 50 a 150, de 1 em 1.

# Loop de 50 a 150 (inclusive) para valores de Fahrenheit
for fahrenheit in range(50, 151):
    # Fórmula de conversão de Fahrenheit para Celsius
    celsius = (5/9) * (fahrenheit - 32)
    # Imprime os valores de Fahrenheit e Celsius formatados com 2 casas decimais
    print(f"Fahrenheit: {fahrenheit}, Celsius: {celsius:.2f}")
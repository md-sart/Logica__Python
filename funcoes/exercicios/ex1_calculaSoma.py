#Faça um programa, utilizando funções, que receba três números inteiros e positivos, e que forneça a soma desses três números.

    #Para este exercício crie três funções:

        #entrada() retorna um número digitado (fazer a verificação se é positivo);
        #calculaSoma(a, b, c) recebe 3 números inteiros e positivos e retorna a soma deles;
        #main() chamada das funções criadas (chama 3 vezes a entrada, sendo uma para cada número e a função para somar) e depois mostre o resultado.

# Função para receber uma entrada do usuário e verificar se é um número positivo.
def entrada():
    valor = int(input('Digite um valor: '))  # Solicita ao usuário que digite um valor.
    if valor <= 0:  # Verifica se o valor é menor ou igual a zero.
        print('Digite um número positivo!')  # Se o valor for menor ou igual a zero, imprime uma mensagem de erro.
    else:
        return valor  # Se o valor for positivo, retorna o valor.

# Função para calcular a soma de três valores.
def calculaSoma(a, b, c):
    return a + b + c  # Retorna a soma dos três valores.

# Função principal que chama as outras funções para executar o algoritmo.
def main():
    print('Digite três valores')  # Solicita ao usuário que digite três valores.
    valor1 = entrada()  # Chama a função entrada para obter o primeiro valor.
    valor2 = entrada()  # Chama a função entrada para obter o segundo valor.
    valor3 = entrada()  # Chama a função entrada para obter o terceiro valor.

    # Chama a função calculaSoma para calcular a soma dos três valores.
    soma = calculaSoma(valor1, valor2, valor3)
    print('A soma dos três valores é:', soma)  # Imprime o resultado da soma dos três valores.

main()  # Chama a função principal para iniciar a execução do programa.
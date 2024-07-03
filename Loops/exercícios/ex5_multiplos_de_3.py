multiplos_de_3 = []  # Inicializa uma lista vazia para armazenar os múltiplos de 3.

for i in range(1, 11): # Loop de 1 a 10, ou seja, para os 10 primeiros números inteiros positivos.
    multiplo = 3 * i # Calcula o múltiplo de 3 multiplicando cada número do loop por 3.
    multiplos_de_3.append(multiplo) #adiciona os valores da variavel multiplo na lista vazia

print("Os 10 primeiros múltiplos de 3 são:", multiplos_de_3) #imprime o resuktado

#eu poderia utilizar % pra ter um resultado mais exato
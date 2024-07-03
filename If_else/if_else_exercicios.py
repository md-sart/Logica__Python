

# AULA 03_ If-Then-Else _EXERCICIOS

# Exercício 1.

#Faça um programa que leia um número inteiro (e diferente de zero) e mostre
#uma mensagem indicando se este número é positivo ou negativo.


# Solicita ao usuário que insira um número inteiro e o converte para inteiro
n1 = int(input('Digite um número:'))

# Verifica se o número inserido é maior ou igual a 1
if n1 >= 1:
    # Se for maior ou igual a 1, imprime que é um número positivo
    print('O número', n1, 'é um número positivo!')

# Verifica se o número inserido é menor ou igual a -1
elif n1 <= -1:
    # Se for menor ou igual a -1, imprime que é um número negativo
    print('O número', n1, 'é um número negativo!')

# Se as condições anteriores não forem satisfeitas, o número é inválido
else:
    print('Digite um número válido!')

# Exercício 2

#Faça um programa que apresenta o maior de dois números inteiros (diferentes) lidos do usuário.


# Solicita ao usuário que insira o primeiro número inteiro e o converte para inteiro
n1 = int(input('Entre com o primeiro número: '))

# Solicita ao usuário que insira o segundo número inteiro e o converte para inteiro
n2 = int(input('Entre com o segundo número: '))

# Verifica se o primeiro número (n1) é maior que o segundo número (n2)
if (n1 > n2):
    # Se n1 for maior que n2, imprime que n1 é maior que n2
    print(n1 , ' é maior que ' , n2)
else:
    # Se n2 for maior que ou igual a n1, imprime que n2 é maior que ou igual a n1
    print(n2 , ' é maior que ' , n1)

# Exercício 3

#Faça um programa que coloque dois nomes em ordem alfabética.


# Define uma função chamada ordenar_nomes que recebe dois nomes como argumentos
def ordenar_nomes(nome1, nome2):
    # Converte os nomes para minúsculas para garantir que a comparação seja feita sem diferenciar maiúsculas de minúsculas
    nome1 = nome1.lower()
    nome2 = nome2.lower()

    # Compara os nomes e os retorna em ordem alfabética
    if nome1 < nome2:
        return nome1, nome2
    else:
        return nome2, nome1

# Solicita ao usuário que insira o primeiro nome
nome1 = input("Digite o primeiro nome: ")

# Solicita ao usuário que insira o segundo nome
nome2 = input("Digite o segundo nome: ")

# Chama a função ordenar_nomes com os nomes inseridos e armazena os resultados
nome_ordenado1, nome_ordenado2 = ordenar_nomes(nome1, nome2)

# Imprime os nomes inseridos pelo usuário na ordem em que foram inseridos e em ordem alfabética
print("1.", nome1, "2.", nome2)

"""# Exercício 4.

Faça um programa que apresente se o número que o usuário digitou é divisível
por 3 e por 5 ao mesmo tempo.

"""

# Solicita ao usuário que insira um número inteiro e o converte para inteiro
numero = int(input("Digite um número: "))

# Verifica se o número inserido é divisível por 3 e por 5 ao mesmo tempo
if numero % 3 == 0 and numero % 5 == 0:
    # Se for divisível por ambos, imprime que o número é divisível por 3 e por 5 ao mesmo tempo
    print(numero, "é divisível por 3 e por 5 ao mesmo tempo!")
else:
    # Se não for divisível por ambos, imprime que o número não é divisível por 3 e por 5 ao mesmo tempo
    print(numero, "não é divisível por 3 e por 5 ao mesmo tempo!")

"""# Exercício 5.

Elabore um programa que leia do teclado o sexo de uma pessoa. Se o sexo
digitado for "M" ou "m" ou "F" ou "f", escrever na tela "Sexo válido! ". Caso contrário,
exibir "Sexo inválido! ".
"""

# Solicita ao usuário que insira seu sexo e converte a entrada para maiúsculas
sexo = input('Digite seu sexo: ').upper()

# Verifica se o sexo é igual a 'M' ou 'F'
if sexo == 'M' or sexo == 'F':
    print('Sexo válido!')
else:
    print('Sexo inválido!')
#Faça um programa que leia uma lista de 5 números inteiros e mostre-os.

    #a. Sem função
    #b. Com função e variável global
    #c. Com função, sem variável global (a função retorna uma lista)
    
# Lista definida sem função.
lista1 = [1, 2, 3, 4, 5]

# Imprime a lista1.
lista1

# Função definida para exibir uma lista passada como argumento.
def exibeLista2(x):
  print(x)

# Lista definida fora da função.
lista2 = [1, 2, 3, 4, 5]

# Chamada da função passando lista2 como argumento.
exibeLista2(lista2)

# Função definida para exibir uma lista, mas sem argumentos.
# A lista é definida dentro da função e não acessível fora dela.
def exibeLista3():
  lista3 = [1, 2, 3, 4, 5]
  print (lista3)

# Chamada da função que exibe lista3.
exibeLista3()
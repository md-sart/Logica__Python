#Faça um programa que leia uma lista de 10 números inteiros e mostre-os na ordem inversa da digitação.

    #a. Sem função
    #b. Com função e variável global
    #c. Com função, sem variável global (a função retorna uma lista)
    
# Lista definida e invertida sem o uso de função.
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista1.reverse()  # Inverte a ordem da lista.
print(lista1)  # Imprime a lista invertida.

# Função definida para inverter uma lista e imprimir seu resultado.
# Esta função utiliza uma variável global (lista2).
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def inverso(lista):
  lista.reverse()  # Inverte a ordem da lista passada como argumento.
  print(lista)  # Imprime a lista invertida.

inverso(lista2)  # Chamada da função inverso passando lista2 como argumento.

# Função definida para inverter uma lista e retorná-la.
# Esta função não utiliza variáveis globais.
def exibeLista3():
  lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  lista3.reverse()  # Inverte a ordem da lista dentro da função.
  print(lista3)  # Imprime a lista invertida.

exibeLista3()  # Chamada da função exibeLista3.

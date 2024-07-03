#Faça um programa que leia uma lista com 4 notas (entre 0 e 10), mostre as notas e a média na tela.
#(Você pore implementar apenas uma das alternativas abaixo, mas tenha certeza de saber implementar de todas as formas alternativas)

    #a. Sem função
    #b. Com função e variável global
    #c. Com função, sem variável global (a função retorna uma lista)
    
    
# Lista de notas definida.
notas = [10, 3, 8, 7]

# Calcula a média das notas.
soma = sum(notas)  # Calcula a soma das notas.
quantidade = len(notas)  # Obtém a quantidade de notas.
media = soma / quantidade  # Calcula a média das notas.

# Imprime as notas e a média.
print("Notas:", notas)
print("Média:", media)

# Lista de notas redefinida.
notas = [10, 3, 8, 7]

# Função definida para calcular a média de uma lista de notas.
# A variável soma, quantidade e media são definidas dentro da função.
def media(x):
  soma = sum(x)  # Calcula a soma das notas passadas como argumento.
  quantidade = len(x)  # Obtém a quantidade de notas passadas como argumento.
  media = soma / quantidade  # Calcula a média das notas.
  return media  # Retorna a média.

# Imprime as notas e chama a função para calcular a média.
print("Notas:", notas)
media(notas)

# Função definida para calcular a média de uma lista de notas.
# As notas são definidas dentro da função e a função retorna a média.
def media():
  notas = [10, 3, 8, 7]  # Lista de notas definida dentro da função.
  soma = sum(notas)  # Calcula a soma das notas.
  quantidade = len(notas)  # Obtém a quantidade de notas.
  media = soma / quantidade  # Calcula a média das notas.
  return media  # Retorna a média.

media()  # Chama a função para calcular a média.

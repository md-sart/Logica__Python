#Faça um programa, utilizando funções, que retorne o valor de um produto já com o imposto. Serão utilizados dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
#Para este exercício crie três funções:

    #entrada() serve para retornar tanto o custo do produto quanto a porcentagem do imposto;
    #somaImposto(porc, custo) recebe o valor da porcentagem do imposto e o custo do produto. Retorna o novo custo do produto já com o imposto.
    #main() chamada das funções criadas (chama 2 vezes a entrada e 1 vez a função somaImposto) e depois mostre o custo com o imposto.
    

# Função para receber o custo do produto e a taxa do imposto do usuário.
def entrada():
    custo = float(input('Digite o custo do produto: '))  # Solicita ao usuário que digite o custo do produto.
    porc = float(input('Digite a taxa do imposto: '))  # Solicita ao usuário que digite a taxa do imposto.
    return custo, porc  # Retorna o custo e a taxa do imposto.

# Função para calcular o valor total do produto com o imposto.
def somaImposto(porc, custo):
    valorTotal = custo + (custo * (porc / 100))  # Calcula o valor total com o imposto.
    return valorTotal  # Retorna o valor total com o imposto.

# Função principal que chama as outras funções para calcular o valor total do produto com o imposto e imprimir o resultado.
def main():
    custo, porc = entrada()  # Chama a função entrada para obter o custo do produto e a taxa do imposto.
    valorTotal = somaImposto(porc, custo)  # Chama a função somaImposto para calcular o valor total com o imposto.
    print('O valor do seu produto com imposto é: R$', valorTotal)  # Imprime o valor total com o imposto.

main()  # Chama a função principal para iniciar a execução do programa.
  
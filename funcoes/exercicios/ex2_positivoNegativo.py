#Faça um programa, utilizando funções, que terá um número inteiro como entrada e a função retornará o caractere "P", se o número for positivo (> 0), "N", se o número for negativo (< 0) e "Zero" se o número for igual a zero.

    #Para este exercício crie duas funções:
    #verifica(a) recebe o número e retorna "P" (> 0), "N" (< 0) ou "Zero" (igual a 0).
    #main() digita um número, faz a chamada à função verifica e depois mostra o resultado.
 
# Definição da função verifica para determinar se um número é zero, positivo ou negativo.
def verifica(a):
  if a == 0:
    print("Zero")  # Se o número for zero, imprime "Zero".
  elif a > 0:
    print("P - Positivo")  # Se o número for maior que zero, imprime "P - Positivo".
  elif a < 0:
    print("N - Negativo")  # Se o número for menor que zero, imprime "N - Negativo".

# Função principal para receber um número do usuário e chamar a função verifica.
def main():
    num = int(input("Digite um número "))  # Solicita ao usuário que digite um número.
    verifica(num)  # Chama a função verifica para determinar se o número é zero, positivo ou negativo.

main()  # Chama a função principal para iniciar a execução do programa.    
    
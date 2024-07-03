#Escreva um programa modularizado que permite ao usuário converter uma faixa de temperatura de Fahrenheit para Celsius (para isso o usuário deve digitar F) e de Celsius para Fahrenheit (neste caso o usuário deve digitar C).
#Para a construção do programa você deve escrever as seguintes funções:

    #exibeMsg() apenas exibe uma mensagem para ao usuário dizendo o que o programa faz e informando como deve ser a entrada de dados. Não tem parâmetro de entrada e não tem retorno;
    #verificaOpcao() a função não tem parâmetro de entrada e retorna “F” ou “C” (fazer a validação para que o usuário só digite F ou C);
    #verificaIntervalo() a função não tem parâmetro de entrada e retorna os valores inicial e final do intervalo (fazer a validação para que o valor inicial seja menor que o valor final);
    #exibeFahrenheitToCelsius(inicio, fim) essa função recebe como entrada o intervalo de temperatura a ser exibido, faz a conversão de temperatura e mostra a temperatura convertida para Celsius;
    #exibeCelsiusToFahrenheit(inicio, fim) essa função recebe como entrada o intervalo de temperatura a ser exibido, faz a conversão de temperatura e mostra a temperatura convertida para Fahrenheit
    
# Função para exibir uma mensagem de boas-vindas e instruções sobre o programa.
def exibeMsg():
  print("Bem-vindo ao programa de conversão de graus. Escolha um intervalo e digite F para converter para Fahrenheit, e C para converter para Celsius")

# Função para verificar se a opção digitada pelo usuário é válida ('F' para Fahrenheit ou 'C' para Celsius).
def verificaOpcao():
    while True:
        opcao = input("Digite 'F' para Fahrenheit ou 'C' para Celsius: ").upper()  # Converte a entrada para maiúsculas
        if opcao == 'F' or opcao == 'C':
            return opcao
        else:
            print("Por favor, digite apenas 'F' ou 'C'.")

# Função para verificar se o intervalo de valores inicial e final é válido.
def verificaIntervalo():
    while True:
        try:
            inicio = float(input("Digite o valor inicial do intervalo: "))
            fim = float(input("Digite o valor final do intervalo: "))
            if inicio < fim:
                return inicio, fim
            else:
                print("O valor inicial deve ser menor que o valor final.")
        except ValueError:
            print("Por favor, digite números válidos para os valores inicial e final.")

# Função para converter e exibir os valores de Fahrenheit para Celsius dentro do intervalo especificado.
def exibeFahrenheitToCelsius(inicio, fim):
    print("\nFahrenheit para Celsius:")
    for fahrenheit in range(int(inicio), int(fim) + 1):
        celsius = (5/9) * (fahrenheit - 32)
        print(f"Fahrenheit: {fahrenheit}, Celsius: {celsius:.2f}")

# Função para converter e exibir os valores de Celsius para Fahrenheit dentro do intervalo especificado.
def exibeCelsiusToFahrenheit(inicio, fim):
    print("\nCelsius para Fahrenheit:")
    for celsius in range(int(inicio), int(fim) + 1):
        fahrenheit = (celsius * 9/5) + 32
        print(f"Celsius: {celsius}, Fahrenheit: {fahrenheit:.2f}")

# Função principal para chamar as outras funções e executar o programa.
def main ():
    exibeMsg()  # Exibe a mensagem de boas-vindas e instruções.
    opcao = verificaOpcao()  # Verifica se a opção digitada é válida.
    inicio, fim = verificaIntervalo()  # Verifica se o intervalo digitado é válido.

    if opcao == 'F':
        exibeFahrenheitToCelsius(inicio, fim)  # Converte e exibe os valores de Fahrenheit para Celsius.
    elif opcao == 'C':
        exibeCelsiusToFahrenheit(inicio, fim)  # Converte e exibe os valores de Celsius para Fahrenheit.
    else:
        print("Opção inválida. Por favor, digite apenas 'F' ou 'C'.")

main()  # Chama a função principal para iniciar a execução do programa.
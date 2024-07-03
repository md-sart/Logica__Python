# Inicializa uma lista vazia para armazenar os números do loop
Loop = []

# Solicita ao usuário que insira um número inteiro e o converte para inteiro
i = int(input('Entre com um inteiro positivo entre 0 e 20 (ou um negativo para sair): '))

# Verifica se o número inserido é maior que 20
if i > 20:
    print('Digite um número entre 1 e 20')

# Verifica se o número inserido está entre 1 e 20 (inclusive)
elif i <= 20 and i > 0:
    # Enquanto 'i' for menor ou igual a 20, o loop continuará
    while i <= 20:
        # Adiciona o valor de 'i' à lista 'Loop'
        Loop.append(i)
        # Imprime o valor de 'i'
        print(i)
        # Incrementa 'i' para o próximo número
        i += 1
    # Encontra o maior número na lista 'Loop' usando a função max()
    maior = max(Loop)
    # Imprime o maior número encontrado
    print('O maior numero desta sequência é:', maior)
    # Encontra o menor número na lista 'Loop' usando a função min()
    menor = min(Loop)
    # Imprime o menor número encontrado
    print('O menor numero desta sequência é:', menor)

# Se o número inserido for negativo, o programa é encerrado
elif i < 0:
    print('Encerrando o programa...')
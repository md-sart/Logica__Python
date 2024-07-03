#Faça um Programa que peça para entrar com um ano com 4 dígitos e determine se o mesmo é ou não bissexto.

# Loop infinito para solicitar um ano com 4 dígitos do usuário até uma entrada válida ser fornecida
while True:
    # Solicita ao usuário que insira um ano
    ano = input("Digite um ano com 4 dígitos: ")

    # Verifica se a entrada tem exatamente 4 dígitos e se todos os caracteres são dígitos
    if len(ano) == 4 and ano.isdigit():
        # Converte a entrada para um número inteiro
        ano = int(ano)
        # Sai do loop se a entrada for válida
        break
    else:
        # Imprime uma mensagem de erro se a entrada for inválida
        print("Ano inválido. Por favor, insira um ano com 4 dígitos.")

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    # Se o ano for bissexto, imprime uma mensagem correspondente
    print("O ano", ano, "é bissexto")
else:
    # Se o ano não for bissexto, imprime uma mensagem correspondente
    print("O ano", ano, "não é bissexto")

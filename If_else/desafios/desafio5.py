#Faça um Programa que verifique se uma letra digitada é vogal ou consoante

while True:
    # Solicita ao usuário que insira uma letra e converte a entrada para maiúsculas
    letra = input("Digite uma letra e descubra se ela é vogal ou consoante: ").upper()

    # Verifica se a entrada tem exatamente um caractere
    if len(letra) == 1 and letra.isalpha():
        break
    else:
        # Imprime uma mensagem de erro se a entrada for inválida
        print("Valor inválido. Por favor, insira apenas uma letra.")

# Verifica se a letra está no conjunto de vogais
if letra in "AEIOU":
    # Se a letra for uma vogal, imprime uma mensagem correspondente
    print("A letra", letra, "é uma vogal")
else:
    # Se a letra não for uma vogal, imprime uma mensagem correspondente
    print("A letra", letra, "é uma consoante")

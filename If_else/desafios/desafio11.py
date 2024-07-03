#Faça um Programa que pergunte em que turno você estuda. Peça para digitar
    #M-matutino
    #V-Vespertino
    #N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# Solicita ao usuário que insira o turno e converte a entrada para maiúsculas
turno = input("Digite o turno que você estuda (M-matutino, V-Vespertino, N-Noturno): ").upper()

# Verifica o turno e imprime uma mensagem correspondente
if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Turno inválido")

#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

#"F" - Feminino,
#"M" - Masculino,
#Caso contrário, 'Sexo Inválido'.

# Solicita ao usuário que insira seu sexo e converte a entrada para maiúsculas
sexo = input("Digite o seu sexo F ou M: ").upper()

# Verifica se o sexo é igual a "F"
if sexo == "F":
    # Se o sexo for "F", imprime que o sexo é Feminino
    print("O seu sexo é", sexo, "- Feminino")
# Verifica se o sexo é igual a "M"
elif sexo == "M":
    # Se o sexo for "M", imprime que o sexo é Masculino
    print("O seu sexo é", sexo, "- Masculino")
# Se o sexo não for nem "F" nem "M"
else:
    # Imprime que o sexo é inválido
    print("Sexo inválido")
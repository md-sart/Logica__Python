#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

    #salários até R$ 280,00 (incluindo): aumento de 20%
    #salários de R$ 280,00 a 700,00 (incluindo) : aumento de 15%
    #salários de R$ 700,00 e 1500,00 (incluindo): aumento de 10%
    #salários de R$ 1500,00 em diante : aumento de 5%
    #Após o aumento ser realizado, informe na tela:

#salário antes do reajuste;
#percentual de aumento aplicado;
#valor do aumento;
#novo salário, após o aumento.


# Solicita ao usuário que insira o salário do colaborador e converte para ponto flutuante
salario = float(input("Digite o salário do colaborador: "))

# Determina o percentual de aumento com base no salário atual
if salario <= 280:
    percentual_aumento = 20
elif salario <= 700:
    percentual_aumento = 15
elif salario <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

# Calcula o valor do aumento e o novo salário
valor_aumento = salario * (percentual_aumento / 100)
novo_salario = salario + valor_aumento

# Imprime os resultados
print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")

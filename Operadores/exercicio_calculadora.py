
print("\n******************* Bem vindo a Calculadora em Python *******************")

while True:
    try:
        num1 = float(input("Entre com o primeiro valor: "))
        break
    except ValueError:
        print("Por favor, insira um valor numérico.")

while True:
    try:
        num2 = float(input("Entre com o segundo valor: "))
        break
    except ValueError:
        print("Por favor, insira um valor numérico.")

while True:
    operacao = str(input("Agora, escolha entre as operações: +, -, / ou *: "))
    if operacao in ['+', '-', '/', '*']:
        break
    else:
        print("Por favor, digite um operador válido.")

def soma(x,y):
  resultado = x+y
  return(resultado)

def subtracao(x,y):
  resultado = x-y
  return(resultado)

def multi(x,y):
  resultado = x*y
  return(resultado)

def divisao(x,y):
  resultado = x/y
  return(resultado)

if operacao == "+":
    resultado = soma(num1, num2)
    print ("O resultado desta operação é: ", resultado)

elif operacao == "-":
    resultado = subtracao(num1, num2)
    print ("O resultado desta operação é: ", resultado)

elif operacao == "*":
    resultado = multi(num1, num2)
    print ("O resultado desta operação é: ", resultado)

elif operacao == "/":
    resultado = divisao(num1, num2)
    print ("O resultado desta operação é: ", resultado)
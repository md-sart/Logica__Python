
# Python

#Os programas aqui, exceto o último exercício  resolvido, têm uma estrutura sequencial, isto é, as instruções executam uma sequência seguida da outra.

# **Formas de retornar os resultados**

#1. Indicando unicamnente a variável;
#2. Utilizando o comando 'print'()'


#Para iniciar com os exemplos, primeiro devempos criar uma variável e um valor deve ser asignado

## neste caso a letera "a" é a nossa variavel a o valor de 30 ficará salvo na variável.
## letra 'b' separa a nossa segunda variavel, e o valor 48 sera salvo nela.

a = 30
b = 40

#podemos unicamente pedir para retornar o valor da variável indicando a mesma

a

#E o que acontece se temos várias variáveis para apresentar ao mesmo tempo?

#Perceba no resoltado que só o último valor será retornado, então, será necessário utilizar o commando 'print'

#a nossa primeira variável
a

#a nossa segunda variável
b

print (a)
print (b)

#Print

#A função ou comando print é empregada para exibir conteúdo de uma variável ou um comentário

#imprimindo / retomando o valor de um comentário [lembre-se que o comentário deve estar entre aspas , sejam simples]

print('Hello Folks!')

#Podemos também imprimir espaços com o intuito de que as mensagens ou resultados deixem uma linha entre as informações
print('')
print('---')
print('***')
print('')

#Comando type () identificando o tipo de variaveis. porem, é necessário utilizar em conjunto con o comando para que o resultado seja apresentado, vejamos:

#identificando o tipo de variável 'a
print ( type(a) )

#identificando o tipo de variavel 'b'
print (type(b))

#Tipos de variáveis

#1. int
#2. float
#3. string

#int

#Representam numeros inteiros, como 1,2, 3...

#Float

#Números de ponto flutuante, são utiliozados para representar numeros decimais, como 3.14, -2.5, etc

var = 3.1416  
print(type(var))

#string

#String (str): sao sequencias de caracteres, como "ola mundo". strings em python podem ser delimias por aspas simpes (") ou duplas ("")
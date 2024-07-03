
# Tipos numéricos

a = 123
b = 1.23
c = 1 + 2j #note j e não i
d = True

print('o valor de _a_ é', type(a))
print(type(b))
print(type(c))
print(type(d))

# Operadores de atribuição

a = 1
a += 3 #significa a= a+3
print(a) #4

# Operadores aritméticos
#Operadores aritméticos são usados com valores numéricos para realizar operações matemáticas

x = 10
y = 6
z = 6.0

print('x + y =', x+y)
print('x + y =', x-y)
print('x + y =', x*y)
print('x + y =', x/y)
print('x + y =', x/z)
print('x + y =', x//y) #resulta o numero inteiro
print('x + y =', x**y) #potência

# Operações de comparação
# Operadores de comparação são usados para comparar valores. Retornarão True ou False

x = 12
y = 3

print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)

# Operadores de identidade
#peradores de identidade são usados para comparar os objetos, não se são iguais, mas se eles forem realment o mesmo objeto com o mesmo local de memória
#**is** e **is not** são operadores de identidade em Python, eles são usados para checacar se os dois valores (ou variávei) estão localizaddos na mesma área de memória, duas variáveis iguais não significam que são idênticas!

x = 1
y = 1

print(x is y)
print(x is not y)

print(x == y)
print(x != y)

#Operadores de membros

a = [1,2,3]
b = 'Guilherme'

print(1 in a)
print("o" in b)

#IMPORTANTE: precedência de operadores

print(3+4)

#Fuções matemáticas, utilizando bibliotecas

import math

print(math.pi)
print(math.exp(1))
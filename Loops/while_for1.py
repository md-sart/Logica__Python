#Loops: while e for

i = 1
while i < 6:
  print ('Passando aqui...', i, '´ésima vez')
  i += 1              #> o mesmo que i = i + 1

#For

for i in [0, 1, 2, 3]:
    print('Passando aqui...', i , '-ésima vez')

#Break, contunue e while-else
#Verifique se realmente precisa disso
#Essas instruções em geral tornam o seu programa menos estruturados e podem

print('\n Break..................................... \n')
i = 1
while i < 6:
    print('Passando aqui...', i, "-ésima vez")
    if i == 3:
        print('E parando aqui...', i, 'ésima passada')
        break
    i += 1  
    
print('\n Continue..................................... \n')

i = 1
while i < 6:
    print('Passando aqui...', i, '-ésima vez')
    if i == 3:
        entrada = input('Entre com \'Yes\' se quiser continuar: ')
        if entrada.lower() == 'yes':
            i += 1  # Incrementa o valor de i para evitar loop infinito
            continue  # Continua para a próxima iteração do loop
        else:
            print('Parando aqui...', i, '-ésima passada')
            break
    i += 1 

print('\n While Else.........................\n')

i = int(input('Entre com um inteiro positivo:'))
while i < 6:
    print('Passando aqui...', i, '-ésima vez')
    i += 1
else:
    print('Entrada é maior ou igual a 6')

#Um uso bem prático

entrada = ''
while entrada.lower() != 'sim' and entrada.lower () != 'não':
  entrada = input('Você gosta de café? Entre com \'sim\' ou \'não\': ')

  print('Ah! Obrigado! Entendi, você ' + entrada.upper() + ' gosta de café!')


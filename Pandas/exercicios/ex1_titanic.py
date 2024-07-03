#Nos exercícios a seguir emprege a base de dados titanic. Todos exercícios possuem várias soluções possíveis, mas não se preocupe com isso. A melhor solução é primeiro, a que funciona para você!

#Qual a quantidade de linhas e colunas de titanic?
#Qual a idade do passageiro mais velho?
#Qual a idade da sobrevivente feminina mais velha?
#Analise a média de idade dos passageiros por classe e sexo (sugestão: empregue groupby). Você pode notar que?


import numpy as np # Importa a biblioteca NumPy, que fornece suporte para arrays e funções matemáticas.
import pandas as pd # Importa a biblioteca Pandas, que oferece estruturas de dados e ferramentas de análise.
import seaborn as sns # Importa a biblioteca Seaborn, que oferece ferramentas para visualização de dados estatísticos.
from random import choices # Importa a função 'choices' do módulo 'random', que gera amostras aleatórias com base em uma lista de opções ponderadas.


titanic = sns.load_dataset('titanic') # Carrega o conjunto de dados 'titanic' do repositório online do Seaborn.

# Obtém o número de linhas e colunas no DataFrame 'titanic' e armazena nos variáveis 'linhas' e 'colunas' respectivamente.
linhas, colunas = titanic.shape

# Imprime o número de linhas do DataFrame 'titanic'.
print("Número de linhas:", linhas)

# Imprime o número de colunas do DataFrame 'titanic'.
print("Número de colunas:", colunas)

# Obtém a idade máxima da coluna 'age' no DataFrame 'titanic' e armazena na variável 'mais_velho'.
mais_velho = titanic['age'].max()

# Imprime a mensagem informando a idade do passageiro mais velho, usando a variável 'mais_velho'.
print("A idade do passageiro mais velho é", mais_velho, "anos")

# Define a string 'sexo_feminino' para filtrar os dados do sexo feminino.
sexo_feminino = 'female'

# Define a string 'sobrevivente' para filtrar os dados de sobreviventes.
sobrevivente = 'yes'

# Aplica um filtro ao DataFrame 'titanic' para selecionar apenas as linhas que correspondem ao sexo feminino e que sobreviveram.
filtro = titanic[(titanic['sex'] == sexo_feminino) & (titanic['survived'] == 1)]

# Obtém a idade máxima da coluna 'age' no DataFrame filtrado e armazena na variável 'mais_velha'.
mais_velha = filtro['age'].max()

# Imprime a mensagem informando a idade da sobrevivente feminina mais velha.
print("A idade da sobrevivente feminina mais velha é:", mais_velha, "anos")

# Filtra o DataFrame 'titanic' para selecionar apenas as linhas que pertencem às classes 'First' e 'Third'.
classes_filtradas = titanic[titanic['class'].isin(['First', 'Third'])]

# Conta o número de sobreviventes por classe.
sobreviventes_por_classe = classes_filtradas[classes_filtradas['survived'] == 1]['class'].value_counts()

# Conta o número total de passageiros por classe.
total_por_classe = classes_filtradas['class'].value_counts()

# Calcula o percentual de sobreviventes em cada classe.
percentual_sobreviventes = (sobreviventes_por_classe / total_por_classe) * 100

# Obtém o percentual de sobreviventes na primeira classe, se existir, caso contrário, define como 0.
percentual_primeira_classe = percentual_sobreviventes['First'] if 'First' in percentual_sobreviventes else 0

# Obtém o percentual de sobreviventes na terceira classe, se existir, caso contrário, define como 0.
percentual_terceira_classe = percentual_sobreviventes['Third'] if 'Third' in percentual_sobreviventes else 0

# Imprime as informações sobre o percentual de sobreviventes em cada classe.
print(f"Percentual de sobreviventes na primeira classe foi de {percentual_primeira_classe:.2f}%\n"
      f"e o percentual de sobreviventes na terceira classe foi de {percentual_terceira_classe:.2f}%")

# Calcula a média da idade dos passageiros por classe e sexo, agrupando os dados e resetando os índices.
media_idade_por_classe_sexo = titanic.groupby(['class', 'sex'])['age'].mean().reset_index()

# Renomeia a coluna 'age' para 'média_idade'.
media_idade_por_classe_sexo.rename(columns={'age': 'média_idade'}, inplace=True)

# Imprime o cabeçalho informativo.
print("Média de idade dos passageiros por classe e sexo:")

# Imprime a tabela com a média de idade por classe e sexo.
print(media_idade_por_classe_sexo)

# Imprime a conclusão sobre a média de idade dos passageiros.
print("Podemos concluir que os passageiros mais velhos eram homens e estavam na primeira classe e as mais novas eram as mulheres da terceira classe. A média de idade dos passageiros diminui à medida que diminui a classe.")

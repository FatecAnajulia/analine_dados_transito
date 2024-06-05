import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Definindo o caminho do arquivo CSV
caminho_arquivo = '../dados/acidentes2023_completa.csv'

# Lendo o arquivo CSV, especificando o delimitador e ignorando linhas com problemas
dados = pd.read_csv(caminho_arquivo, delimiter=';', on_bad_lines='skip', encoding='ISO-8859-1')

# Acessando a coluna 'tipo_acidente'
tipo_acidente = dados['tipo_acidente']

# Contando a frequência de cada tipo de acidente no DataFrame
frequencia_tipos_acidente = tipo_acidente.value_counts()

# Calculando a porcentagem de cada tipo de acidente
porcentagem_tipos_acidente = (frequencia_tipos_acidente / frequencia_tipos_acidente.sum()) * 100

# Exibindo as porcentagens dos tipos de acidentes
print(porcentagem_tipos_acidente)

# Preparando os dados para a equação da reta
x = np.arange(len(frequencia_tipos_acidente))
y = porcentagem_tipos_acidente.values

# Calculando a inclinação (m) e o intercepto (b) da reta
m, b = np.polyfit(x, y, 1)

# Gerando valores de y para plotar a reta
y_reta = m * x + b

# Plotando os tipos de acidentes e a reta de tendência
plt.figure(figsize=(10, 5))
plt.bar(frequencia_tipos_acidente.index, y, label='Porcentagem de Acidentes por Tipo')
plt.plot(frequencia_tipos_acidente.index, y_reta, color='red', linestyle='--', label=f'Equação da reta: y = {m:.2f}x + {b:.2f}')
plt.xlabel('Tipo de Acidente')
plt.ylabel('Porcentagem de Acidentes')
plt.title('Porcentagem de Cada Tipo de Acidente no Ano')
plt.xticks(rotation=45, ha='right')  # Rotacionando os rótulos do eixo x para melhor visualização
plt.legend()
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Definindo o caminho do arquivo CSV
caminho_arquivo = '../dados/acidentes2023_completa.csv'

# Lendo o arquivo CSV, especificando o delimitador e ignorando linhas com problemas
dados = pd.read_csv(caminho_arquivo, delimiter=';', on_bad_lines='skip', encoding='ISO-8859-1')

# Acessando a coluna 'horario'
horario = dados['horario']

# Convertendo a coluna 'horario' para o tipo datetime
dados['horario'] = pd.to_datetime(dados['horario'], format='%H:%M:%S')

# Extraindo a hora do horário
dados['hora'] = dados['horario'].dt.hour

# Contando a frequência de acidentes por hora
frequencia_acidentes_por_hora = dados['hora'].value_counts()

# Ordenando as horas
frequencia_acidentes_por_hora = frequencia_acidentes_por_hora.sort_index()

# Calculando a porcentagem de acidentes por hora







porcentagem_acidentes_por_hora = (frequencia_acidentes_por_hora / frequencia_acidentes_por_hora.sum()) * 100

# Exibindo as porcentagens de acidentes por hora
print(porcentagem_acidentes_por_hora)

# Definindo os pontos para a equação da reta
x = frequencia_acidentes_por_hora.index
y = porcentagem_acidentes_por_hora.values

# Calculando a inclinação (m) e o intercepto (b) da reta
# descobre o coeficiente angular e o coeficiente linear da reta
m, b = np.polyfit(x, y, 1)

# Gerando valores de y para plotar a reta
y_reta = m * x + b

# Plotando a porcentagem de acidentes por hora e a reta
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='Porcentagem de Acidentes por Hora')
plt.plot(x, y_reta, 'r--', label=f'Equação da reta: y = {m:.2f}x + {b:.2f}')
plt.xlabel('Hora')
plt.ylabel('Porcentagem de Acidentes')
plt.title('Porcentagem de Acidentes por Hora')
plt.xticks(np.arange(0, 24, step=1))  
plt.legend()
plt.grid(True)
plt.show()

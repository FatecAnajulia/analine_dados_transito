import pandas as pd
import matplotlib.pyplot as plt

# Definindo o caminho do arquivo CSV
caminho_arquivo = '../dados/datatran2023_1trimestre.csv'

# Lendo o arquivo CSV, especificando o delimitador e ignorando linhas com problemas
dados = pd.read_csv(caminho_arquivo, delimiter=';', on_bad_lines='skip', encoding='latin1')

# Exibindo os nomes das colunas para verificar o nome correto da coluna desejada
# print(dados.columns)

# Acessando a coluna 'tipo_acidente' e 'data_inversa'
tipo_acidente = dados['tipo_acidente']
data_acidente = pd.to_datetime(dados['data_inversa'], dayfirst=True)

# Contando a frequência de acidentes por dia
frequencia_diaria = data_acidente.value_counts().sort_index()

# Definindo os pontos para a equação da reta
x1, y1 = frequencia_diaria.index[0].toordinal(), frequencia_diaria.iloc[0]
x2, y2 = frequencia_diaria.index[-1].toordinal(), frequencia_diaria.iloc[-1]

# Calculando a inclinação (m) e o intercepto (b) da reta
m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1

# Gerando valores de x para plotar a reta
x = [date.toordinal() for date in frequencia_diaria.index]
y = [m * xi + b for xi in x]

# Plotando a frequência de acidentes e a reta
plt.figure(figsize=(10, 5))
plt.plot(frequencia_diaria.index, frequencia_diaria.values, label='Frequência diária de acidentes')
plt.plot(frequencia_diaria.index, y, color='red', linestyle='--', label='Equação da reta (tendência)')
plt.xlabel('Data')
plt.ylabel('Número de Acidentes')
plt.title('Frequência de Acidentes ao Longo do Tempo')
plt.legend()
plt.grid(True)
plt.show()

# Contando a frequência de cada tipo de acidente no DataFrame
frequencia_tipos_acidente = tipo_acidente.value_counts()

# Calculando a porcentagem de cada tipo de acidente
porcentagem_tipos_acidente = (frequencia_tipos_acidente / frequencia_tipos_acidente.sum()) * 100

# Exibindo as porcentagens dos tipos de acidentes
print(porcentagem_tipos_acidente)

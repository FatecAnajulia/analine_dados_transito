import pandas as pd

# Definindo o caminho do arquivo CSV
caminho_arquivo = '../dados/datatran2023_1trimestre_teste.csv'

# Lendo o arquivo CSV, especificando o delimitador e ignorando linhas com problemas
dados = pd.read_csv(caminho_arquivo, delimiter=';', on_bad_lines='skip', encoding='latin1')

# Exibindo os nomes das colunas para verificar o nome correto da coluna desejada
print(dados.columns)

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

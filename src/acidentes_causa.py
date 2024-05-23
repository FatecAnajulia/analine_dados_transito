import pandas as pd

# Definindo o caminho do arquivo CSV
caminho_arquivo = '../dados/datatran2023_1trimestre_teste.csv'

# Lendo o arquivo CSV, especificando o delimitador e ignorando linhas com problemas
dados = pd.read_csv(caminho_arquivo, delimiter=';', on_bad_lines='skip', encoding='latin1')

# Exibindo os nomes das colunas para verificar o nome correto da coluna desejada
print(dados.columns)

# Acessando a coluna 'tipo_acidente'
tipo_acidente = dados['tipo_acidente']

# Contando a frequência de cada tipo de acidente no DataFrame
frequencia_tipos_acidente = tipo_acidente.value_counts()

# Calculando a porcentagem de cada tipo de acidente
porcentagem_tipos_acidente = (frequencia_tipos_acidente / frequencia_tipos_acidente.sum()) * 100

# Exibindo as porcentagens dos tipos de acidentes
print(porcentagem_tipos_acidente)

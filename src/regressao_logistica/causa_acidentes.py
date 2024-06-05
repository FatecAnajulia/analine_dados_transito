import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Carregar os dados do arquivo CSV fornecido pelo DETRAN
caminho_arquivo_csv = "../dados/datatran2023_1trimestre.csv"  # Substitua pelo caminho real do seu arquivo
dados_csv = pd.read_csv(caminho_arquivo_csv)

# Usaremos apenas o horário como feature
X = pd.get_dummies(dados_csv['horario'])
 
 
# Inicializar e treinar o modelo de regressão logística
modelo = LogisticRegression()
modelo.fit(X, dados_csv['horario'])
 
# Prever o horário do próximo acidente
proximo_acidente = pd.DataFrame({'horario': ['horario_previsto_do_proximo_acidente']})  # Substitua pelo horário previsto
horario_previsto = modelo.predict_proba(pd.get_dummies(proximo_acidente))
print("Probabilidade de cada horário para o próximo acidente:", horario_previsto)
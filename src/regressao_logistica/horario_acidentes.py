import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
 
# Carregar os dados do arquivo CSV fornecido pelo DETRAN
caminho_arquivo_csv = "../dados/datatran2023_1trimestre.csv"  # Substitua pelo caminho real do seu arquivo
dados_csv = pd.read_csv(caminho_arquivo_csv)
 
 
# Usaremos apenas as causas como features
X = pd.get_dummies(dados_csv['causas'])
 
 
# Inicializar e treinar o modelo de regressão logística
modelo = LogisticRegression()
modelo.fit(X, dados_csv['causas'])
 
# Prever a causa do próximo acidente
proximo_acidente = pd.DataFrame({'causas': ['causa_prevista_do_proximo_acidente']})  # Substitua pela causa prevista
causa_prevista = modelo.predict_proba(pd.get_dummies(proximo_acidente))
print("Probabilidade de cada causa para o próximo acidente:", causa_prevista)
from utils.avaliador import Avaliador
from utils.carregador import Carregador
from utils.ml_model import Model
from sklearn.preprocessing import StandardScaler



# Para Rodar, vá ao terminal e rode: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros
url_dados = "database/heart.csv"
colunas = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]

# Aplicando padronização nos dados de entrada
scaler = StandardScaler().fit(X)
X_scaled = scaler.transform(X)

# O nome do método a ser testado necessita começar com "test_"

# Método para testar modelo KNN a partir do arquivo correspondente
def test_modelo_knn():
    # Importando modelo de KNN
    knn_path = 'ml_model/heart_disease_knn.pkl'
    modelo_knn = modelo.carrega_modelo(knn_path)



    # Obtendo as métricas do KNN
    acuracia_knn, recall_knn, precisao_knn, f1_knn = avaliador.avaliar(modelo_knn, X_scaled, Y)

    # Testando as métricas do KNN

    # É a proporção de previsões corretas em relação ao total de previsões feitas pelo modelo KNN.
    assert acuracia_knn >= 0.85

    # Representa a proporção de exemplos positivos corretamente identificados pelo modelo em relação a todos os exemplos positivos existentes.
    assert recall_knn >= 0.85

    #Refere-se à proporção de exemplos corretamente identificados como positivos em relação a todos os exemplos que o modelo classificou como positivos.
    assert precisao_knn >= 0.85

    #É uma média harmônica entre precisão e recall,
    # fornecendo uma medida única que considera o equilíbrio entre essas duas métricas de avaliação do modelo KNN.
    assert f1_knn >= 0.85



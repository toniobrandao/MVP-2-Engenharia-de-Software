import numpy as np
import pickle
import joblib
import os


class Model:
    def carrega_modelo(self, path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model

    def preditor(model, form):
        """Realiza a predição de um paciente com base no modelo treinado
        """

        # Obtém o caminho do diretório atual
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Caminho para o arquivo scaler.pkl
        scaler_path = os.path.join(current_dir, '..', 'ml_model', 'scaler.pkl')

        # Carregar o scaler para padronização dos dados
        with open(scaler_path, 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)

        # Criar um array com os valores das colunas
        X_input = np.array([
            form['age'],
            form['sex'],
            form['cp'],
            form['trestbps'],
            form['chol'],
            form['fbs'],
            form['restecg'],
            form['thalach'],
            form['exang'],
            form['oldpeak'],
            form['slope'],
            form['ca'],
            form['thal']
        ])

        # Aplicar a padronização nos dados de entrada
        X_input_scaled = scaler.transform(X_input.reshape(1, -1))

        # Realizar a predição
        diagnosis = model.predict(X_input_scaled)
        return int(diagnosis[0])

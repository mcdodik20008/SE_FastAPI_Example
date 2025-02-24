import os

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

# Тестирование модели
def test_model(model, input_folder):
    mse_scores = []

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_folder, file_name)
            data = pd.read_csv(file_path)

            X = data[['Day']]
            y_true = data['Temperature']
            y_pred = model.predict(X)

            mse = mean_squared_error(y_true, y_pred)
            mse_scores.append(mse)

    avg_mse = np.mean(mse_scores)
    print(f"Средняя MSE: {avg_mse:.2f}")

# Загрузка обученной модели
from joblib import load
model = load('trained_model.joblib')

# Тестирование модели на данных из папки test_preprocessed
test_model(model, 'test_preprocessed')
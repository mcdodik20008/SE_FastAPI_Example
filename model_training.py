import os

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression


def train_model(input_folder):
    model = LinearRegression()

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_folder, file_name)
            data = pd.read_csv(file_path)

            X = data[['Day']]
            y = data['Temperature']

            model.fit(X, y)

    return model


model = train_model('train_preprocessed')

joblib.dump(model, "trained_model.joblib")
print("Модель успешно обучена.")

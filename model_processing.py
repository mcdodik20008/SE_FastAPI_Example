import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_folder, file_name)
            data = pd.read_csv(file_path)

            scaler = StandardScaler()
            data['Temperature'] = scaler.fit_transform(data[['Temperature']])

            output_path = os.path.join(output_folder, file_name)
            data.to_csv(output_path, index=False)

preprocess_data('train', 'train_preprocessed')
preprocess_data('test', 'test_preprocessed')

print("Данные успешно предобработаны.")
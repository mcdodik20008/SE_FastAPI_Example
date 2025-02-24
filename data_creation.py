import os
from random import Random

import numpy as np
import pandas as pd

os.makedirs('./train', exist_ok=True)
os.makedirs('./test', exist_ok=True)

def generate_data(noise_level=0.1, anomalies=False):
    days = np.arange(1, 366)
    base_temperature = 20 * np.sin(2 * np.pi * days / 365) + 15
    noise = np.random.normal(0, noise_level, len(days))
    temperature = base_temperature + noise

    if anomalies:
        anomaly_indices = np.random.choice(len(days), size=10, replace=False)
        temperature[anomaly_indices] += np.random.choice([-15, 15], size=len(anomaly_indices))

    return pd.DataFrame({'Day': days, 'Temperature': temperature})

rnd = Random()

for i in range(5):
    data = generate_data(noise_level=0.1, anomalies=(rnd.randint(0, 100) % 2 == 0))
    data.to_csv(f'./train/data_{i}.csv', index=False)

for i in range(3):
    data = generate_data(noise_level=0.2, anomalies=(rnd.randint(0, 100) % 2 != 0))
    data.to_csv(f'./test/data_{i}.csv', index=False)

print("Данные успешно сгенерированы.")
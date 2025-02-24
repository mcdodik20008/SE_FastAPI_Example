#!/bin/bash

pip install -r requirements.txt

# Запуск скрипта генерации данных
echo "Run data_creation.py..."
python ./data_creation.py

# Запуск скрипта предобработки данных
echo "Run model_processing.p..."
python ./model_processing.py

# Запуск скрипта обучения модели
echo "Run model_training.py..."
python ./model_training.py

# Запуск скрипта тестирования модели
echo "Run model_testing.py..."
python ./model_testing.py


echo "Pipeline ended."
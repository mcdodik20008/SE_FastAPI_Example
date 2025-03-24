#!/bin/bash

pip3 install -r requirements.txt

# Запуск скрипта генерации данных
echo "Запуск data_creation.py..."
python3 data_creation.py

# Запуск скрипта предобработки данных
echo "Запуск model_processing.py..."
python3 model_processing.py

# Запуск скрипта обучения модели
echo "Запуск model_training.py..."
python3 model_training.py

# Запуск скрипта тестирования модели
echo "Запуск model_testing.py.py..."
python3 model_testing.py

echo "Pipeline завершен."

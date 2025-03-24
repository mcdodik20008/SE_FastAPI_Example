#!/bin/bash
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip

pip install -r requirements.txt

# Запуск скрипта генерации данных
echo "Запуск data_creation.py..."
python data_creation.py

# Запуск скрипта предобработки данных
echo "Запуск model_processing.py..."
python model_processing.py

# Запуск скрипта обучения модели
echo "Запуск model_training.py..."
python model_training.py

# Запуск скрипта тестирования модели
echo "Запуск model_testing.py.py..."
python model_testing.py

echo "Pipeline завершен."

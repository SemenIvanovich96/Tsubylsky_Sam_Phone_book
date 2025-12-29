import json
from pathlib import Path


# Функция загрузки справочника из JSON файла или создания пустого
def load_phonebook(filename=Path('phonebook.json')):
    # Проверяем наличие файла с помощью os.path.exists
    if filename.exists():
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)  # Загружаем данные из файла
    return {"contacts": []}  # Возвращаем пустой справочник если файла нет


# Функция сохранения справочника в JSON файл
def save_phonebook(phonebook, filename='phonebook.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(phonebook, f, ensure_ascii=False, indent=2)  # Сохраняем с отступами

import json
from pathlib import Path


def load_phonebook(filename=Path('phonebook.json')):
    """Функция загрузки справочника из JSON файла или создания пустого."""
    if filename.exists():
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)  # Загружаем данные из файла
    return {"contacts": []}  # Возвращаем пустой справочник если файла нет


def save_phonebook(phonebook, filename='phonebook.json'):
    """ Функция сохранения справочника в JSON файл."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(phonebook, f, ensure_ascii=False, indent=2)  # Сохраняем с отступами

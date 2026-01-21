import json
from pathlib import Path
from typing import Dict, List
from dataclasses import dataclass


@dataclass
class Contact:
    id: str
    name: str
    phone: str
    comment: str


class PhoneBook:
    """Модель — управление данными справочника."""

    def __init__(self, filename=Path('phonebook.json')):
        self.filename = filename
        self.data = {"contacts": []}
        self.load()

    def load(self) -> None:
        """Загрузка из JSON."""
        if self.filename.exists():
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.data = json.load(f)

    def save(self) -> None:
        """Сохранение в JSON."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    @property
    def contacts(self) -> List[Dict[str, str]]:
        """Геттер для списка контактов."""
        return self.data["contacts"]

    def add_contact(self, contact_data: Dict[str, str]) -> None:
        """Добавление контакта."""
        self.contacts.append(contact_data)

    def delete_contact(self, contact_id: str) -> bool:
        """Удаление по ID."""
        for i, contact in enumerate(self.contacts):
            if contact["id"] == contact_id:
                self.contacts.pop(i)
                return True
        return False

    def find_contact(self, query: str) -> List[Dict[str, str]]:
        """Поиск контакта"""
        return [c for c in self.contacts
                if (query.lower() in c["name"].lower() or
                    query.lower() in c["phone"].lower() or
                    query.lower() in c["comment"].lower())]

    def edit_contact(self, contact_id: str, updates: Dict[str, str]) -> bool:
        """Изменение контакта."""
        for contact in self.contacts:
            if contact["id"] == contact_id:
                contact.update(updates)
                return True
        return False

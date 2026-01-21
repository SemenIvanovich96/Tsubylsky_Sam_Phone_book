from typing import Dict, Any


class PhoneBookView:

    @staticmethod
    def add_contact_manual_id(phonebook_data: Dict[str, Any]) -> Dict[str, str] | None:
        """Ввод нового контакта"""
        try:
            new_id = input("Введите ID: ").strip()

            # Проверка уникальности
            if any(c["id"] == new_id for c in phonebook_data["contacts"]):
                print("ID уже существует!")
                return None

            name = input("Имя: ").strip()
            phone = input("Телефон: ").strip()
            comment = input("Комментарий: ").strip()

            return {"id": new_id, "name": name, "phone": phone, "comment": comment}

        except KeyboardInterrupt:
            print("\nОтменено.")
            return None

    @staticmethod
    def show_all(phonebook_data: Dict[str, Any]) -> None:
        """Показать все контакты"""
        if not phonebook_data["contacts"]:
            print("Справочник пуст")
            return
        print("\nID | Имя        | Телефон      | Комментарий")
        print("-" * 50)
        for c in phonebook_data["contacts"]:
            print(f"{c['id']:3} | {c['name']:<10} | {c['phone']:<13} | {c['comment']}")

    @staticmethod
    def search_contact(phonebook_data: Dict[str, Any]) -> None:
        """Поиск контакта"""
        query = input("Поиск (имя/телефон/комментарий): ").strip().lower()
        found = False
        for c in phonebook_data["contacts"]:
            if (query in c["name"].lower() or query in c["phone"].lower() or
                    query in c["comment"].lower()):
                print(f"ID: {c['id']}, {c['name']}: {c['phone']} ({c['comment']})")
                found = True
        if not found:
            print("Не найдено")

    @staticmethod
    def delete_contact(phonebook_data: Dict[str, Any]) -> str | None:
        """Удаление контакта"""
        PhoneBookView.show_all(phonebook_data)
        return input("ID для удаления: ").strip()

    @staticmethod
    def edit_contact(phonebook_data: Dict[str, Any]) -> tuple[str, Dict[str, str]] | None:
        """Изменение контакта"""
        PhoneBookView.show_all(phonebook_data)
        contact_id = input("ID для изменения: ").strip()
        if not contact_id:
            return None

        # Находим контакт для текущих значений
        for contact in phonebook_data["contacts"]:
            if contact["id"] == contact_id:
                updates = {}
                new_name = input(f"Имя [{contact['name']}]: ").strip()
                if new_name:
                    updates["name"] = new_name
                new_phone = input(f"Телефон [{contact['phone']}]: ").strip()
                if new_phone:
                    updates["phone"] = new_phone
                new_comment = input(f"Комментарий [{contact['comment']}]: ").strip()
                if new_comment:
                    updates["comment"] = new_comment
                return contact_id, updates
        return None

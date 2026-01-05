def add_contact_manual_id(phonebook):
    """Добавление нового контакта с вводом ID"""
    try:
        new_id = int(input("Введите ID: "))

        # Проверяем, не существует ли уже такой ID
        for contact in phonebook["contacts"]:
            if contact["id"] == new_id:
                print(" ID уже существует! Выберите другой.")
                return  # Выходим если ID занят

        #  данные контакта
        name = input("Имя: ").strip()
        phone = input("Телефон: ").strip()
        comment = input("Комментарий: ").strip()

        # Создаем словарь контакта
        contact = {
            "id": new_id,
            "name": name,
            "phone": phone,
            "comment": comment
        }

        phonebook["contacts"].append(contact)  # Добавляем в список контактов
        print(f" Контакт '{name}' добавлен с ID {new_id}")

    except ValueError:  # Обработка ошибки ввода не числа
        print(" ID должен быть целым числом!")


def show_all(phonebook):
    """Функция показывает все контакты в таблице."""
    if not phonebook["contacts"]:  # Проверяем пустой ли справочник
        print("Справочник пуст")
        return

    print("\nID | Имя        | Телефон      | Комментарий")
    print("-" * 50)
    # Выводим каждый контакт
    for contact in phonebook["contacts"]:
        print(f"{contact['id']:3} | {contact['name']:<10} | {contact['phone']:<13} | {contact['comment']}")


def search_contact(phonebook):
    """ Поиск контакта по любому полю."""
    query = input("Введите имя, телефон или комментарий: ").strip().lower()
    found = False  # Флаг найденного контакта
    for contact in phonebook["contacts"]:
        # Ищем в любом поле, где есть информация контактов
        if (query in contact["name"].lower() or
                query in contact["phone"].lower() or
                query in contact["comment"].lower()):
            print(f"ID: {contact['id']}, {contact['name']}: {contact['phone']} ({contact['comment']})")
            found = True
    if not found:
        print("Контакт не найден")


def delete_contact(phonebook):
    """ Удаление контакта по ID."""
    show_all(phonebook)  # Показываем список для выбора
    try:
        contact_id = int(input("Введите ID для удаления: "))
        # Ищем контакт по ID и удаляем
        for i, contact in enumerate(phonebook["contacts"]):
            if contact["id"] == contact_id:
                removed = phonebook["contacts"].pop(i)  # Удаляем из списка
                print(f" Удален: {removed['name']} (ID {removed['id']})")
                return
        print("Контакт не найден")
    except ValueError:
        print("Введите корректный ID")


def edit_contact(phonebook):
    """ Изменение существующего контакта"""
    show_all(phonebook)  # Показываем список для выбора
    try:
        contact_id = int(input("Введите ID для изменения: "))

        # Ищем контакт по ID
        for i, contact in enumerate(phonebook["contacts"]):
            if contact["id"] == contact_id:
                print(f"Изменяем: {contact['name']} ({contact['phone']}, {contact['comment']})")

                # Изменяем только заполненные поля (Enter = пропуск)
                new_name = input(f"Новое имя [{contact['name']}]: ").strip()
                if new_name:
                    contact['name'] = new_name

                new_phone = input(f"Новый телефон [{contact['phone']}]: ").strip()
                if new_phone:
                    contact['phone'] = new_phone

                new_comment = input(f"Новый комментарий [{contact['comment']}]: ").strip()
                if new_comment:
                    contact['comment'] = new_comment

                print(f" Контакт ID {contact_id} обновлен!")
                return

        print("Контакт не найден")
    except ValueError:
        print("Введите корректный ID")

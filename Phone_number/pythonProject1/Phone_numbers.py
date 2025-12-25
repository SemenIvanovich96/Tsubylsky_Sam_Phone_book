import json
import os


# Функция загрузки справочника из JSON файла или создания пустого
def load_phonebook(filename='phonebook.json'):
    # Проверяем наличие файла с помощью os.path.exists
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)  # Загружаем данные из файла
    return {"contacts": []}  # Возвращаем пустой справочник если файла нет


# Функция сохранения справочника в JSON файл
def save_phonebook(phonebook, filename='phonebook.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(phonebook, f, ensure_ascii=False, indent=2)  # Сохраняем с отступами


# Загружаем справочник при запуске программы
phonebook = load_phonebook()


# Главное меню программы
def main_menu():
    while True:
        print("\n ТЕЛЕФОННЫЙ СПРАВОЧНИК ")
        print("1 - Добавить контакт")
        print("2 - Показать все контакты")
        print("3 - Найти контакт")
        print("4 - Удалить контакт")
        print("5 - Изменить контакт")
        print("6 - Выход")

        choice = input("Выберите действие (1-6): ").strip()  # Получаем выбор пользователя

        if choice == "1":
            add_contact_manual_id()  # Вызов функции добавления
        elif choice == "2":
            show_all()  # Показать все контакты
        elif choice == "3":
            search_contact()  # Поиск контакта
        elif choice == "4":
            delete_contact()  # Удаление контакта
        elif choice == "5":
            edit_contact()  # Изменение контакта
        elif choice == "6":
            save_phonebook(phonebook)  # Сохраняем перед выходом
            print("Справочник сохранен.")
            break  # Выход из цикла
        else:
            print("Неверный выбор!")


# Добавление нового контакта с вводом ID
def add_contact_manual_id():
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


# Показать все контакты в таблице
def show_all():
    if not phonebook["contacts"]:  # Проверяем пустой ли справочник
        print("Справочник пуст")
        return

    print("\nID | Имя        | Телефон      | Комментарий")
    print("-" * 50)
    # Выводим каждый контакт
    for contact in phonebook["contacts"]:
        print(f"{contact['id']:3} | {contact['name']:<10} | {contact['phone']:<13} | {contact['comment']}")


# Поиск контакта по любому полю
def search_contact():
    query = input("Введите имя, телефон или комментарий: ").strip().lower()
    found = False  # Флаг найденного контакта
    for contact in phonebook["contacts"]:
        # Ищем в любом поле (регистронезависимо)
        if (query in contact["name"].lower() or
                query in contact["phone"].lower() or
                query in contact["comment"].lower()):
            print(f"ID: {contact['id']}, {contact['name']}: {contact['phone']} ({contact['comment']})")
            found = True
    if not found:
        print("Контакт не найден")


# Удаление контакта по ID
def delete_contact():
    show_all()  # Показываем список для выбора
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


# Изменение существующего контакта
def edit_contact():
    show_all()  # Показываем список для выбора
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


# Точка входа в программу
if __name__ == "__main__":
    main_menu()

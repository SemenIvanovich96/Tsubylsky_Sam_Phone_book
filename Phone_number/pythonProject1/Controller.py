from View import add_contact_manual_id, show_all, search_contact, delete_contact, edit_contact
from Model import save_phonebook


def main_menu(phonebook):
    """ Главное меню программы."""
    running = True
    while running:
        print("\n ТЕЛЕФОННЫЙ СПРАВОЧНИК ")
        print("1 - Добавить контакт")
        print("2 - Показать все контакты")
        print("3 - Найти контакт")
        print("4 - Удалить контакт")
        print("5 - Изменить контакт")
        print("6 - Выход")

        choice = input("Выберите действие (1-6): ").strip()  # Получаем выбор пользователя

        if choice == "1":
            add_contact_manual_id(phonebook)  # Вызов функции добавления
        elif choice == "2":
            show_all(phonebook)  # Показать все контакты
        elif choice == "3":
            search_contact(phonebook)  # Поиск контакта
        elif choice == "4":
            delete_contact(phonebook)  # Удаление контакта
        elif choice == "5":
            edit_contact(phonebook)  # Изменение контакта
        elif choice == "6":
            save_phonebook(phonebook)  # Сохраняем перед выходом
            print("Справочник сохранен.")
            running = False  # Выход из цикла
        else:
            print("Неверный выбор!")

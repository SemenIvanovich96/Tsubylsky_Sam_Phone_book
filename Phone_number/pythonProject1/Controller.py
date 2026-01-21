from Model import PhoneBook
from View import PhoneBookView


class PhoneBookController:

    def __init__(self):
        self.model = PhoneBook()
        self.view = PhoneBookView()

    def run(self):
        """Главное меню."""
        running = True
        while running:
            print("\n=== ТЕЛЕФОННЫЙ СПРАВОЧНИК ===")
            print("1 - Добавить контакт    2 - Показать все контакты")
            print("3 - Поиск контакта      4 - Удалить контакт")
            print("5 - Изменить контакт    6 - Выход")

            choice = input("Выбор (1-6): ").strip()

            if choice == "1":
                contact_data = self.view.add_contact_manual_id(self.model.data)
                if contact_data:
                    self.model.add_contact(contact_data)
                    print("контакт добавлен")

            elif choice == "2":
                self.view.show_all(self.model.data)

            elif choice == "3":
                self.view.search_contact(self.model.data)

            elif choice == "4":
                contact_id = self.view.delete_contact(self.model.data)
                if contact_id and self.model.delete_contact(contact_id):
                    print("контакт удален")
                else:
                    print("контакт не найден")

            elif choice == "5":
                result = self.view.edit_contact(self.model.data)
                if result:
                    contact_id, updates = result
                    if self.model.edit_contact(contact_id, updates):
                        print("контакт обновлен")
                    else:
                        print("контакт Не найден")

            elif choice == "6":
                self.model.save()
                print(" Справочник сохранен")
                running = False

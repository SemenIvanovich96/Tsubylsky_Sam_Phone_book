from Model import load_phonebook
from Controller import main_menu

# Точка входа в программу
if __name__ == "__main__":
    phonebook = load_phonebook()
    main_menu(phonebook)1234

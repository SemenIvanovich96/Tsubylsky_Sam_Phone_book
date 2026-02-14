import pytest
from Controller import PhoneBookController
from Model import PhoneBook


@pytest.fixture
def controller(tmp_path):
    """Создаём контроллер с временным файлом."""

    filename = tmp_path / "test.json"
    model = PhoneBook(filename)

    controller = PhoneBookController()
    controller.model = model

    return controller


class TestController:
    def test_add_contact(self, controller, monkeypatch, capsys):
        inputs = ['1', '3', 'Петр', '+79333333333', 'тест', '6']

        def fake_input(prompt=''):
            return inputs.pop(0)

        monkeypatch.setattr('builtins.input', fake_input)
        controller.run()
        captured = capsys.readouterr()
        assert "контакт добавлен" in captured.out

    def test_show_all(self, controller, monkeypatch, capsys):
        controller.model.add_contact({"id": "1", "name": "Иван", "phone": "+7911", "comment": "друг"})
        inputs = ['2', '6']

        def fake_input(prompt=''):
            return inputs.pop(0)

        monkeypatch.setattr('builtins.input', fake_input)
        controller.run()
        captured = capsys.readouterr()
        assert "Иван" in captured.out

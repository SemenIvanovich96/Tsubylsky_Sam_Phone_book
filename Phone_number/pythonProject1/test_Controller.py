import pytest
from Controller import PhoneBookController


@pytest.fixture
def controller(tmp_path):
    filename = tmp_path / "test.json"
    controller = PhoneBookController()
    controller.model.filename = filename
    return controller


class TestController:
    def test_add_contact(self, controller, monkeypatch, capsys):
        inputs = ['1', '3', 'Петр', '+79333333333', 'тест', '6']

        def fake_input(prompt=''):  # ← ОБЯЗАТЕЛЬНО prompt!
            return inputs.pop(0)

        monkeypatch.setattr('builtins.input', fake_input)
        controller.run()

        captured = capsys.readouterr()
        assert "контакт добавлен" in captured.out

    def test_menu_show(self, controller, monkeypatch, capsys):
        controller.model.add_contact({"id": "1", "name": "Иван", "phone": "+7911", "comment": "друг"})

        inputs = ['2', '6']

        def fake_input(prompt=''):
            return inputs.pop(0)

        monkeypatch.setattr('builtins.input', fake_input)
        controller.run()

        captured = capsys.readouterr()
        assert "Иван" in captured.out

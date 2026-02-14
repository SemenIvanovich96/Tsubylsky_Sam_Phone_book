import pytest
from View import PhoneBookView


@pytest.fixture
def sample_data():
    return {"contacts": [
        {"id": "1", "name": "Иван", "phone": "+79111111111", "comment": "друг"},
        {"id": "2", "name": "Мария", "phone": "+79222222222", "comment": "коллега"}
    ]}


class TestView:
    def test_show_all(self, sample_data, capsys):
        """Показ всех контактов """
        PhoneBookView.show_all(sample_data)
        captured = capsys.readouterr()
        assert "Иван" in captured.out
        assert "Мария" in captured.out

    def test_show_empty(self, capsys):
        """Пустой справочник."""
        PhoneBookView.show_all({"contacts": []})
        captured = capsys.readouterr()
        assert "Справочник пуст" in captured.out

    def test_add_duplicate_id(self, sample_data, capsys, monkeypatch):
        """Дубликат ID."""
        monkeypatch.setattr('builtins.input', lambda *args: '1')  # Всегда вводит "1"
        result = PhoneBookView.add_contact_manual_id(sample_data)
        captured = capsys.readouterr()
        assert "ID уже существует!" in captured.out
        assert result is None

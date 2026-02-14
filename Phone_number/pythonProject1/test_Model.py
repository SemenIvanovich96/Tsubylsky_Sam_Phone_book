import pytest
from Model import PhoneBook


@pytest.fixture
def temp_model(tmp_path):
    filename = tmp_path / "phonebook.json"
    model = PhoneBook(filename)
    return model, filename


@pytest.fixture
def model_with_data(temp_model):
    model, filename = temp_model
    contacts = [
        {"id": "1", "name": "Иван", "phone": "+79111111111", "comment": "друг"},
        {"id": "2", "name": "Мария", "phone": "+79222222222", "comment": "коллега"}
    ]
    model.data["contacts"] = contacts
    model.save()
    model.load()
    return model, filename


class TestModel:
    def test_init_empty(self, temp_model):
        model, _ = temp_model
        assert model.contacts == []

    def test_load_save(self, temp_model):
        model, filename = temp_model
        model.add_contact({"id": "1", "name": "Тест", "phone": "+7", "comment": ""})
        model.save()
        model.load()
        assert len(model.contacts) == 1

    def test_add_contact(self, temp_model):
        model, _ = temp_model
        model.add_contact({"id": "1", "name": "Иван", "phone": "+7911", "comment": "друг"})
        assert len(model.contacts) == 1

    def test_delete_success(self, model_with_data):
        model, _ = model_with_data
        result = model.delete_contact("1")
        assert result is True
        assert len(model.contacts) == 1

    def test_delete_not_found(self, temp_model):
        model, _ = temp_model
        result = model.delete_contact("999")
        assert result is False

    @pytest.mark.parametrize("query,expected_count", [
        ("Иван", 1), ("7911", 1), ("друг", 1), ("НЕТ", 0), ("мария", 1)
    ])
    def test_find(self, model_with_data, query, expected_count):
        model, _ = model_with_data
        results = model.find_contact(query)
        assert len(results) == expected_count

    def test_edit_success(self, model_with_data):
        model, _ = model_with_data
        result = model.edit_contact("1", {"phone": "+79999999999"})
        assert result is True
        assert model.contacts[0]["phone"] == "+79999999999"

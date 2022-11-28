import pytest


def test_lookup_by_name(populated_phonebook):
    populated_phonebook.add("Rossmann", "123456789")
    assert "123456789" == populated_phonebook.lookup("Rossmann")


def test_phonebook_contains_all_names(populated_phonebook):
    populated_phonebook.add("Rossmann", "123456789")
    populated_phonebook.add("Missing", "123456789")
    assert populated_phonebook.names() == {"Rossmann", "Missing"}


def test_number_isnt_numeric(populated_phonebook):
    with pytest.raises(ValueError):
        populated_phonebook.add("BadNumber", "telefon")
    assert len(populated_phonebook.names()) == 2

@pytest.mark.parametrize("name, number", [('TooLong', "123456789012")])
def test_number_too_long(populated_phonebook, name, number):
    with pytest.raises(FileExistsError):
        populated_phonebook.add(name, number)
    assert len(populated_phonebook.names()) == 2


@pytest.mark.parametrize("name, number", [('TooShort', "12345678")])
def test_number_too_short(populated_phonebook, name, number):
    with pytest.raises(ValueError):
        populated_phonebook.add(name, number)
    assert len(populated_phonebook.names()) == 2


import pytest


def test_lookup_by_name(empty_phonebook):
    empty_phonebook.add("Rossmann", "123456789")
    assert "123456789" == empty_phonebook.lookup("Rossmann")


def test_phonebook_contains_all_names(populated_phonebook):
    assert populated_phonebook.names() == {"Rossmann", "Missing"}


@pytest.mark.parametrize("name, number", [
    ("Too short", "12345678"),
    ("Too long", "123456789012"),
    ("xx", "1"),
    ("yy", "")
])
def test_wrong_number(empty_phonebook, name, number):
    with pytest.raises(ValueError):
        empty_phonebook.add(name, number)
    assert len(empty_phonebook.names()) == 0

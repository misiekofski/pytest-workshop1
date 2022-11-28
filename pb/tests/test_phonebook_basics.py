def test_lookup_by_name(populated_phonebook):
    populated_phonebook.add("Rossmann", "123456789")
    assert "123456789" == populated_phonebook.lookup("Rossmann")


def test_phonebook_contains_all_names(populated_phonebook):
    populated_phonebook.add("Rossmann", "123456789")
    populated_phonebook.add("Missing", "123456789")
    assert populated_phonebook.names() == {"Rossmann", "Missing"}


def test_number_isnt_numeric(populated_phonebook):
    populated_phonebook.add("Rossmann", "telefon")
    assert len(populated_phonebook.names()) == 0


def test_number_too_long(populated_phonebook):
    populated_phonebook.add("Rossmann", "123456789012")
    assert len(populated_phonebook.names()) == 0


def test_number_too_short(populated_phonebook):
    populated_phonebook.add("Rossmann", "12345678")
    assert len(populated_phonebook.names()) == 0

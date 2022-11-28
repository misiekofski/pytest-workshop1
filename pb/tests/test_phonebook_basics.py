from pb.phonebook import PhoneBook


def test_lookup_by_name():
    phonebook = PhoneBook()
    phonebook.add("Rossmann", "12345678")
    assert "12345678" == phonebook.lookup("Rossmann")


def test_phonebook_contains_all_names():
    phonebook = PhoneBook()
    phonebook.add("Rossmann", "123456789")
    phonebook.add("Missing", "123456789")
    assert phonebook.names() == {"Rossmann", "Missing"}


def test_number_isnt_numeric():
    phonebook = PhoneBook()
    phonebook.add("Rossmann", "telefon")
    assert "telefon" == phonebook.lookup("Rossmann")


def test_number_too_long():
    phonebook = PhoneBook()
    phonebook.add("Rossmann", "123456789012")
    assert "123456789012" == phonebook.lookup("Rossmann")


def test_number_too_short():
    phonebook = PhoneBook()
    phonebook.add("Rossmann", "12345678")
    assert "12345678" == phonebook.lookup("Rossmann")

